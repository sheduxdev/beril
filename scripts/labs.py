#!/usr/bin/env python3
"""List and run the local labs.

./beril labs
./beril labs --run
./beril labs --run web
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABS = {
    "web": ["bash", "labs/web/tests.sh"],
    "rce": ["bash", "labs/rce/tests.sh"],
    "binary": ["bash", "labs/binary/tests.sh"],
    "re": ["bash", "labs/re/tests.sh"],
    "mobile": ["bash", "labs/mobile/tests.sh"],
    "firmware": ["bash", "labs/firmware/tests.sh"],
    "cloud": ["bash", "labs/cloud/tests.sh"],
    "ad": ["bash", "labs/ad/tests.sh"],
    "llm": ["bash", "labs/llm/tests.sh"],
    "detection": ["bash", "labs/detection/tests.sh"],
    "fuzz": [
        "bash",
        "-c",
        "cd labs/fuzz && make -s clean all && timeout 20 ./fuzz corpus -runs=20000 -max_len=256 2>&1 | tail -5",
    ],
}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--run", action="store_true")
    ap.add_argument("name", nargs="?")
    args = ap.parse_args()

    if not args.run:
        for name in LABS:
            print(name)
        print("\nrun one: ./beril labs --run web")
        return

    names = [args.name] if args.name else list(LABS)
    failed = []
    for name in names:
        if name not in LABS:
            sys.exit(f"unknown lab: {name}")
        print(f"== {name}")
        code = subprocess.call(LABS[name], cwd=ROOT)
        if code != 0:
            failed.append(name)
    print("\nfailed: " + (", ".join(failed) if failed else "none"))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
