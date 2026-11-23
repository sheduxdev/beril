#!/usr/bin/env python3
"""Render a Beril report as Markdown, JSON or SARIF.

Four Markdown profiles:

- ``engineer``: full technical detail for the person who will fix it.
- ``bugbounty``: program-ready shape, CVSS/CWE, request pair, impact.
- ``smb``: one page for a non-technical decision maker.
- ``maintainer``: open source disclosure shape for a hunt finding.

All profiles share the same honesty sections: authorization, scope checked,
scope not checked and the limits of the pass. JSON is the source of truth. The
Markdown and SARIF views never contain a finding the JSON lacks.

    python scripts/report.py --input scans/site.json --profile smb --out scans/site-smb.md
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sarif_schema
from beril_model import (
    Finding,
    Report,
    load_report,
    utc_now,
)

ORDER = {s: i for i, s in enumerate(("critical", "high", "medium", "low", "info"))}
SMB_LIGHT = {"critical": "RED", "high": "RED", "medium": "AMBER", "low": "GREEN", "info": "GREEN"}
SEVERITY_LABEL = {"critical": "critical", "high": "high", "medium": "medium", "low": "low", "info": "info"}


def _sorted(report: Report) -> list[Finding]:
    return sorted(report.findings, key=lambda f: (ORDER.get(f.severity, 9), -f.priority()))


def _auth_lines(report: Report) -> list[str]:
    auth = report.authorization or {}
    if not auth:
        return ["- No authorization record. Fine for passive checks, not for active ones."]
    lines = [f"- Method: {auth.get('method', 'not stated')}"]
    if auth.get("evidence"):
        lines.append(f"- Evidence: {auth['evidence']}")
    if auth.get("verified_at"):
        lines.append(f"- Verified at: {auth['verified_at']}")
    if auth.get("expires_at"):
        lines.append(f"- Valid until: {auth['expires_at']}")
    if auth.get("note"):
        lines.append(f"- Note: {auth['note']}")
    return lines


def _scope_lines(report: Report) -> list[str]:
    scope = report.scope or {}
    lines: list[str] = []
    checked = scope.get("checked") or ["(not recorded)"]
    not_checked = scope.get("not_checked") or ["(not recorded)"]
    lines.append("**Checks attempted**")
    lines += [f"- {item}" for item in checked]
    lines += ["", "**Checks not attempted**"]
    lines += [f"- {item}" for item in not_checked]
    if scope.get("in_scope"):
        lines += ["", "**Authorized scope**"]
        lines += [f"- {item}" for item in scope["in_scope"]]
    if scope.get("out_of_scope"):
        lines += ["", "**Out of scope**"]
        lines += [f"- {item}" for item in scope["out_of_scope"]]
    return lines


def _limit_lines(report: Report) -> list[str]:
    limits = report.limits or {}
    lines = []
    labels = [
        ("user_agent", "User agent"),
        ("max_requests", "Request budget"),
        ("requests_sent", "Requests sent"),
        ("rate_per_second", "Rate limit"),
        ("duration_seconds", "Duration"),
        ("waf_backoff", "Backoff on 429/503"),
        ("max_files", "File cap"),
        ("max_bytes_per_file", "Bytes per file"),
        ("execution", "Execution"),
        ("timebox_seconds", "Timebox"),
        ("network", "Network"),
        ("robots", "robots.txt"),
    ]
    for key, label in labels:
        if key in limits and limits[key] not in (None, ""):
            lines.append(f"- {label}: {limits[key]}")
    return lines


def render_markdown(report: Report, profile: str = "engineer") -> str:
    text = _render_markdown(report, profile)
    problems = report.problems()
    if problems:
        block = ["", "## Schema warnings", ""] + [f"- {item}" for item in problems] + [""]
        text = text.rstrip() + "\n" + "\n".join(block)
    return text


def _render_markdown(report: Report, profile: str = "engineer") -> str:
    if profile == "smb":
        return render_smb(report)
    if profile == "bugbounty":
        return render_bugbounty(report)
    if profile == "maintainer":
        return render_maintainer(report)
    if profile == "cra":
        return render_cra(report)
    if profile == "health":
        return render_health(report)
    if profile == "evidence":
        return render_evidence(report)
    return render_engineer(report)


def _header(report: Report, title: str, lines: list[str]) -> None:
    lines += [f"# {title}", ""]
    lines.append(f"Generated {report.finished_at or utc_now()} by Beril {report.tool_version}. Mode: {report.mode}.")
    lines.append("")
    lines.append("| Severity | Count |")
    lines.append("|---|---:|")
    for severity in ("critical", "high", "medium", "low", "info"):
        lines.append(f"| {severity} | {report.counts().get(severity, 0)} |")
    lines.append("")


def render_engineer(report: Report) -> str:
    lines: list[str] = []
    _header(report, f"Scan: {report.target}", lines)
    if report.errors:
        lines += ["## Errors", ""] + [f"- {error}" for error in report.errors] + [""]
    lines += ["## Fix now", ""]
    top = report.top_actions()
    if top:
        for index, finding in enumerate(top, 1):
            lines.append(
                f"{index}. **{finding.title}** ({finding.severity}, confidence {finding.confidence}): {finding.fix}"
            )
    else:
        lines.append("No medium or higher finding with enough confidence in this pass.")
    lines.append("")
    lines += ["## Authorization", "", *_auth_lines(report), ""]
    lines += ["## Scope", "", *_scope_lines(report), ""]
    limits = _limit_lines(report)
    if limits:
        lines += ["## Limits", "", *limits, ""]
    lines += ["## Findings", ""]
    findings = _sorted(report)
    if not findings:
        lines.append(
            "No finding inside these checks. The attempted and skipped lists below show what passed. "
            "That is not a certificate."
        )
        lines.append("")
    for finding in findings:
        lines += [
            f"### [{finding.severity.upper()}] {finding.title}",
            "",
            f"- Confidence: {finding.confidence}" + (" (verified)" if finding.verified else ""),
            f"- Source: {finding.source}",
        ]
        if finding.cwe:
            lines.append(f"- CWE: {', '.join(finding.cwe)}")
        if finding.cvss_score is not None:
            lines.append(f"- CVSS: {finding.cvss_score} {finding.cvss_vector}".rstrip())
        if finding.kev:
            lines.append("- CISA KEV: yes")
        if finding.epss is not None:
            lines.append(f"- EPSS: {finding.epss:.3f}")
        lines += ["", f"**Evidence:** {finding.evidence}"]
        if finding.request:
            lines += ["", "```http", finding.request, "```"]
        if finding.response:
            lines += ["", "```http", finding.response[:1200], "```"]
        lines += ["", f"**Impact:** {finding.impact}", "", f"**Fix:** {finding.fix}"]
        if finding.false_positive:
            lines += ["", f"**Can be a false positive:** {finding.false_positive}"]
        if finding.refs:
            lines += ["", "References: " + " ".join(finding.refs)]
        lines.append("")
    return "\n".join(lines)


def render_bugbounty(report: Report) -> str:
    lines: list[str] = []
    _header(report, f"Bounty report: {report.target}", lines)
    lines += ["## Summary", ""]
    top = report.top_actions()
    if top:
        best = top[0]
        lines.append(f"Highest impact: **{best.title}** ({best.severity}, confidence {best.confidence}).")
    else:
        lines.append("No reportable finding with enough confidence. Candidates are listed as information.")
    lines += ["", "## Authorization and scope", "", *_auth_lines(report), "", *_scope_lines(report), ""]
    lines += ["## Findings", ""]
    for finding in _sorted(report):
        lines += [
            f"### {finding.title}",
            "",
            f"- Severity: {finding.severity}",
            f"- Confidence: {finding.confidence}" + (" (verified)" if finding.verified else ""),
            f"- State: {finding.state}",
            f"- CWE: {', '.join(finding.cwe) or 'none'}",
            f"- CVSS: {finding.cvss_score if finding.cvss_score is not None else 'none'} {finding.cvss_vector}".rstrip(),
            f"- Asset: {finding.subject}",
            "",
        ]
        if finding.request:
            lines += ["**Request**", "", "```http", finding.request, "```", ""]
        if finding.response:
            lines += ["**Response**", "", "```http", finding.response[:1500], "```", ""]
        lines += [
            f"**Evidence:** {finding.evidence}",
            "",
            f"**Impact:** {finding.impact}",
            "",
            f"**Fix:** {finding.fix}",
            "",
        ]
        if finding.false_positive:
            lines += [f"**False positive note:** {finding.false_positive}", ""]
        if finding.refs:
            lines += ["**References:** " + " ".join(finding.refs), ""]
    lines += [
        "## Notes",
        "",
        "Generated with Beril. Every finding carries a configuration, a request pair or a "
        "file location. A line that cannot be replayed is not a finding.",
        "",
    ]
    return "\n".join(lines)


def render_smb(report: Report) -> str:
    critical = report.counts().get("critical", 0) + report.counts().get("high", 0)
    light = "RED" if critical else ("AMBER" if report.counts().get("medium", 0) else "GREEN")
    verdict = {
        "RED": "There is urgent work. Start the five items below today.",
        "AMBER": "Nothing is on fire, but the defence is weak. Fix this within the week.",
        "GREEN": "The short checklist passed. Read the scope section before treating that as safety.",
    }[light]
    lines = [
        f"# Security summary for {report.target}",
        "",
        f"Date: {(report.finished_at or utc_now())[:10]}",
        "",
        f"## Status: {light}",
        "",
        verdict,
        "",
    ]
    lines += ["## Do today", ""]
    top = report.top_actions()
    if top:
        for index, finding in enumerate(top, 1):
            lines.append(
                f"{index}. **{finding.title}.** {finding.fix} "
                f"({SEVERITY_LABEL[finding.severity]} risk, {finding.confidence} confidence)"
            )
    else:
        lines.append("No urgent item. Review the checklist below.")
    lines.append("")
    if critical:
        lines += [
            "## Why it matters",
            "",
            "These items make an attacker's job easier: open doors, leaked keys or outdated components. "
            "Each one can be fixed without stopping normal work.",
            "",
        ]
    lines += [
        "## Traffic light",
        "",
        "| Color | Meaning | Count |",
        "|---|---|---:|",
        f"| Red | Today | {critical} |",
        f"| Amber | This week | {report.counts().get('medium', 0)} |",
        f"| Green | Queue it | {report.counts().get('low', 0) + report.counts().get('info', 0)} |",
        "",
    ]
    lines += ["## Findings", ""]
    for finding in _sorted(report):
        if finding.severity == "info" and finding.confidence == "low":
            continue
        lines += [
            f"### {finding.title}",
            "",
            f"- Importance: {SEVERITY_LABEL[finding.severity]}",
            f"- What we saw: {finding.evidence}",
            f"- What to do: {finding.fix}",
            "",
        ]
        if finding.false_positive:
            lines += [f"- Note: {finding.false_positive}", ""]
    lines += ["## Scope and limits", "", *_scope_lines(report)]
    lines += [
        "",
        "## Data protection note",
        "",
        "If a finding exposes personal data and a breach occurred, the data controller must notify the "
        "authority within 72 hours under KVKK. This report is not legal advice. Ask counsel about the "
        "article 12 duty of care.",
        "",
    ]
    lines += [
        "## Next step",
        "",
        "- Close the red items, then run this scan again.",
        "- Review the skipped areas by hand: logged-in pages and business logic.",
        "- Keep backups, updates and IP restrictions on admin panels even after a clean pass.",
        "",
    ]
    return "\n".join(lines)


def render_maintainer(report: Report) -> str:
    lines = [
        "# Security report",
        "",
        f"Project: {report.target}",
        "",
        "A local, read-only review with Beril produced the candidate findings below. Each one has a file "
        "and a line. The report is AI assisted. The reproduction is included.",
        "",
    ]
    product = report.meta.get("product", "")
    version = report.meta.get("version", "")
    contact = report.meta.get("contact", "")
    if product or version or contact:
        lines += ["## Product", ""]
        if product:
            lines.append(f"- Product: {product}")
        if version:
            lines.append(f"- Affected version: {version}")
        if contact:
            lines.append(f"- Contact: {contact}")
        lines.append("")
    lines += ["## Summary", ""]
    for finding in _sorted(report):
        lines.append(f"- [{finding.severity}/{finding.confidence}] {finding.title} ({finding.subject})")
    lines += ["", "## Detail", ""]
    for finding in _sorted(report):
        lines += [
            f"### {finding.title}",
            "",
            f"- File: {finding.subject}",
            f"- Severity reason: {finding.impact}",
            f"- Evidence: {finding.evidence}",
            f"- Suggested fix: {finding.fix}",
        ]
        if finding.cwe:
            lines.append(f"- CWE: {', '.join(finding.cwe)}")
        if finding.false_positive:
            lines.append(f"- Can be a false positive: {finding.false_positive}")
        lines.append("")
    lines += [
        "## Verification state",
        "",
        "These findings came from static review and a local build. Items marked reproduced ran inside "
        "the sandbox. The rest are candidates.",
        "",
        "## Coordinated disclosure",
        "",
        "Send this through a private channel. Use SECURITY.md or the GitHub private advisory when the "
        "project has one. Otherwise send a short introductory email. Respect the project timeline before "
        "publishing.",
        "",
    ]
    return "\n".join(lines)


def render_evidence(report: Report) -> str:
    """Evidence dossier with one row per claim and its source hash."""
    meta = report.meta
    lines = [
        f"# Evidence dossier: {report.target}",
        "",
        f"{meta.get('claims', 0)} claims, {meta.get('confirmed', 0)} confirmed, "
        f"{meta.get('inferred', 0)} inferred. URL sources were "
        f"{'fetched' if meta.get('fetched') else 'not fetched'}; local copies are hashed.",
        "",
        "A hash proves the copy did not change after this run. It does not prove the " "source is right.",
        "",
        "## Claims",
        "",
        "| # | Claim | Status | Source | SHA-256 |",
        "|---|---|---|---|---|",
    ]
    for finding in report.findings:
        if finding.check not in ("evidence.claim", "evidence.missing-source", "evidence.quote-mismatch"):
            continue
        status = "confirmed" if finding.verified else "check"
        digest = finding.evidence.split("sha256:")[1][:16] if "sha256:" in finding.evidence else "-"
        source = (
            "-"
            if finding.check == "evidence.missing-source"
            else finding.evidence.split(" sha256:")[0].split(" ", 1)[-1]
        )
        lines.append(f"| {finding.subject.split(':')[-1]} | {finding.title} | {status} | {source} | {digest} |")
    lines += ["", "## Flags", ""]
    flags = [f for f in report.findings if f.check not in ("evidence.claim",)]
    if not flags:
        lines.append("No flag.")
    for finding in flags:
        lines += [f"- **{finding.title}** ({finding.severity}): {finding.evidence}", f"  - {finding.fix}"]
    lines += [
        "",
        "## Method",
        "",
        "Each row in `claims.jsonl` is one statement with a `kind` and a `source` or `local` path. "
        "The tool checks presence, hashes the local copy and looks for the quote. Keep the source "
        "copies next to `claims.jsonl`.",
        "",
    ]
    lines += ["## Scope and limits", "", *_scope_lines(report), ""]
    return "\n".join(lines)


def render_health(report: Report) -> str:
    """One page open source health scorecard."""
    scores = report.meta.get("scorecard", {})
    signals = report.meta.get("signals", {})
    overall = round(sum(scores.values()) / len(scores)) if scores else 0
    lines = [
        f"# Project health: {report.target}",
        "",
        f"Overall {overall}/100. This is a maintenance signal, not a quality verdict.",
        "",
        "| Dimension | Score | Why |",
        "|---|---:|---|",
    ]
    reasons = {
        "maintenance": f"{signals.get('authors_last_year', 0)} authors, "
        f"{signals.get('commits_last_year', 0)} commits last year, "
        f"top author share {signals.get('top_author_share', 0)}",
        "release": f"{signals.get('releases_last_year', 0)} releases last year, "
        f"tags signed: {signals.get('signed_tags')}",
        "tests": f"tests: {signals.get('tests')}, CI: {signals.get('ci')}",
        "process": f"SECURITY.md: {signals.get('security_file')}, licence: {signals.get('license') or 'none'}",
        "dependencies": f"{signals.get('direct_components', 0)} components, lockfile: {signals.get('lockfile')}",
        "docs": f"{signals.get('files', 0)} files scanned, README and docs checked",
    }
    for dimension in ("maintenance", "release", "tests", "process", "dependencies", "docs"):
        lines.append(f"| {dimension} | {scores.get(dimension, 0)} | {reasons[dimension]} |")
    lines += ["", "## Signals", ""]
    for key, value in signals.items():
        lines.append(f"- {key}: {value}")
    lines += ["", "## Findings", ""]
    if not report.findings:
        lines.append("No health finding. The absence list below still applies.")
    for finding in _sorted(report):
        lines += [
            f"### {finding.title}",
            "",
            f"- Severity: {finding.severity} ({finding.confidence})",
            f"- Evidence: {finding.evidence}",
            f"- Impact: {finding.impact}",
            f"- Next step: {finding.fix}",
            "",
        ]
    lines += ["## Scope and limits", "", *_scope_lines(report), ""]
    return "\n".join(lines)


def render_cra(report: Report) -> str:
    """EU Cyber Resilience Act shaped vulnerability report."""
    meta = report.meta
    product = meta.get("product", report.target)
    version = meta.get("version", "not stated")
    contact = meta.get("contact", "security@example.invalid")
    fixed = meta.get("fixed_versions", {})
    timeline = (
        ("Found", meta.get("found_at", "TBD")),
        ("Reported", meta.get("reported_at", "TBD")),
        ("Acknowledged", meta.get("acknowledged_at", "TBD")),
        ("Fix target", meta.get("fix_target", "TBD")),
        ("Disclosure", meta.get("disclosure_at", "TBD")),
    )
    lines = [
        "# CRA vulnerability report",
        "",
        f"Product: {product}",
        f"Affected version: {version}",
        f"Contact: {contact}",
        "",
        "This is an engineering report shaped for the EU Cyber Resilience Act "
        "vulnerability handling duties. It is not a conformity assessment.",
        "",
    ]
    lines += ["## Summary", "", "| Severity | Count |", "|---|---:|"]
    for severity in ("critical", "high", "medium", "low", "info"):
        lines.append(f"| {severity} | {report.counts().get(severity, 0)} |")
    lines += ["", "## Findings", ""]
    for finding in _sorted(report):
        lines += [
            f"### {finding.title}",
            "",
            f"- ID: {finding.id}",
            f"- Severity / confidence: {finding.severity} / {finding.confidence}",
            f"- CVSS: {finding.cvss_score if finding.cvss_score else 'not scored'}"
            + (f" ({finding.cvss_vector})" if finding.cvss_vector else ""),
            f"- CWE: {', '.join(finding.cwe) if finding.cwe else 'not assigned'}",
            f"- Affected component: {finding.subject}",
            f"- Fixed version: {fixed.get(finding.id, meta.get('fixed_version', 'TBD'))}",
            f"- Impact: {finding.impact}",
            f"- Remediation: {finding.fix}",
            f"- Evidence: {finding.evidence}",
        ]
        if finding.false_positive:
            lines.append(f"- False positive note: {finding.false_positive}")
        lines.append("")
    lines += [
        "## Timeline",
        "",
        "| Step | Date |",
        "|---|---|",
    ]
    lines += [f"| {label} | {value} |" for label, value in timeline]
    lines += [
        "",
        "Default handling window is 90 days from the report before publication, "
        "shorter when exploitation is observed.",
        "",
        "## CRA article map",
        "",
        "| Article | Duty | Where |",
        "|---|---|---|",
        "| 14 | Handle vulnerabilities in the product | This report and the timeline |",
        "| 18 | Report an actively exploited vulnerability | Timeline and severity |",
        "| 19 | Vulnerability handling process | Fix, fixed version, disclosure |",
        "| 20 | SBOM and component record | `beril sbom --spdx` |",
        "",
        "## Evidence boundary",
        "",
        "Each finding carries a file line or a request pair. A finding without a "
        "reproduction stays a candidate. The scope and limit block below says what "
        "was not tested.",
        "",
    ]
    return "\n".join(lines) + "\n" + "\n".join(["## Scope and limits", "", *_scope_lines(report), ""])


def render_sarif(report: Report) -> str:
    rules, results = [], []
    seen_rules = set()
    for finding in report.findings:
        if finding.check not in seen_rules:
            seen_rules.add(finding.check)
            rules.append(
                {
                    "id": finding.check,
                    "name": finding.title[:80],
                    "shortDescription": {"text": finding.title},
                    "fullDescription": {"text": finding.impact},
                    "help": {"text": finding.fix, "markdown": f"**Fix:** {finding.fix}"},
                    "defaultConfiguration": {"level": _sarif_level(finding.severity)},
                    "properties": {"tags": finding.tags + finding.cwe, "confidence": finding.confidence},
                }
            )
        result = {
            "ruleId": finding.check,
            "level": _sarif_level(finding.severity),
            "message": {"text": f"{finding.title}: {finding.evidence}"},
            "partialFingerprints": {"beril/v1": finding.id},
            "properties": {
                "severity": finding.severity,
                "confidence": finding.confidence,
                "priority": finding.priority(),
                "verified": finding.verified,
            },
        }
        location = _sarif_location(finding)
        if location:
            result["locations"] = [location]
        results.append(result)
    doc = {
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "version": "2.1.0",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "Beril",
                        "version": report.tool_version,
                        "informationUri": "https://github.com/sheduxdev/beril",
                        "rules": rules,
                    }
                },
                "automationDetails": {"id": f"beril/{report.mode}"},
                "results": results,
                "invocations": [
                    {
                        "executionSuccessful": not report.errors,
                        "startTimeUtc": report.started_at,
                        "endTimeUtc": report.finished_at or utc_now(),
                        "toolExecutionNotifications": [
                            {"level": "error", "message": {"text": error}} for error in report.errors
                        ],
                    }
                ],
            }
        ],
    }
    sarif_schema.ensure(doc)
    return json.dumps(doc, indent=2, ensure_ascii=False)


def _sarif_level(severity: str) -> str:
    return {"critical": "error", "high": "error", "medium": "warning", "low": "note", "info": "none"}.get(
        severity, "note"
    )


def _sarif_location(finding: Finding) -> dict | None:
    text = finding.subject
    match = None
    for pattern in (r"^(?P<file>[^\s:]+):(?P<line>\d+)", r"^(?P<file>https?://\S+)$"):
        match = __import__("re").search(pattern, text)
        if match:
            break
    if not match:
        return None
    uri = match.group("file")
    region = {}
    if "line" in match.groupdict() and match.group("line"):
        region = {"startLine": int(match.group("line"))}
    location = {"physicalLocation": {"artifactLocation": {"uri": uri}}}
    if region:
        location["physicalLocation"]["region"] = region
    return location


def write(report: Report, profile: str, out: str) -> str:
    if profile == "json":
        text = report.to_json()
    elif profile == "sarif":
        text = render_sarif(report)
    else:
        text = render_markdown(report, profile)
    if out:
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        with open(out, "w", encoding="utf-8") as handle:
            handle.write(text if text.endswith("\n") else text + "\n")
    return text


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, help="Beril JSON report")
    ap.add_argument(
        "--profile", default="engineer", choices=("engineer", "bugbounty", "smb", "maintainer", "cra", "json", "sarif")
    )
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    report = load_report(args.input)
    text = write(report, args.profile, args.out)
    if not args.out:
        print(text)
    else:
        print(f"wrote {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
