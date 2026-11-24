#!/usr/bin/env python3
"""Durable knowledge cards. Git is the memory.

    ./beril remember add --title "IDOR needs an owner check" \
      --claim "Object id from the request is trusted without comparing it to the session." \
      --test "Two accounts, swap the id, compare read, update and delete." \
      --proof "Account B reads account A's object." --tags web,idor,access-control \
      --sources references/techniques.md --confidence high
    ./beril remember list
    ./beril remember index
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "knowledge")
INDEX = os.path.join(DIR, "index.json")
CARD_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60]


def parse(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    m = CARD_RE.match(text)
    if not m:
        return {}
    meta, body = m.group(1), m.group(2)
    card = {"path": os.path.relpath(path, ROOT), "body": body.strip()}
    for line in meta.splitlines():
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if key in ("tags", "sources"):
            card[key] = [t.strip() for t in value.split(",") if t.strip()]
        else:
            card[key] = value
    for section, key in (("Claim", "claim"), ("Test", "test"), ("Proof", "proof"), ("Failure modes", "failure")):
        sm = re.search(rf"## {section}\n(.*?)(?=\n## |\Z)", body, re.S)
        card[key] = sm.group(1).strip() if sm else ""
    return card


def load() -> list[dict]:
    if not os.path.isdir(DIR):
        return []
    return [
        c for c in (parse(os.path.join(DIR, f)) for f in sorted(os.listdir(DIR)) if f.endswith(".md")) if c.get("id")
    ]


def rebuild() -> list[dict]:
    cards = load()
    os.makedirs(DIR, exist_ok=True)
    with open(INDEX, "w", encoding="utf-8") as fh:
        json.dump(cards, fh, ensure_ascii=False, indent=1)
    lines = [
        "# Knowledge index",
        "",
        f"{len(cards)} durable cards. Read this before a web search; open a card only when it matches.",
        "",
        "| id | title | tags | confidence | updated |",
        "|---|---|---|---|---|",
    ]
    for c in sorted(cards, key=lambda x: (x.get("tags", [""])[0], x["title"])):
        lines.append(
            f"| `{c['id']}` | {c['title']} | {', '.join(c.get('tags', []))} | {c.get('confidence', '?')} | {c.get('updated', '')} |"
        )
    with open(os.path.join(DIR, "INDEX.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return cards


def write_card(data: dict) -> str:
    os.makedirs(DIR, exist_ok=True)
    path = os.path.join(DIR, data["id"] + ".md")
    text = f"""---
id: {data["id"]}
title: {data["title"]}
tags: {", ".join(data.get("tags", []))}
confidence: {data.get("confidence", "medium")}
updated: {dt.date.today().isoformat()}
uses: {data.get("uses", 0)}
sources: {", ".join(data.get("sources", []))}
status: {data.get("status", "active")}
---
# {data["title"]}

## Claim

{data.get("claim", "")}

## Test

{data.get("test", "")}

## Proof

{data.get("proof", "")}

## Failure modes

{data.get("failure", "")}
"""
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    add = sub.add_parser("add")
    add.add_argument("--title", required=True)
    add.add_argument("--claim", required=True)
    add.add_argument("--test", default="")
    add.add_argument("--proof", default="")
    add.add_argument("--failure", default="")
    add.add_argument("--tags", default="")
    add.add_argument("--sources", default="")
    add.add_argument("--confidence", choices=["high", "medium", "low"], default="medium")
    add.add_argument("--id", default="")

    upd = sub.add_parser("update")
    upd.add_argument("--id", required=True)
    for key in ("title", "claim", "test", "proof", "failure", "tags", "sources", "confidence", "status"):
        upd.add_argument("--" + key, default=None)

    sub.add_parser("list")
    sub.add_parser("index")
    use = sub.add_parser("use")
    use.add_argument("--id", required=True)
    prune = sub.add_parser("prune")
    prune.add_argument("--days", type=int, default=180)

    args = ap.parse_args()
    if args.cmd == "add":
        cid = args.id or slug(args.title)
        if os.path.exists(os.path.join(DIR, cid + ".md")):
            print(f"exists: {cid}; use update")
            return
        write_card(
            {
                "id": cid,
                "title": args.title,
                "claim": args.claim,
                "test": args.test,
                "proof": args.proof,
                "failure": args.failure,
                "tags": [x.strip() for x in args.tags.split(",") if x.strip()],
                "sources": [x.strip() for x in args.sources.split(",") if x.strip()],
                "confidence": args.confidence,
            }
        )
        rebuild()
        print(cid)
    elif args.cmd == "update":
        cards = {c["id"]: c for c in load()}
        if args.id not in cards:
            raise SystemExit("not found")
        c = cards[args.id]
        for key in ("title", "claim", "test", "proof", "failure", "confidence", "status"):
            if getattr(args, key) is not None:
                c[key] = getattr(args, key)
        if args.tags is not None:
            c["tags"] = [x.strip() for x in args.tags.split(",") if x.strip()]
        if args.sources is not None:
            c["sources"] = [x.strip() for x in args.sources.split(",") if x.strip()]
        write_card(c)
        rebuild()
        print("updated", args.id)
    elif args.cmd == "list":
        for c in load():
            print(f"{c['id']:<34} {c.get('confidence','?'):<7} {', '.join(c.get('tags', [])):<28} {c['title']}")
    elif args.cmd == "index":
        print(len(rebuild()), "cards")
    elif args.cmd == "use":
        cards = {c["id"]: c for c in load()}
        if args.id not in cards:
            raise SystemExit("not found")
        c = cards[args.id]
        c["uses"] = int(c.get("uses") or 0) + 1
        write_card(c)
        rebuild()
        print("used", args.id, c["uses"])
    elif args.cmd == "prune":
        cutoff = (dt.date.today() - dt.timedelta(days=args.days)).isoformat()
        n = 0
        for c in load():
            if c.get("updated", "") < cutoff and c.get("confidence") != "high":
                c["status"] = "stale"
                write_card(c)
                n += 1
        rebuild()
        print("stale", n)


if __name__ == "__main__":
    main()
