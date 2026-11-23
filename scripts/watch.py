#!/usr/bin/env python3
"""Watch one target on an interval and report only new findings.

The first pass becomes the baseline. Later passes suppress it and alert on the
difference. This is the missing continuous mode.

    ./beril watch --target https://app.example --interval 3600
    ./beril watch --target https://app.example --iterations 3 --webhook https://hooks.example/x

Read-only unless ``--active`` is passed with an ownership record.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import report_render
import scan_app
from beril_model import load_report


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def notify(url: str, payload: dict) -> str:
    if not url:
        return ""
    try:
        request = urllib.request.Request(
            url,
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json", "User-Agent": "Beril/1.4 watch"},
        )
        with urllib.request.urlopen(request, timeout=10) as response:
            return f"webhook {response.status}"
    except Exception as exc:
        return f"webhook {type(exc).__name__}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--interval", type=int, default=3600)
    ap.add_argument("--iterations", type=int, default=0, help="0 means until stopped")
    ap.add_argument("--out-dir", default="scans/watch")
    ap.add_argument("--profile", default="engineer", choices=("engineer", "bugbounty", "smb", "maintainer", "cra"))
    ap.add_argument("--active", action="store_true")
    ap.add_argument("--owned", action="store_true")
    ap.add_argument("--scope", default="")
    ap.add_argument("--webhook", default="")
    ap.add_argument("--max-requests", type=int, default=200)
    ap.add_argument("--rate", type=float, default=1.0)
    args = ap.parse_args()
    os.makedirs(args.out_dir, exist_ok=True)
    baseline_path = os.path.join(args.out_dir, "baseline.json")
    baseline = load_report(baseline_path) if os.path.exists(baseline_path) else None
    count = 0
    while True:
        stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        report = scan_app.scan(
            args.target,
            "active" if args.active else "passive",
            profile=args.profile,
            owned=args.owned,
            scope_file=args.scope,
            rate=args.rate,
            max_requests=args.max_requests,
        )
        suppressed = report.suppress(baseline) if baseline else 0
        path = os.path.join(args.out_dir, f"{stamp}.json")
        report.write_json(path)
        with open(path.replace(".json", ".md"), "w", encoding="utf-8") as handle:
            handle.write(report_render.render_markdown(report, args.profile) + "\n")
        if baseline is None:
            baseline = report
            baseline.write_json(baseline_path)
        summary = {
            "target": args.target,
            "at": now(),
            "new": len(report.findings),
            "suppressed": suppressed,
            "counts": report.counts(),
            "top": [f.title for f in report.top_actions()],
            "report": path,
        }
        summary["webhook"] = notify(args.webhook, summary)
        print(json.dumps(summary, ensure_ascii=False))
        count += 1
        if args.iterations and count >= args.iterations:
            break
        time.sleep(max(args.interval, 10))


if __name__ == "__main__":
    main()
