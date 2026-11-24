#!/usr/bin/env python3
"""Turn harvested URLs into method notes: headings, intro, code density.

Examples
--------
python scripts/extract.py --input data/threads.jsonl --out data/thread_details.jsonl --limit 30
python scripts/extract.py --url https://0x00sec.org/some-post/ --out /tmp/note.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guard
from camo import CamoSession, clean

NOW = lambda: dt.datetime.now(dt.UTC).isoformat(timespec="seconds")  # noqa: E731

DYNAMIC = {
    "reddit.com": "shreddit-post",
    "hackerone.com": "main",
    "hackthebox.com": "#main-outlet",
    "forum.hackthebox.com": "#main-outlet",
    "intigriti.com": "main",
}


def browser_view(session: CamoSession, url: str) -> tuple[str, list[str], int]:
    """Read shadow DOM and JS-rendered pages through the live page."""
    selector = next((sel for host, sel in DYNAMIC.items() if host in url), None)
    if not selector:
        return "", [], 0
    try:
        session.page.wait_for_selector(selector, timeout=15_000)
    except Exception:
        pass
    body = session.text_of(selector)
    heads = session.headings(f"{selector} h2, {selector} h3")
    try:
        code = session.page.eval_on_selector_all(f"{selector} pre, {selector} code", "els => els.length")
    except Exception:
        code = 0
    return body, heads, code


def parse(html: str, fallback_title: str = "") -> dict:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
        tag.decompose()
    root = soup.select_one("article") or soup.select_one("main") or soup.body
    if not root:
        return {}
    h1 = root.find("h1")
    title = clean(h1.get_text()) if h1 and len(clean(h1.get_text())) > 8 else clean(fallback_title)
    heads = []
    for h in root.find_all(["h2", "h3"]):
        text = clean(h.get_text())
        if 3 < len(text) < 160 and text not in heads:
            heads.append(text)
    paras = []
    for p in root.find_all("p"):
        text = clean(p.get_text())
        if len(text) > 70 and "cookie" not in text.lower()[:60]:
            paras.append(text)
        if len(paras) >= 8:
            break
    intro = " ".join(paras)[:2600]
    return {
        "title": title,
        "headings": heads[:30],
        "intro": intro,
        "code_blocks": len(root.find_all(["pre", "code"])),
        "tables": len(root.find_all("table")),
    }


def extract_one(session: CamoSession, row: dict, fresh: bool = False) -> dict | None:
    url = row["url"]
    html = session.get(url, fresh=fresh, wait_ms=1200)
    parsed = parse(html or "", row.get("title", ""))
    body, heads, code = browser_view(session, url)
    if body and len(body) > 120:
        parsed["intro"] = body[:3000]
        parsed["headings"] = heads or parsed.get("headings", [])
        parsed["code_blocks"] = max(code, parsed.get("code_blocks", 0))
    if not parsed or (len(parsed.get("intro", "")) < 120 and not parsed.get("headings")):
        return None
    risk = guard.analyze(parsed.get("intro", ""))
    return {
        "type": row.get("type", "thread"),
        "source": row.get("source", ""),
        "url": url,
        "title": parsed.get("title") or row.get("title", ""),
        "headings": parsed.get("headings", []),
        "intro": parsed.get("intro", ""),
        "code_blocks": parsed.get("code_blocks", 0),
        "tables": parsed.get("tables", 0),
        "prompt_risk": risk["level"],
        "prompt_score": risk["risk"],
        "treat_as": "data",
        "collected_at": NOW(),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", default="", help="JSONL with type, source, url, title")
    ap.add_argument("--out", default="data/details.jsonl")
    ap.add_argument("--limit", type=int, default=40)
    ap.add_argument("--source", default="", help="only rows from this source")
    ap.add_argument("--url", default="", help="extract one URL instead of a file")
    ap.add_argument("--delay", type=float, default=1.2)
    ap.add_argument("--cache", default="raw")
    ap.add_argument("--headful", action="store_true")
    ap.add_argument("--fresh", action="store_true")
    args = ap.parse_args()

    if args.url:
        rows = [{"type": "method", "source": "manual", "url": args.url, "title": ""}]
    else:
        with open(args.input, encoding="utf-8") as handle:
            rows = [json.loads(line) for line in handle if line.strip()]
        if args.source:
            rows = [r for r in rows if r.get("source") == args.source]
        rows = [r for r in rows if r.get("url")][: args.limit]

    results = []
    with CamoSession(
        headless=not args.headful, min_delay=args.delay, max_delay=args.delay + 1.2, cache_dir=args.cache or None
    ) as session:
        for i, row in enumerate(rows, 1):
            out = extract_one(session, row, fresh=args.fresh)
            if out:
                results.append(out)
                print(f"{i:>3} {len(out['headings']):>2}h {out['code_blocks']:>3}c {out['url'][:90]}")
            else:
                print(f"{i:>3} skipped (no public body) {row['url'][:80]}")

    if args.url:
        print(json.dumps(results[0] if results else {}, ensure_ascii=False, indent=2))
    else:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as fh:
            for row in results:
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"wrote {len(results)} -> {args.out}")


if __name__ == "__main__":
    main()
