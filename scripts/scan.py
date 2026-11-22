#!/usr/bin/env python3
"""Unified Beril scan: URL, APK, IPA, PE, ELF, archive, or source directory.

    ./beril scan --target https://example.com
    ./beril scan --target ./build/app.apk
    ./beril scan --target ./src --tools
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scan_app  # noqa: E402
import scan_artifact  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", default="", help="URL or local artifact")
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--timeout", type=int, default=15, help="web request timeout")
    ap.add_argument("--insecure", action="store_true", help="skip TLS verification on web scans")
    ap.add_argument("--tools", action="store_true", help="run optional local tools (semgrep, gitleaks, trivy)")
    ap.add_argument("--max-files", type=int, default=20_000)
    args = ap.parse_args()

    target = args.target or input("URL or artifact path: ").strip()
    if not target:
        sys.exit("no target given")

    slug = re.sub(r"[^a-zA-Z0-9._-]+", "_", target.replace("https://", "").replace("http://", "")).strip("_")[:80]
    out = args.out or os.path.join("scans", slug or "scan")

    if target.startswith(("http://", "https://")):
        result = scan_app.scan(target, args.timeout, args.insecure)
        text = scan_app.render(result)
    else:
        if not os.path.exists(target):
            sys.exit(f"not found: {target}")
        result = scan_artifact.scan(target, args.max_files, args.tools)
        text = scan_artifact.render(result)

    print(json.dumps(result, indent=2, ensure_ascii=False) if args.json else text)
    if args.out is not None:
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        open(out + ".json", "w", encoding="utf-8").write(json.dumps(result, indent=2, ensure_ascii=False))
        open(out + ".md", "w", encoding="utf-8").write(text)
        print(f"\nwrote {out}.md and {out}.json", file=sys.stderr)


if __name__ == "__main__":
    main()
