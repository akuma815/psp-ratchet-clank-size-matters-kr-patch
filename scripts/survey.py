#!/usr/bin/env python3
"""Read-only ISO9660 survey and source verification for Ratchet & Clank: Size Matters (KR & JA)."""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOURCES_SPEC = {
    "ja": {
        "role": "japanese_reference_source",
        "root_path": "Ratchet & Clank 5 - Gekitotsu! Dodeka Ginga no MiriMiri Gundan (Japan).iso",
        "extract_dir": "extracted/disc_ja",
        "inventory_manifest": "manifests/iso_inventory_ja.json",
    },
    "ko": {
        "role": "korean_base_target",
        "root_path": "Ratchet & Clank - Size Matters (Korea).iso",
        "extract_dir": "extracted/disc_ko",
        "inventory_manifest": "manifests/iso_inventory_ko.json",
    },
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(8 * 1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_sfo(data: bytes) -> dict[str, str | int]:
    magic, version, keys_off, values_off, count = struct.unpack_from("<5I", data, 0)
    if magic != 0x46535000:
        raise ValueError(f"Invalid PARAM.SFO magic: 0x{magic:08X}")
    result: dict[str, str | int] = {}
    for i in range(count):
        key_off, fmt, length, capacity, val_off = struct.unpack_from("<HHIII", data, 20 + 16 * i)
        key_name = data[keys_off + key_off :].split(b"\x00", 1)[0].decode("utf-8")
        raw = data[values_off + val_off : values_off + val_off + length]
        if fmt == 0x0404:
            result[key_name] = int.from_bytes(raw, "little")
        else:
            result[key_name] = raw.rstrip(b"\x00").decode("utf-8", errors="replace")
    return result


def inspect_iso(iso_path: Path) -> tuple[list[dict[str, object]], dict[str, str | int]]:
    file_size = iso_path.stat().st_size
    files: list[dict[str, object]] = []
    visited: set[int] = set()
    param_sfo_data: bytes | None = None

    with iso_path.open("rb") as f:
        f.seek(16 * 2048)
        pvd = f.read(2048)
        if pvd[:7] != b"\x01CD001\x01":
            raise ValueError(f"Unsupported PVD in {iso_path}")
        block_size = struct.unpack_from("<H", pvd, 128)[0]
        if block_size != 2048:
            raise ValueError(f"Unsupported logical block size {block_size} in {iso_path}")

        def both32(record: bytes, offset: int) -> int:
            le = struct.unpack_from("<I", record, offset)[0]
            be = struct.unpack_from(">I", record, offset + 4)[0]
            if le != be:
                raise ValueError(f"ISO dual-endian mismatch: {le} != {be}")
            return le

        def walk(record: bytes, parent: Path) -> None:
            nonlocal param_sfo_data
            lba = both32(record, 2)
            size = both32(record, 10)
            if lba in visited:
                raise ValueError(f"Directory cycle at LBA {lba}")
            visited.add(lba)
            start = lba * 2048
            if start + size > file_size:
                raise ValueError(f"Directory outside ISO bounds at LBA {lba}")
            f.seek(start)
            block = f.read(size)
            pos = 0
            while pos < size:
                n = block[pos]
                if not n:
                    pos = (pos // 2048 + 1) * 2048
                    continue
                rec = block[pos : pos + n]
                if n < 34 or len(rec) != n or 33 + rec[32] > n:
                    raise ValueError("Truncated ISO directory record")
                pos += n
                raw_name = rec[33 : 33 + rec[32]]
                if raw_name in (b"\x00", b"\x01"):
                    continue
                name = raw_name.decode("ascii").removesuffix(";1")
                if name in ("", ".", "..") or any(c in name for c in "/\\:"):
                    raise ValueError(f"Unsafe ISO path component: {name}")
                rel_path = parent / name
                flags = rec[25]
                if flags & 0x80:
                    raise ValueError(f"Multi-extent record unsupported: {rel_path}")
                if flags & 0x02:
                    walk(rec, rel_path)
                else:
                    extent = both32(rec, 2)
                    length = both32(rec, 10)
                    iso_offset = extent * 2048
                    if iso_offset + length > file_size:
                        raise ValueError(f"File outside ISO bounds: {rel_path}")
                    f.seek(iso_offset)
                    h = hashlib.sha256()
                    remaining = length
                    magic_bytes = b""
                    chunks_for_sfo: list[bytes] = []
                    is_sfo = rel_path.as_posix().upper() == "PSP_GAME/PARAM.SFO"
                    while remaining > 0:
                        chunk = f.read(min(remaining, 4 * 1024 * 1024))
                        if not chunk:
                            raise ValueError(f"Unexpected EOF reading {rel_path}")
                        if len(magic_bytes) < 16:
                            magic_bytes += chunk[: 16 - len(magic_bytes)]
                        if is_sfo:
                            chunks_for_sfo.append(chunk)
                        h.update(chunk)
                        remaining -= len(chunk)
                    if is_sfo:
                        param_sfo_data = b"".join(chunks_for_sfo)
                    files.append(
                        {
                            "path": rel_path.as_posix(),
                            "lba": extent,
                            "iso_offset": iso_offset,
                            "size": length,
                            "sha256": h.hexdigest(),
                            "magic_hex": magic_bytes.hex(),
                        }
                    )

        root_rec = pvd[156 : 156 + pvd[156]]
        walk(root_rec, Path())

    if len({item["path"] for item in files}) != len(files):
        raise ValueError(f"Duplicate file paths in {iso_path}")
    if param_sfo_data is None:
        raise ValueError(f"Missing PSP_GAME/PARAM.SFO in {iso_path}")
    return files, parse_sfo(param_sfo_data)


def extract_key_files(iso_path: Path, files: list[dict[str, object]], out_root: Path) -> list[str]:
    extracted: list[str] = []
    with iso_path.open("rb") as f:
        for item in files:
            rel = str(item["path"])
            upper = rel.upper()
            # Extract PARAM.SFO, UMD_DATA.BIN, ICON0.PNG, SYSDIR/BOOT.BIN, and any localization/binary files
            if (
                upper in ("UMD_DATA.BIN", "PSP_GAME/PARAM.SFO", "PSP_GAME/ICON0.PNG", "PSP_GAME/PIC1.PNG")
                or upper.startswith("PSP_GAME/SYSDIR/")
                or "LOCALDAT" in upper
                or upper.endswith(".BIN")
                or upper.endswith(".PRX")
                or "DATA/HUD" in upper
                or "DATA/FONTS" in upper
                or "DATA/FONT" in upper
            ):
                target = out_root / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                f.seek(int(item["iso_offset"]))
                payload = f.read(int(item["size"]))
                if sha256_bytes(payload) != item["sha256"]:
                    raise ValueError(f"SHA-256 mismatch while extracting {rel}")
                target.write_bytes(payload)
                extracted.append(rel)
    return extracted


def run_survey() -> None:
    sources_summary: dict[str, object] = {}
    for code, spec in SOURCES_SPEC.items():
        iso_path = ROOT / spec["root_path"]
        if not iso_path.exists():
            raise FileNotFoundError(f"Missing ISO: {iso_path}")
        print(f"[*] Inspecting {code.upper()} ISO: {iso_path.name}...")
        iso_sha = sha256_file(iso_path)
        files, sfo = inspect_iso(iso_path)
        print(f"    Title: {sfo.get('TITLE')}, Disc ID: {sfo.get('DISC_ID')}, Version: {sfo.get('DISC_VERSION')}")
        print(f"    Files: {len(files)}, Size: {iso_path.stat().st_size:,} bytes, SHA-256: {iso_sha}")

        # Save inventory
        manifest_path = ROOT / spec["inventory_manifest"]
        save_json(manifest_path, {"iso_name": iso_path.name, "sha256": iso_sha, "size": iso_path.stat().st_size, "param_sfo": sfo, "files": files})

        # Extract key files
        out_root = ROOT / spec["extract_dir"]
        extracted = extract_key_files(iso_path, files, out_root)
        print(f"    Extracted {len(extracted)} key files to {spec['extract_dir']}.")

        sources_summary[code] = {
            "iso_name": iso_path.name,
            "sha256": iso_sha,
            "size": iso_path.stat().st_size,
            "param_sfo": sfo,
            "file_count": len(files),
            "extracted_count": len(extracted),
        }

    save_json(ROOT / "manifests/sources.json", sources_summary)
    print("[+] ISO survey and extraction completed successfully.")


if __name__ == "__main__":
    run_survey()

