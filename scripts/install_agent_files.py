#!/usr/bin/env python3
"""Install Beril's agent entry files into another project.

./scripts/install_agent_files.py --target ~/code/app --agents claude,cursor,copilot
./scripts/install_agent_files.py --target . --agents all
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILES = {
    "claude": "CLAUDE.md",
    "agents": "AGENTS.md",
    "openai": "OPENAI.md",
    "gemini": "GEMINI.md",
    "cursor": ".cursor/rules/beril.mdc",
    "windsurf": ".windsurf/rules/beril.md",
    "cline": ".clinerules/beril.md",
    "copilot": ".github/copilot-instructions.md",
    "aider": ".aider.conf.yml",
    "llms": "llms.txt",
}

EXTRA = {"llms": ["llms-full.txt"]}


def with_header(text: str, root: str) -> str:
    line = f"> Beril root: `{root}`. Run `./beril` from that directory.\n\n"
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return "---" + parts[1] + "---\n\n" + line + parts[2].lstrip()
    return line + text


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", required=True)
    ap.add_argument("--agents", default="all")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    names = list(FILES) if args.agents == "all" else [x.strip() for x in args.agents.split(",") if x.strip()]
    unknown = [n for n in names if n not in FILES]
    if unknown:
        sys.exit(f"unknown agent: {unknown}. Choose from {list(FILES)}")

    target = os.path.abspath(os.path.expanduser(args.target))
    os.makedirs(target, exist_ok=True)

    for name in names:
        rel = FILES[name]
        src = os.path.join(ROOT, rel)
        dst = os.path.join(target, rel)
        if os.path.exists(dst) and not args.force:
            print(f"skip existing {rel}")
            continue
        if args.dry_run:
            print(f"would write {rel}")
            continue
        os.makedirs(os.path.dirname(dst) or target, exist_ok=True)
        text = Path(src).read_text(encoding="utf-8")
        if name != "aider":
            text = with_header(text, ROOT)
        Path(dst).write_text(text, encoding="utf-8")
        print(f"wrote {rel}")
        for extra in EXTRA.get(name, []):
            shutil.copyfile(os.path.join(ROOT, extra), os.path.join(target, extra))
            print(f"wrote {extra}")


if __name__ == "__main__":
    main()
