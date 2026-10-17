#!/usr/bin/env python3
"""Build a reproducible patched Korean ISO into dist/Ratchet & Clank - Size Matters (Korea) (Updated).iso
by sector-precise injection of patched LOCALDAT_K.BIN and HELPLOCALDAT_K.BIN.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import shutil
import sys
from datetime import datetime, timezone, timedelta

from analyze_localdat import sha256_bytes

KST = timezone(timedelta(hours=9))
ROOT = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    parser = argparse.ArgumentParser(description="Build patched Korean PSP ISO.")
    parser.add_argument("--src-iso", default=str(ROOT / "Ratchet & Clank - Size Matters (Korea).iso"))
    parser.add_argument("--out-iso", default=str(ROOT / "dist/Ratchet & Clank - Size Matters (Korea) (Updated).iso"))
    parser.add_argument(
        "--localdat", default=str(ROOT / "build/disc_ko_rebuilt/PSP_GAME/USRDIR/CODE/HUD/DATA/LOCALDAT_K.BIN")
    )
    parser.add_argument(
        "--helplocaldat", default=str(ROOT / "build/disc_ko_rebuilt/PSP_GAME/USRDIR/CODE/HUD/DATA/HELPLOCALDAT_K.BIN")
    )
    args = parser.parse_args()

    src_iso = pathlib.Path(args.src_iso)
    out_iso = pathlib.Path(args.out_iso)
    loc_path = pathlib.Path(args.localdat)
    help_path = pathlib.Path(args.helplocaldat)

    if not src_iso.exists():
        raise FileNotFoundError(f"Source ISO not found: {src_iso}")
    if not loc_path.exists() or not help_path.exists():
        raise FileNotFoundError("Patched localdat binaries not found; run scripts/build_patched_localdat.py first")

    # Read ISO inventory to get exact LBA offsets and size limits
    inv = json.loads((ROOT / "manifests/iso_inventory_ko.json").read_text(encoding="utf-8"))["files"]
    files_by_path = {item["path"]: item for item in inv}

    loc_info = files_by_path["PSP_GAME/USRDIR/CODE/HUD/DATA/LOCALDAT_K.BIN"]
    help_info = files_by_path["PSP_GAME/USRDIR/CODE/HUD/DATA/HELPLOCALDAT_K.BIN"]

    loc_bytes = loc_path.read_bytes()
    help_bytes = help_path.read_bytes()

    out_iso.parent.mkdir(parents=True, exist_ok=True)
    print(f"Creating patched ISO: {out_iso.name}...")
    shutil.copyfile(src_iso, out_iso)

    with out_iso.open("r+b") as f:
        # 1. Inject LOCALDAT_K.BIN
        f.seek(loc_info["iso_offset"])
        f.write(loc_bytes)
        # Pad remainder of original extent if any
        if len(loc_bytes) < loc_info["size"]:
            f.write(b"\x00" * (loc_info["size"] - len(loc_bytes)))

        # 2. Inject HELPLOCALDAT_K.BIN
        f.seek(help_info["iso_offset"])
        f.write(help_bytes)
        if len(help_bytes) < help_info["size"]:
            f.write(b"\x00" * (help_info["size"] - len(help_bytes)))

    out_size = out_iso.stat().st_size
    h = hashlib.sha256()
    with out_iso.open("rb") as f:
        while chunk := f.read(8 * 1024 * 1024):
            h.update(chunk)
    out_sha256 = h.hexdigest()

    report = {
        "generated_at": datetime.now(KST).isoformat(timespec="seconds"),
        "status": "ok",
        "output_iso": str(out_iso.relative_to(ROOT)).replace("\\", "/"),
        "size_bytes": out_size,
        "sha256": out_sha256,
        "injections": [
            {
                "file": "PSP_GAME/USRDIR/CODE/HUD/DATA/LOCALDAT_K.BIN",
                "iso_offset": loc_info["iso_offset"],
                "lba": loc_info["lba"],
                "original_size": loc_info["size"],
                "patched_size": len(loc_bytes),
                "patched_sha256": sha256_bytes(loc_bytes),
            },
            {
                "file": "PSP_GAME/USRDIR/CODE/HUD/DATA/HELPLOCALDAT_K.BIN",
                "iso_offset": help_info["iso_offset"],
                "lba": help_info["lba"],
                "original_size": help_info["size"],
                "patched_size": len(help_bytes),
                "patched_sha256": sha256_bytes(help_bytes),
            },
        ],
    }

    report_path = ROOT / "qa/reports/build_iso_report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
