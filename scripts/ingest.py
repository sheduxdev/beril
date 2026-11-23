#!/usr/bin/env python3
"""Ingest results from another scanner into the Beril report schema.

The point is one brief for a mixed tool chain. SARIF, Nuclei JSONL, Trivy JSON
and Gitleaks JSON are supported. The original finding keeps its tool name and
raw location.

    python scripts/ingest.py --input nuclei.jsonl --format nuclei --target https://app.example
    python scripts/ingest.py --input semgrep.sarif --format sarif --target ./src --profile engineer
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adapters
import report_render
from beril_model import Finding, Report, load_report

FORMATS = ("sarif", "nuclei", "trivy", "gitleaks", "osv", "grype", "zap", "generic")


def sarif_findings(data: dict) -> list[Finding]:
    out = []
    for run in data.get("runs", []):
        rules = {rule.get("id"): rule for rule in run.get("tool", {}).get("driver", {}).get("rules", [])}
        for result in run.get("results", []):
            rule_id = result.get("ruleId", "sarif")
            rule = rules.get(rule_id, {})
            message = (result.get("message") or {}).get("text", "")
            level = result.get("level", rule.get("defaultConfiguration", {}).get("level", "warning"))
            location = (result.get("locations") or [{}])[0].get("physicalLocation", {})
            uri = (location.get("artifactLocation") or {}).get("uri", "")
            line = (location.get("region") or {}).get("startLine", 0)
            out.append(
                Finding(
                    check="sarif." + re.sub(r"\W+", "-", rule_id)[:70],
                    title=rule.get("shortDescription", {}).get("text", message)[:180] or rule_id,
                    severity=adapters.SEVERITY_MAP.get(str(level).lower(), "medium"),
                    confidence="low",
                    evidence=f"{uri}:{line} {message[:300]}",
                    impact=(rule.get("fullDescription", {}).get("text") or message or "Imported finding.")[:400],
                    fix=(rule.get("help", {}).get("text") or "Read the rule and fix at the source.")[:500],
                    subject=f"{uri}:{line}" if uri else report_target_placeholder(),
                    source="tool",
                    tags=["sarif"],
                    false_positive="Imported rule match. Replay before reporting.",
                )
            )
    return out


def report_target_placeholder() -> str:
    return "imported"


def generic_findings(data: list | dict) -> list[Finding]:
    rows = data if isinstance(data, list) else data.get("findings", [])
    out = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        out.append(
            Finding(
                check="import." + re.sub(r"\W+", "-", str(row.get("check", row.get("rule", "finding")))).lower()[:70],
                title=str(row.get("title", row.get("message", "Imported finding")))[:180],
                severity=adapters.SEVERITY_MAP.get(str(row.get("severity", "medium")).lower(), "medium"),
                confidence=str(row.get("confidence", "low")),
                evidence=str(row.get("evidence", row.get("location", "imported")))[:500],
                impact=str(row.get("impact", "Imported finding."))[:400],
                fix=str(row.get("fix", "Review the source tool."))[:500],
                subject=str(row.get("subject", "imported")),
                source="tool",
                tags=["import"],
            )
        )
    return out


def parse(payload: str, fmt: str) -> list[Finding]:
    if fmt == "sarif":
        return sarif_findings(json.loads(payload))
    if fmt == "nuclei":
        return adapters.parse_nuclei(payload)
    if fmt == "trivy":
        return adapters.parse_trivy(payload)
    if fmt == "gitleaks":
        return adapters.parse_gitleaks(payload)
    if fmt == "osv":
        return adapters.parse_osv(payload)
    if fmt == "grype":
        return adapters.parse_grype(payload)
    if fmt == "zap":
        return adapters.parse_zap(payload)
    return generic_findings(json.loads(payload))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True)
    ap.add_argument("--format", required=True, choices=FORMATS)
    ap.add_argument("--target", default="imported")
    ap.add_argument("--profile", default="engineer", choices=("engineer", "bugbounty", "smb", "maintainer", "cra"))
    ap.add_argument("--baseline", default="")
    ap.add_argument("--fail-on", default="none", choices=("none", "info", "low", "medium", "high", "critical"))
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    try:
        with open(args.input, encoding="utf-8", errors="replace") as handle:
            payload = handle.read()
        findings = parse(payload, args.format)
        problems = adapters.validate_findings(findings)
        if problems:
            print("schema: " + "; ".join(problems[:5]), file=sys.stderr)
    except (OSError, json.JSONDecodeError) as exc:
        sys.exit(f"cannot parse input: {exc}")
    report = Report(target=args.target, mode="artifact", profile=args.profile)
    report.scope["checked"] = [f"Imported {len(findings)} findings from {args.format}"]
    report.scope["not_checked"] = ["Original tool coverage and tuning", "Replay of each finding"]
    for finding in findings:
        report.add(finding)
    if args.baseline:
        report.suppress(load_report(args.baseline))
    report.finish()
    text = report.to_json() if args.json else report_render.render_markdown(report, args.profile)
    print(text)
    if args.out:
        report.write_json(args.out + ".json")
        with open(args.out + ".md", "w", encoding="utf-8") as handle:
            handle.write(report_render.render_markdown(report, args.profile) + "\n")
    if args.fail_on != "none":
        raise SystemExit(report.exit_code(args.fail_on))


if __name__ == "__main__":
    main()
