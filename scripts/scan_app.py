#!/usr/bin/env python3
"""Beril web scan: passive by default, minimal active probes behind a gate.

Passive mode sends ordinary GETs: headers, cookies, CORS, exposed paths, TLS,
DNS mail policy, common ports and page fingerprints. Active mode adds one
quote, one marker, one redirect and one traversal probe per discovered
parameter, plus OPTIONS and TRACE. No writes, no brute force, no fuzzing.

Active mode requires an ownership record from ``scripts/authz.py`` or an
explicit ``--owned`` acknowledgement. A scope file narrows the allowed hosts.

    python scripts/authz.py --new example.com        # then publish the token
    python scripts/authz.py --verify example.com
    python scripts/scan_app.py --target https://example.com --active

    python scripts/scan_app.py --target https://example.com --profile smb --out scans/site
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import active
import authz
import report_render
import web_checks
from beril_model import Report, load_report

CHECKED_PASSIVE = [
    "Security headers and CSP content",
    "Cookie flags",
    "CORS behavior (one Origin)",
    "Common exposed files and admin paths",
    "TLS certificate, expiry and version",
    "SPF, DKIM and DMARC records",
    "MySQL, PostgreSQL, MongoDB, Redis, Elasticsearch, Memcached, Docker, SSH, RDP, SMB, VNC and 12 more ports",
    "Technology and version hints, error signatures, directory listing",
]
NOT_CHECKED_PASSIVE = [
    "Pages and APIs behind a login",
    "Business logic, authorization and IDOR",
    "Parameter injection (active mode required)",
    "Content built by JavaScript",
    "Subdomains and hosts outside the inventory",
    "WAF rule quality and rate limit policy",
    "Known CVE matching (dependency scan is a separate command)",
]


def headers_from(args: argparse.Namespace) -> dict:
    headers: dict = {}
    if args.auth_file:
        try:
            with open(args.auth_file, encoding="utf-8") as handle:
                headers.update({str(k): str(v) for k, v in json.load(handle).get("headers", {}).items()})
        except (OSError, json.JSONDecodeError) as exc:
            raise SystemExit(f"auth file: {exc}") from exc
    for item in args.header:
        key, _, value = item.partition(":")
        if key and value:
            headers[key.strip()] = value.strip()
    if args.cookie:
        headers["Cookie"] = args.cookie
    return headers


def render_page(url: str) -> tuple[str, str]:
    """Render a page with Camoufox.

    Args:
        url: Target URL.

    Returns:
        HTML and an error string.
    """
    try:
        from camo import CamoSession

        with CamoSession(headless=True, cache_dir=None, min_delay=0.0, max_delay=0.2) as session:
            html = session.get(url, wait_ms=1500)
        return html or "", "" if html else "empty render"
    except Exception as exc:
        return "", f"{type(exc).__name__}: {exc}"


def normalize(target: str) -> str:
    if not re.match(r"^https?://", target):
        return "https://" + target
    return target


def host_of(url: str) -> str:
    return urllib.parse.urlsplit(url).hostname or ""


def safe(fetcher: web_checks.Fetcher, url: str, **kwargs: object) -> dict:
    """A request that never raises the budget guard into the orchestrator."""
    try:
        return fetcher.request(url, **kwargs)
    except web_checks.BudgetExceeded:
        fetcher.stopped = True
        return {
            "url": url,
            "status": 0,
            "headers": [],
            "body": "",
            "error": "request budget spent",
            "elapsed_ms": 0,
            "request": "",
        }


def gate(url: str, owned: bool, scope_file: str) -> tuple[dict, dict]:
    host = host_of(url)
    auth = authz.require(host, owned=owned)
    scope = authz.load_scope(scope_file)
    if scope and not authz.in_scope(url, scope):
        raise SystemExit(f"target is outside the scope file: {url}\nscope: {scope_file}")
    if not auth:
        raise SystemExit(
            f"no authorization record for an active scan: {host}\n\n"
            f"  1) python scripts/authz.py --new {host}\n"
            f"  2) publish the token in DNS TXT, /.well-known/beril-verify.txt or a meta tag\n"
            f"  3) python scripts/authz.py --verify {host}\n\n"
            f"or acknowledge ownership with --owned\n"
            f"or stay passive and drop --active"
        )
    return auth, {"in_scope": scope}


def scan(
    target: str,
    mode: str = "passive",
    timeout: int = 15,
    insecure: bool = False,
    profile: str = "engineer",
    owned: bool = False,
    scope_file: str = "",
    rate: float = 2.0,
    max_requests: int = 250,
    respect_robots: bool = True,
    headers: dict | None = None,
    render: bool = False,
) -> Report:
    target = normalize(target)
    host = host_of(target)
    authorization = {}
    in_scope = []
    if mode == "active":
        authorization, gate_info = gate(target, owned, scope_file)
        in_scope = gate_info["in_scope"]
    elif scope_file:
        scope = authz.load_scope(scope_file)
        if scope and not authz.in_scope(target, scope):
            raise SystemExit(f"target is outside the scope file: {target}")
        in_scope = scope

    report = Report(target=target, mode=mode, profile=profile)
    report.authorization = authorization
    report.scope["in_scope"] = in_scope
    report.scope["out_of_scope"] = ["Out of scope subdomains", "Write operations", "Authenticated areas"]
    report.limits = {
        "user_agent": web_checks.UA,
        "max_requests": max_requests,
        "rate_per_second": rate,
        "robots": "respected" if respect_robots else "off",
    }
    if not host:
        report.errors.append("could not resolve the target host")
        return report.finish()

    fetcher = web_checks.Fetcher(
        timeout=timeout,
        insecure=insecure,
        rate=rate,
        max_requests=max_requests,
        respect_robots=respect_robots,
        extra_headers=headers,
    )
    origin = "https://beril.example"
    report.scope["checked"] = list(CHECKED_PASSIVE)
    report.scope["not_checked"] = list(NOT_CHECKED_PASSIVE)

    report.meta = {
        "final_url": target,
        "render": "camoufox" if render else "http",
        "title": "",
        "tls": {},
        "fingerprint": {},
    }
    if render:
        html, render_error = render_page(target)
        if html:
            page = {
                "url": target,
                "status": 200,
                "headers": [],
                "body": html,
                "bytes": len(html),
                "error": "",
                "request": "GET (rendered)",
            }
            report.scope["checked"].append("JavaScript render (Camoufox)")
        else:
            report.errors.append("render failed: " + render_error)
            page = safe(fetcher, target, origin=origin)
    else:
        page = safe(fetcher, target, origin=origin)
    report.meta["status"] = page.get("status", 0)
    report.meta["final_url"] = page.get("url", target)
    if page.get("status") == 0:
        report.errors.append(page.get("error", "connection failed"))
        return report.finish()
    body = page.get("body", "")
    final = page.get("url") or target
    match = re.search(r"<title[^>]*>(.*?)</title>", body, re.I | re.S)
    if match:
        report.meta["title"] = re.sub(r"\s+", " ", match.group(1)).strip()[:160]
    final_host = host_of(final)
    if final_host and final_host != host:
        report.meta["redirected_to"] = final
        if mode == "active" and not authz.in_scope(final, in_scope or [final_host]):
            report.errors.append(f"response redirected to another host: {final_host}. Check the scope.")

    page_headers = web_checks.header_map(page)
    for finding in web_checks.check_headers(page, final):
        report.add(finding)
    for finding in web_checks.check_cookies(page, final):
        report.add(finding)
    for finding in web_checks.check_cors(page, final, origin):
        report.add(finding)
    for finding in web_checks.analyze_html(final, body, page_headers):
        report.add(finding)
    if final.startswith("https://"):
        tls = web_checks.tls_info(final, timeout=min(timeout, 12))
        report.meta["tls"] = tls
        for finding in web_checks.check_tls(tls, final):
            report.add(finding)
    for finding in web_checks.check_redirect_https(target, fetcher):
        report.add(finding)
    for finding in web_checks.check_email(host):
        report.add(finding)
    for finding in web_checks.check_ports(host):
        report.add(finding)

    soft404 = (0, "")
    rnd = urllib.parse.urljoin(final.rstrip("/") + "/", "beril-missing-%08x.txt" % (abs(hash(final)) & 0xFFFFFFFF))
    probe = safe(fetcher, rnd, origin=origin, max_body=60_000)
    if probe.get("status") == 200:
        soft404 = (len(probe.get("body", "")), web_checks.sha(probe.get("body", "")))
    for finding in web_checks.probe_paths(final, fetcher, soft404, origin):
        report.add(finding)
    robots_url = urllib.parse.urljoin(final.rstrip("/") + "/", "robots.txt")
    robots = safe(fetcher, robots_url, origin=origin, max_body=80_000)
    if robots.get("status") == 200:
        for finding in web_checks.check_robots_disclosure(robots.get("body", ""), robots_url):
            report.add(finding)

    if mode == "active":
        report.scope["checked"] += [
            "SQL error signature (single quote)",
            "Reflection (XSS marker)",
            "Open redirect",
            "Path traversal",
            "OPTIONS and TRACE",
        ]
        report.scope["not_checked"] += [
            "Time based injection",
            "Authenticated IDOR",
            "File upload and SSRF",
            "POST bodies",
        ]
        for finding in active.run(final, body, fetcher, origin):
            report.add(finding)

    report.limits["requests_sent"] = fetcher.sent
    report.limits["waf_backoff"] = fetcher.backoff_events
    if fetcher.stopped:
        report.errors.append(f"request budget spent ({max_requests}). Remaining paths were skipped")
    report.meta["fingerprint"] = {"sha256_16": web_checks.sha(body), "bytes": len(body)}
    report.finish()
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", default="", help="URL or host")
    ap.add_argument("--active", action="store_true", help="minimal active probes, needs authorization")
    ap.add_argument("--owned", action="store_true", help="record an ownership acknowledgement for this host")
    ap.add_argument("--scope", default="", help="scope file: hosts, *.hosts or host/path prefixes")
    ap.add_argument("--profile", default="engineer", choices=("engineer", "bugbounty", "smb", "maintainer", "cra"))
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--sarif", action="store_true")
    ap.add_argument("--timeout", type=int, default=15)
    ap.add_argument("--insecure", action="store_true")
    ap.add_argument("--rate", type=float, default=2.0, help="requests per second per target")
    ap.add_argument("--max-requests", type=int, default=250)
    ap.add_argument("--no-robots", action="store_true", help="ignore robots.txt")
    ap.add_argument("--fail-on", default="none", choices=("none", "info", "low", "medium", "high", "critical"))
    ap.add_argument("--baseline", default="", help="earlier JSON report; matching findings are suppressed")
    ap.add_argument("--header", action="append", default=[], help="Name: value, repeatable")
    ap.add_argument("--cookie", default="")
    ap.add_argument("--auth-file", default="", help="JSON with a headers object")
    ap.add_argument("--render", action="store_true", help="render JavaScript with Camoufox")
    args = ap.parse_args()
    target = args.target or input("Target URL (own it or have permission): ").strip()
    if not target:
        sys.exit("no target given")
    report = scan(
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
        headers_from(args),
        args.render,
    )
    if args.baseline:
        report.suppress(load_report(args.baseline))
    text = report_render.render_markdown(report, args.profile)
    if args.json:
        text = report.to_json()
    if args.sarif:
        text = report_render.render_sarif(report)
    print(text)
    out = args.out or os.path.join(
        "scans",
        re.sub(r"[^a-zA-Z0-9._-]+", "_", target.replace("https://", "").replace("http://", "")).strip("_")[:80]
        or "scan",
    )
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    report.write_json(out + ".json")
    with open(out + ".md", "w", encoding="utf-8") as fh:
        fh.write(report_render.render_markdown(report, args.profile) + "\n")
    if args.sarif:
        with open(out + ".sarif", "w", encoding="utf-8") as fh:
            fh.write(report_render.render_sarif(report) + "\n")
    print(f"\nwrote {out}.json and {out}.md", file=sys.stderr)
    if args.fail_on != "none":
        raise SystemExit(report.exit_code(args.fail_on))


if __name__ == "__main__":
    main()
