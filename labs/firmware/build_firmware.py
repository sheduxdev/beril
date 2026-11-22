#!/usr/bin/env python3
"""Build a synthetic firmware image with a ZIP payload behind a fake header."""
import io
import os
import zipfile

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rootfs")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "firmware.bin")

buf = io.BytesIO()
with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
    for dirpath, _, files in os.walk(ROOT):
        for name in files:
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, ROOT)
            z.write(full, rel)

with open(OUT, "wb") as fh:
    fh.write(b"BERILFW1\n")
    fh.write(b"\x00" * 256)
    fh.write(buf.getvalue())
    fh.write(b"\xff" * 64)
print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes)")
