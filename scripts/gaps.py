#!/usr/bin/env python3
"""Track knowledge gaps and what closes them.

./beril gaps --next
./beril gaps --cover web-csrf --card web-csrf-samesite
./beril gaps --add web "CORS null origin" high references/techniques.md
"""

from __future__ import annotations

import argparse
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "knowledge", "gaps.json")
MD = os.path.join(ROOT, "knowledge", "GAPS.md")


def load() -> list[dict]:
    return json.load(open(PATH, encoding="utf-8")) if os.path.exists(PATH) else []


def save(rows: list[dict]) -> None:
    with open(PATH, "w", encoding="utf-8") as fh:
        json.dump(rows, fh, ensure_ascii=False, indent=1)
    lines = [
        "# Knowledge gaps",
        "",
        f"{len(rows)} gaps. A gap is a card that does not exist yet, ranked by priority.",
        "",
        "| # | Domain | Gap | Priority | Source | Status |",
        "|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(rows, 1):
        status = r["status"] if r["status"] != "covered" else f"covered by `{r.get('covered_by','')}`"
        lines.append(f"| {i} | {r['domain']} | {r['gap']} | {r['priority']} | `{r['source']}` | {status} |")
    lines += ["", "Close a gap with `./beril remember add`, then `./beril gaps --cover <gap> --card <id>`.", ""]
    with open(MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--next", action="store_true")
    ap.add_argument("--priority", default="")
    ap.add_argument("--domain", default="")
    ap.add_argument("--cover", default="")
    ap.add_argument("--card", default="")
    ap.add_argument("--add", nargs=4, metavar=("DOMAIN", "GAP", "PRIORITY", "SOURCE"))
    ap.add_argument("--index", action="store_true")
    args = ap.parse_args()

    rows = load()
    if args.add:
        domain, gap, priority, source = args.add
        rows.append(
            {
                "id": domain + "-" + gap.lower().split()[0],
                "domain": domain,
                "gap": gap,
                "priority": priority,
                "source": source,
                "covered_by": "",
                "status": "open",
            }
        )
        save(rows)
        print("added")
    elif args.cover:
        for r in rows:
            if r["id"] == args.cover:
                r["status"] = "covered"
                r["covered_by"] = args.card
                save(rows)
                print("covered", args.cover, "->", args.card)
                return
        print("not found")
    elif args.next:
        for r in rows:
            if r["status"] == "open" and r["priority"] == "high":
                print(f"{r['id']} [{r['domain']}] {r['gap']}\n  source: {r['source']}")
                return
        print("no high gaps")
    elif args.index:
        save(rows)
        print(len(rows), "gaps")
    else:
        for r in rows:
            if args.priority and r["priority"] != args.priority:
                continue
            if args.domain and r["domain"] != args.domain:
                continue
            print(f"{r['id']:<28} {r['priority']:<7} {r['status']:<8} {r['gap'][:90]}")


if __name__ == "__main__":
    main()
