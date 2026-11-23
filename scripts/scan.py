#!/usr/bin/env python3
"""Unified Beril scan: URL, APK, IPA, PE, ELF, JAR, archive, source, MCP config.

./beril scan --target https://example.com
./beril scan --target https://example.com --active --owned
./beril scan --target ./src --tools --vibe
./beril scan --target ./plugins --jar
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import report_render
import scan_app
import scan_artifact
import scan_mcp
import scan_vibe
import suppress
from beril_model import load_report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", default="", help="URL or local artifact")
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--sarif", action="store_true")
    ap.add_argument("--profile", default="engineer", choices=("engineer", "bugbounty", "smb", "maintainer", "cra"))
    ap.add_argument("--timeout", type=int, default=15, help="web request timeout")
    ap.add_argument("--insecure", action="store_true", help="skip TLS verification on web scans")
    ap.add_argument("--active", action="store_true", help="minimal active probes, needs authorization")
    ap.add_argument("--owned", action="store_true", help="record ownership acknowledgement")
    ap.add_argument("--scope", default="", help="scope file for active scans")
    ap.add_argument("--rate", type=float, default=2.0)
    ap.add_argument("--max-requests", type=int, default=250)
    ap.add_argument("--no-robots", action="store_true")
    ap.add_argument("--tools", action="store_true", help="run optional local tools (semgrep, gitleaks)")
    ap.add_argument("--online-deps", action="store_true", help="query OSV over the network")
    ap.add_argument("--max-files", type=int, default=20_000)
    ap.add_argument("--deep", action="store_true", help="run optional capa, FLOSS, rizin and Ghidra passes")
    ap.add_argument("--jar", action="store_true", help="force JAR / Minecraft plugin triage")
    ap.add_argument("--mcp", action="store_true", help="also lint MCP configuration files")
    ap.add_argument("--vibe", action="store_true", help="also run Supabase/RLS and client-secret checks")
    ap.add_argument("--sbom", default="", help="write a CycloneDX SBOM for source targets")
    ap.add_argument("--fail-on", default="none", choices=("none", "info", "low", "medium", "high", "critical"))
    ap.add_argument("--baseline", default="", help="earlier JSON report; matching findings are suppressed")
    ap.add_argument("--suppress", default="", help="JSON Lines ignore file (.berilignore)")
    ap.add_argument("--header", action="append", default=[], help="Name: value, repeatable")
    ap.add_argument("--cookie", default="")
    ap.add_argument("--auth-file", default="")
    ap.add_argument("--render", action="store_true", help="render JavaScript with Camoufox")
    args = ap.parse_args()

    target = args.target or input("URL or artifact path: ").strip()
    if not target:
        sys.exit("no target given")

    slug = re.sub(r"[^a-zA-Z0-9._-]+", "_", target.replace("https://", "").replace("http://", "")).strip("_")[:80]
    out = args.out or os.path.join("scans", slug or "scan")

    if target.startswith(("http://", "https://")):
        report = scan_app.scan(
            target,
            "active" if args.active else "passive",
            args.timeout,
            args.insecure,
            args.profile,
            args.owned,
            args.scope,
            args.rate,
            args.max_requests,
            not args.no_robots,
            scan_app.headers_from(args),
            args.render,
        )
    else:
        if not os.path.exists(target):
            sys.exit(f"not found: {target}")
        if args.deep:
            cmd = [
                sys.executable,
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "re_triage.py"),
                "--target",
                target,
                "--out",
                out,
                "--capa",
                "--floss",
                "--rizin",
            ]
            if os.environ.get("GHIDRA_HOME"):
                cmd.append("--ghidra")
            if args.json:
                cmd.append("--json")
            if args.tools:
                cmd.append("--tools")
            raise SystemExit(subprocess.call(cmd))
        if args.jar or target.lower().endswith(".jar"):
            import scan_jar

            report = scan_jar.scan(target)
        else:
            report = scan_artifact.scan(target, args.max_files, args.tools, args.online_deps, args.sbom)
        if args.vibe and os.path.isdir(target):
            extra = scan_vibe.scan(target)
            for finding in extra.findings:
                report.add(finding)
            report.scope["checked"] += extra.scope.get("checked", [])
        if args.mcp and os.path.isdir(target):
            extra = scan_mcp.scan(target)
            for finding in extra.findings:
                report.add(finding)
            report.scope["checked"] += extra.scope.get("checked", [])
        report.finish()

    if args.suppress:
        suppress.apply_file(report, args.suppress)
    if args.baseline:
        report.suppress(load_report(args.baseline))

    text = (
        report.to_json()
        if args.json
        else (report_render.render_sarif(report) if args.sarif else report_render.render_markdown(report, args.profile))
    )
    print(text)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    report.write_json(out + ".json")
    with open(out + ".md", "w", encoding="utf-8") as fh:
        fh.write(report_render.render_markdown(report, args.profile) + "\n")
    if args.sarif:
        with open(out + ".sarif", "w", encoding="utf-8") as fh:
            fh.write(report_render.render_sarif(report) + "\n")
    print(f"\nwrote {out}.md and {out}.json", file=sys.stderr)
    if args.fail_on != "none":
        raise SystemExit(report.exit_code(args.fail_on))


if __name__ == "__main__":
    main()
