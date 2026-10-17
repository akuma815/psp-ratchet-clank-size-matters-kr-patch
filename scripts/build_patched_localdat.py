#!/usr/bin/env python3
"""Build patched LOCALDAT_K.BIN and HELPLOCALDAT_K.BIN from translation_patches.json
for Ratchet & Clank: Size Matters (UCKS45048).
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import analyze_localdat

ROOT = Path(__file__).resolve().parents[1]

# Sector boundary limits from original ISO9660 allocation:
# HELPLOCALDAT_K: LBA 26528 -> next file at LBA 26544 (gap = 16 sectors = 32,768 bytes)
# LOCALDAT_K: LBA 26544 -> next file at LBA 26608 (gap = 64 sectors = 131,072 bytes)
LIMITS = {
    "localdat": 131072,
    "helplocaldat": 32768,
}


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    patches_path = ROOT / "workspace/translation/translation_patches.json"
    if not patches_path.exists():
        print(f"[-] Patches file not found: {patches_path}", file=sys.stderr)
        return 1

    patches = json.loads(patches_path.read_text(encoding="utf-8"))
    loc_patches = {p["id"]: p for p in patches if p["file"] == "localdat"}
    help_patches = {p["id"]: p for p in patches if p["file"] == "helplocaldat"}

    print(f"[*] Loaded {len(patches)} patches ({len(loc_patches)} LOCALDAT, {len(help_patches)} HELPLOCALDAT).")

    configs = [
        (
            "localdat",
            ROOT / "extracted/disc_ko/PSP_GAME/USRDIR/CODE/HUD/DATA/LOCALDAT_K.BIN",
            ROOT / "build/disc_ko_rebuilt/PSP_GAME/USRDIR/CODE/HUD/DATA/LOCALDAT_K.BIN",
            loc_patches,
        ),
        (
            "helplocaldat",
            ROOT / "extracted/disc_ko/PSP_GAME/USRDIR/CODE/HUD/DATA/HELPLOCALDAT_K.BIN",
            ROOT / "build/disc_ko_rebuilt/PSP_GAME/USRDIR/CODE/HUD/DATA/HELPLOCALDAT_K.BIN",
            help_patches,
        ),
    ]

    for name, src_path, dst_path, p_map in configs:
        orig_bytes = src_path.read_bytes()
        parsed = analyze_localdat.parse_loc_data(orig_bytes, "ko")

        applied = 0
        for entry in parsed["entries"]:
            eid = entry["id"]
            if eid in p_map:
                patch = p_map[eid]
                old_text = entry["text"]
                if old_text != patch["original"]:
                    print(
                        f"[-] Warning: Entry ID {eid} original text mismatch!\n    Expected: {patch['original']!r}\n    Found:    {old_text!r}",
                        file=sys.stderr,
                    )
                entry["text"] = patch["patched"]
                applied += 1

        serialized = analyze_localdat.serialize_loc_data(parsed)
        limit = LIMITS[name]
        print(
            f"[*] {name.upper()}: Applied {applied}/{len(p_map)} patches. "
            f"Size {len(orig_bytes):,} -> {len(serialized):,} bytes (limit: {limit:,} bytes, spare: {limit - len(serialized):,} bytes)"
        )
        if len(serialized) > limit:
            raise ValueError(f"{name.upper()} exceeded sector boundary limit ({len(serialized)} > {limit})!")

        # Round-trip verify parsed serialization
        reparsed = analyze_localdat.parse_loc_data(serialized, "ko")
        reserialized = analyze_localdat.serialize_loc_data(reparsed)
        if reserialized != serialized:
            raise AssertionError(f"{name.upper()} round-trip verification failed!")

        dst_path.parent.mkdir(parents=True, exist_ok=True)
        dst_path.write_bytes(serialized)
        print(f"[+] Written patched {name.upper()} to {dst_path.relative_to(ROOT)} (SHA-256: {sha256_bytes(serialized)})")

    print("[+] All patched localization binaries built and verified successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
