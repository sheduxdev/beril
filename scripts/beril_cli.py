#!/usr/bin/env python3
"""Thin command wrapper for Beril.

./beril scan --target https://example.com --active
./beril recon --target example.com
./beril verify --new example.com
./beril hunt --target ./repo --sandbox
./beril harvest forums --sources 0x00sec,reddit
./beril dossier
./beril report --input scans/site.json --profile smb
./beril dashboard
"""

from __future__ import annotations

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
COMMANDS = {
    "scan": "scan.py",
    "recon": "recon.py",
    "verify": "authz.py",
    "secrets": "beril_secrets.py",
    "mcp": "scan_mcp.py",
    "jar": "scan_jar.py",
    "vibe": "scan_vibe.py",
    "deps": "deps.py",
    "sbom": "sbom.py",
    "hunt": "hunt.py",
    "triage": "triage_crash.py",
    "guard": "guard.py",
    "report": "report_render.py",
    "priority": "priority.py",
    "bgp": "bgp.py",
    "run": "run.py",
    "ingest": "ingest.py",
    "watch": "watch.py",
    "infra": "infra.py",
    "image": "image.py",
    "netcheck": "netcheck.py",
    "feeds": "feeds.py",
    "benchmark": "benchmark.py",
    "health": "project_health.py",
    "evidence": "evidence.py",
    "incidents": "incidents.py",
    "current": "current_brief.py",
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
    "recall": "recall.py",
    "remember": "remember.py",
    "gaps": "gaps.py",
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
