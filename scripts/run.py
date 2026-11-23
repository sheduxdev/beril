#!/usr/bin/env python3
"""Run installed specialist tools and merge them into one Beril report.

This is the orchestration layer: Nuclei, Semgrep, Trivy, Gitleaks, OSV-Scanner,
Grype and testssl. Missing tools are listed, never simulated. Active tools
(Nuclei, testssl) need an ownership record.

    ./beril run --target https://app.example --owned
    ./beril run --target ./repo
    ./beril run --target ./image.tar --only trivy,grype
    ./beril run --list
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adapters
import authz
import report_render
from beril_model import Finding, Report, load_report

URL_TOOLS = ["nuclei", "testssl"]
DIR_TOOLS = ["semgrep", "trivy", "gitleaks", "osv-scanner"]
IMAGE_TOOLS = ["trivy", "grype", "syft"]


def headers_from(args: argparse.Namespace) -> dict:
    headers = {}
    if args.auth_file:
        try:
            with open(args.auth_file, encoding="utf-8") as handle:
                data = json.load(handle)
            headers.update({str(k): str(v) for k, v in data.get("headers", {}).items()})
        except (OSError, json.JSONDecodeError) as exc:
            sys.exit(f"auth file: {exc}")
    for item in args.header:
        key, _, value = item.partition(":")
        if key and value:
            headers[key.strip()] = value.strip()
    if args.cookie:
        headers["Cookie"] = args.cookie
    return headers


def select(target: str, only: list[str], skip: list[str]) -> tuple[list[str], str]:
    if target.startswith(("http://", "https://")):
        tools, kind = URL_TOOLS, "web"
    elif os.path.isdir(target):
        tools, kind = DIR_TOOLS, "source"
    elif os.path.isfile(target):
        tools, kind = IMAGE_TOOLS, "artifact"
    else:
        tools, kind = [], "unknown"
    if only:
        tools = [name for name in only if name in adapters.TOOLS]
    tools = [name for name in tools if name not in skip]
    return tools, kind


def run(
    target: str, tools: list[str], headers: dict, offline: bool, timeout: int, owned: bool, scope_file: str
) -> Report:
    report = Report(target=target, mode="artifact", profile="engineer")
    report.scope["checked"] = [f"Adapter: {name}" for name in tools]
    report.scope["not_checked"] = ["Auth flows", "Business logic", "Manual replay"]
    report.limits = {"tools": tools, "timeout_seconds": timeout, "network": "off" if offline else "on"}
    host = ""
    if target.startswith(("http://", "https://")):
        from urllib.parse import urlsplit

        host = urlsplit(target).hostname or ""
        if any(adapters.TOOLS[name].active for name in tools):
            auth = authz.require(host, owned=owned)
            if not auth:
                raise SystemExit(
                    f"active tools need an ownership record for {host}. "
                    f"Use --owned or `./beril verify --new {host}`."
                )
            report.authorization = auth
        if scope_file:
            scope = authz.load_scope(scope_file)
            if scope and not authz.in_scope(target, scope):
                raise SystemExit("target is outside the scope file")
            report.scope["in_scope"] = scope
    statuses = {}
    for name in tools:
        if not adapters.AVAILABLE[name]:
            statuses[name] = "not installed"
            continue
        if name == "syft":
            stdout, stderr, code = adapters.run_tool(name, target, headers=headers, timeout=timeout, offline=offline)
            if stdout.strip():
                os.makedirs("scans", exist_ok=True)
                path = os.path.join("scans", "sbom-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S") + ".cdx.json")
                with open(path, "w", encoding="utf-8") as handle:
                    handle.write(stdout)
                report.meta["sbom"] = path
                report.add(
                    Finding(
                        check="run.sbom",
                        title="SBOM written",
                        severity="info",
                        confidence="high",
                        evidence=path,
                        impact="Component inventory.",
                        fix="Store it with the image digest.",
                        subject=path,
                        source="tool",
                    )
                )
                statuses[name] = "SBOM written"
            else:
                statuses[name] = f"exit {code}: {stderr[:120]}"
            continue
        findings, error = adapters.run(name, target, headers, offline, timeout)
        for finding in findings:
            report.add(finding)
        if error:
            statuses[name] = error
            continue
        statuses[name] = f"{len(findings)} findings"
    report.meta["tools"] = statuses
    report.finish()
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", default="")
    ap.add_argument("--only", default="")
    ap.add_argument("--skip", default="")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--header", action="append", default=[], help="Name: value, repeatable")
    ap.add_argument("--cookie", default="")
    ap.add_argument("--auth-file", default="")
    ap.add_argument("--owned", action="store_true")
    ap.add_argument("--scope", default="")
    ap.add_argument("--profile", default="engineer", choices=("engineer", "bugbounty", "smb", "maintainer", "cra"))
    ap.add_argument("--fail-on", default="none", choices=("none", "info", "low", "medium", "high", "critical"))
    ap.add_argument("--baseline", default="")
    ap.add_argument("--timeout", type=int, default=420)
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if args.list:
        for item in adapters.list_tools():
            print(f"{'ok' if item['installed'] else '--'} {item['name']:<12} {item['kind']:<9} {item['description']}")
        return
    target = args.target
    if not target:
        sys.exit("give --target")
    only = [x.strip() for x in args.only.split(",") if x.strip()]
    skip = [x.strip() for x in args.skip.split(",") if x.strip()]
    tools, kind = select(target, only, skip)
    if not tools:
        sys.exit("no adapter for this target")
    headers = headers_from(args)
    if args.dry_run:
        print(f"target: {target}")
        print(f"kind: {kind}")
        for name in tools:
            print(" ".join(adapters.build_args(name, target, headers, args.offline)))
        return
    report = run(target, tools, headers, args.offline, args.timeout, args.owned, args.scope)
    if args.baseline:
        report.suppress(load_report(args.baseline))
    text = report.to_json() if args.json else report_render.render_markdown(report, args.profile)
    print(text)
    out = args.out or os.path.join("scans", "run-" + os.path.basename(target.rstrip("/")).replace(".", "_")[:50])
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    report.write_json(out + ".json")
    with open(out + ".md", "w", encoding="utf-8") as handle:
        handle.write(report_render.render_markdown(report, args.profile) + "\n")
    if args.fail_on != "none":
        raise SystemExit(report.exit_code(args.fail_on))


if __name__ == "__main__":
    main()
