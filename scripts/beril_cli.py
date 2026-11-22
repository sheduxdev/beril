#!/usr/bin/env python3
"""Thin command wrapper for Beril.

    ./beril scan --target https://example.com
    ./beril harvest forums --sources 0x00sec,reddit
    ./beril dossier
    ./beril dashboard
    ./beril job log --type scan --title "example.com" --status done
"""
from __future__ import annotations

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
COMMANDS = {
    "scan": "scan.py",
    "harvest": "harvest.py",
    "extract": "extract.py",
    "dossier": "build_dossier.py",
    "validate": "validate.py",
    "re": "re_triage.py",
    "train": "train.py",
    "labs": "labs.py",
    "reflect": "reflect.py",
    "github": "github_sweep.py",
    "dashboard": "dashboard.py",
    "job": "job.py",
}


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help", "help"):
        print(__doc__)
        print("commands: " + ", ".join(COMMANDS))
        return
    cmd, rest = args[0], args[1:]
    if cmd not in COMMANDS:
        sys.exit(f"unknown command: {cmd}. Choose from {', '.join(COMMANDS)}")
    script = os.path.join(HERE, COMMANDS[cmd])
    raise SystemExit(subprocess.call([sys.executable, script, *rest]))


if __name__ == "__main__":
    main()
