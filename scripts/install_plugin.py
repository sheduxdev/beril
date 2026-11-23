#!/usr/bin/env python3
"""Install the Beril plugin files into another project.

./scripts/install_plugin.py --agent claude --dest ~/code/myapp
./scripts/install_plugin.py --agent all --dest ~/code/myapp --force
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugin"
MAP = {
    "claude": ("claude-code", Path(".claude") / "plugins" / "beril"),
    "codex": ("codex", Path(".codex") / "beril"),
    "gemini": ("gemini", Path(".gemini") / "extensions" / "beril"),
}


def install(agent: str, dest: Path, force: bool) -> list[str]:
    source_name, relative = MAP[agent]
    source = PLUGIN / source_name
    target = dest / relative
    if target.exists() and not force:
        raise SystemExit(f"{target} exists, use --force")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, dirs_exist_ok=True)
    return [str(target)]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--agent", required=True, choices=("claude", "codex", "gemini", "all"))
    ap.add_argument("--dest", required=True)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    dest = Path(os.path.expanduser(args.dest)).resolve()
    if not dest.is_dir():
        sys.exit(f"destination is not a directory: {dest}")
    agents = list(MAP) if args.agent == "all" else [args.agent]
    for agent in agents:
        for path in install(agent, dest, args.force):
            print(f"installed {agent}: {path}")
    print("Beril CLI still runs from the repository. Point the agent at its absolute path.")


if __name__ == "__main__":
    main()
