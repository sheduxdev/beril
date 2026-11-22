#!/usr/bin/env python3
"""Read-only scan for an application you own or are authorized to test.

Checks response headers, TLS, cookies, a short list of exposed paths, and
common HTML fingerprints. It does not brute force, fuzz parameters, or send
attack payloads.

    python scripts/scan_app.py --target https://example.com --out scans/example
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import os
import re
import socket
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

UA = "Beril/1.0 (authorized read-only scan; +https://github.com/sheduxdev/beril)"

HEADER_CHECKS = [
    ("strict-transport-security", "medium", "HSTS is missing. Add it on HTTPS responses."),
    ("content-security-policy", "medium", "CSP is missing. Add a policy that fits the app."),
    ("x-content-type-options", "low", "X-Content-Type-Options is missing. Set it to nosniff."),
    ("x-frame-options", "low", "X-Frame-Options is missing. Use CSP frame-ancestors or DENY."),
    ("referrer-policy", "low", "Referrer-Policy is missing. Set strict-origin-when-cross-origin."),
    ("permissions-policy", "low", "Permissions-Policy is missing. Disable unused browser features."),
]

PATHS = [
    ("/.git/HEAD", "high", "Git metadata is web accessible."),
    ("/.env", "critical", "Environment file is web accessible."),
    ("/.svn/entries", "medium", "Subversion metadata is web accessible."),
    ("/backup.zip", "medium", "A backup archive is web accessible."),
    ("/server-status", "low", "Apache server-status is public."),
    ("/phpinfo.php", "medium", "phpinfo output is public."),
    ("/actuator/health", "low", "Spring Actuator health endpoint is public."),
    ("/openapi.json", "info", "OpenAPI document is public. Confirm it is intended."),
    ("/swagger-ui/", "info", "Swagger UI is public. Confirm it is intended."),
    ("/graphql", "info", "GraphQL endpoint responds. Test authorization separately."),
    ("/.well-known/security.txt", "info", "security.txt found. Good sign, not a finding."),
]

MARKERS = {
    "/.git/HEAD": lambda s: s.startswith("ref:") or len(s) == 40,
    "/.env": lambda s: "=" in s and not s.lstrip().startswith("<"),
    "/.svn/entries": lambda s: len(s.strip()) > 0,
    "/backup.zip": lambda s: s[:2] in ("PK", "\x1f\x8b"),
    "/server-status": lambda s: "Apache Server Status" in s,
    "/phpinfo.php": lambda s: "PHP Version" in s,
    "/actuator/health": lambda s: '"status"' in s,
    "/openapi.json": lambda s: '"openapi"' in s or '"swagger"' in s,
    "/swagger-ui/": lambda s: "Swagger UI" in s or "swagger-ui" in s,
    "/graphql": lambda s: "GraphQL" in s or "graphql" in s or '"data"' in s,
    "/.well-known/security.txt": lambda s: "Contact:" in s,
}


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def fetch(url: str, timeout: int = 15, insecure: bool = False) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    ctx = ssl._create_unverified_context() if insecure else None
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            body = resp.read(400_000)
            text = body.decode("utf-8", errors="replace")
            return {"url": resp.geturl(), "status": resp.status,
                    "headers": {k.lower(): v for k, v in resp.headers.items()},
                    "body": text, "bytes": len(body), "error": ""}
    except urllib.error.HTTPError as exc:
        body = exc.read(200_000).decode("utf-8", errors="replace")
        return {"url": url, "status": exc.code,
                "headers": {k.lower(): v for k, v in exc.headers.items()},
                "body": body, "bytes": len(body), "error": f"HTTP {exc.code}"}
    except Exception as exc:
        return {"url": url, "status": 0, "headers": {}, "body": "",
                "bytes": 0, "error": f"{type(exc).__name__}: {exc}"}


def tls_info(url: str, timeout: int = 12) -> dict:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https":
        return {"enabled": False, "reason": "not https"}
    host = parsed.hostname
    port = parsed.port or 443
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, port), timeout=timeout) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as tls:
                cert = tls.getpeercert() or {}
                not_after = cert.get("notAfter", "")
                days = None
                if not_after:
                    try:
                        expiry = dt.datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z").replace(
                            tzinfo=dt.timezone.utc)
                        days = (expiry - dt.datetime.now(dt.timezone.utc)).days
                    except ValueError:
                        pass
                return {"enabled": True, "version": tls.version(),
                        "issuer": dict(x[0] for x in cert.get("issuer", [])),
                        "subject": dict(x[0] for x in cert.get("subject", [])),
                        "not_after": not_after, "days_left": days,
                        "san": [x[1] for x in cert.get("subjectAltName", [])][:20]}
    except Exception as exc:
        return {"enabled": False, "error": f"{type(exc).__name__}: {exc}"}


def check_headers(headers: dict) -> list[dict]:
    findings = []
    for name, severity, advice in HEADER_CHECKS:
        if name not in headers:
            findings.append({"id": f"header-{name}", "severity": severity,
                             "title": f"Missing {name}", "evidence": "Header absent",
                             "advice": advice})
    if "server" in headers:
        findings.append({"id": "header-server", "severity": "info",
                         "title": "Server header exposed", "evidence": headers["server"],
                         "advice": "Remove version details if the server does not need to advertise them."})
    if "x-powered-by" in headers:
        findings.append({"id": "header-powered-by", "severity": "info",
                         "title": "X-Powered-By exposed", "evidence": headers["x-powered-by"],
                         "advice": "Disable the header in production."})
    cors = headers.get("access-control-allow-origin", "")
    if cors == "*":
        findings.append({"id": "cors-wildcard", "severity": "info",
                         "title": "CORS allows any origin",
                         "evidence": "Access-Control-Allow-Origin: *",
                         "advice": "Confirm that public read access is intended."})
    return findings


def check_cookies(headers: dict) -> list[dict]:
    findings = []
    raw = headers.get("set-cookie", "")
    if not raw:
        return findings
    for part in re.split(r",(?=[^;]+=[^;]+)", raw):
        name = part.split("=", 1)[0].strip()
        lower = part.lower()
        missing = [flag for flag in ("secure", "httponly", "samesite") if flag not in lower]
        if missing:
            findings.append({"id": f"cookie-{name}", "severity": "low",
                             "title": f"Cookie {name} is missing flags",
                             "evidence": "missing: " + ", ".join(missing),
                             "advice": "Set Secure, HttpOnly and SameSite on session cookies."})
    return findings


def analyze_html(base: str, body: str, headers: dict) -> list[dict]:
    findings = []
    lower = body.lower()
    tech = []
    for name, needle in (("WordPress", "wp-content"), ("Next.js", "__next_data__"),
                         ("React", "react"), ("Shopify", "cdn.shopify"),
                         ("Cloudflare", "cloudflare"), ("Google Analytics", "gtag("),
                         ("jQuery", "jquery")):
        if needle in lower:
            tech.append(name)
    if tech:
        findings.append({"id": "tech-fingerprint", "severity": "info",
                         "title": "Technology hints", "evidence": ", ".join(tech),
                         "advice": "Keep versions current. Hints are not proof of a vulnerable version."})
    if base.startswith("http://") and re.search(r"<input[^>]+type=[\"']?password", lower):
        findings.append({"id": "password-over-http", "severity": "medium",
                         "title": "Password form on HTTP", "evidence": base,
                         "advice": "Serve the login page over HTTPS and redirect HTTP."})
    if "generator" in lower:
        match = re.search(r'<meta[^>]+name=["\']generator["\'][^>]+content=["\']([^"\']+)', body, re.I)
        if match:
            findings.append({"id": "generator", "severity": "info",
                             "title": "Generator meta tag", "evidence": match.group(1),
                             "advice": "Remove the version if it is not needed."})
    if not body.strip():
        findings.append({"id": "empty-body", "severity": "info",
                         "title": "Empty response body", "evidence": f"{len(body)} bytes",
                         "advice": "Check whether a WAF or a client-side app is expected."})
    return findings


def probe_paths(base: str, timeout: int, insecure: bool) -> list[dict]:
    findings = []

    def one(item):
        path, severity, advice = item
        url = urllib.parse.urljoin(base + "/", path.lstrip("/"))
        res = fetch(url, timeout=timeout, insecure=insecure)
        body = res.get("body", "")
        marker = MARKERS.get(path, lambda s: len(s.strip()) > 0)
        if res["status"] in (200, 401, 403) and marker(body):
            return {"id": "path-" + path.strip("/").replace("/", "-").replace(".", "-"),
                    "severity": severity, "title": f"Exposed {path}",
                    "evidence": f"HTTP {res['status']}, {res['bytes']} bytes, {url}",
                    "advice": advice}
        return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for result in pool.map(one, PATHS):
            if result:
                findings.append(result)
    return findings


def scan(target: str, timeout: int = 15, insecure: bool = False) -> dict:
    if not target.startswith(("http://", "https://")):
        target = "https://" + target
    page = fetch(target, timeout=timeout, insecure=insecure)
    base = page["url"] or target
    title = ""
    match = re.search(r"<title[^>]*>(.*?)</title>", page.get("body", ""), re.I | re.S)
    if match:
        title = re.sub(r"\s+", " ", match.group(1)).strip()[:160]
    findings = []
    findings += check_headers(page.get("headers", {}))
    findings += check_cookies(page.get("headers", {}))
    findings += analyze_html(base, page.get("body", ""), page.get("headers", {}))
    findings += probe_paths(base, timeout, insecure)
    tls = tls_info(base, timeout=timeout)
    if tls.get("enabled") and tls.get("days_left") is not None and tls["days_left"] < 21:
        findings.append({"id": "tls-expiry", "severity": "medium",
                         "title": "TLS certificate expires soon",
                         "evidence": f"{tls['days_left']} days left, {tls.get('not_after')}",
                         "advice": "Renew the certificate and automate the renewal."})
    if tls.get("enabled") and str(tls.get("version", "")) in ("TLSv1", "TLSv1.1"):
        findings.append({"id": "tls-version", "severity": "low",
                         "title": "Older TLS version negotiated",
                         "evidence": str(tls.get("version")), "advice": "Enable TLS 1.2 and 1.3."})
    weights = {"critical": 10, "high": 6, "medium": 3, "low": 1, "info": 0}
    score = sum(weights.get(f["severity"], 0) for f in findings)
    return {"target": target, "final_url": base, "status": page.get("status"),
            "title": title, "scanned_at": now(), "tls": tls,
            "findings": findings, "score": score,
            "counts": {s: sum(1 for f in findings if f["severity"] == s)
                       for s in ("critical", "high", "medium", "low", "info")},
            "error": page.get("error", "")}


def render(result: dict) -> str:
    lines = [f"# Scan: {result['final_url']}", "",
             f"Scanned {result['scanned_at']}. Read-only checks. Score: {result['score']}.", ""]
    lines += ["| Severity | Count |", "|---|---:|"]
    for sev, count in result["counts"].items():
        lines.append(f"| {sev} | {count} |")
    lines += ["", "## Target", "",
              f"- URL: {result['final_url']}",
              f"- HTTP status: {result['status']}",
              f"- Title: {result['title'] or '(none)'}"]
    tls = result.get("tls", {})
    if tls.get("enabled"):
        lines += [f"- TLS: {tls.get('version')}, expires {tls.get('not_after')} ({tls.get('days_left')} days)",
                  f"- Issuer: {tls.get('issuer', {}).get('organizationName', 'unknown')}"]
    if result.get("error"):
        lines.append(f"- Error: {result['error']}")
    lines += ["", "## Findings", ""]
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
    findings = sorted(result["findings"], key=lambda f: order.get(f["severity"], 9))
    if not findings:
        lines.append("No findings from this pass. That is not a clean bill of health; it means the short check list passed.")
    for f in findings:
        lines += [f"### {f['title']}", "",
                  f"- Severity: {f['severity']}",
                  f"- Evidence: {f['evidence']}",
                  f"- Advice: {f['advice']}", ""]
    lines += ["## What this scan does not do", "",
              "- No authentication, fuzzing, injection, or brute force.",
              "- No JavaScript rendering. Use Camoufox harvesters for app flows.",
              "- No vulnerability database match. Run nuclei separately for known CVEs.",
              "- A clean result is a starting point, not a certification.", ""]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", default="", help="URL or host you own or may test")
    ap.add_argument("--out", default="", help="output prefix, for example scans/myapp")
    ap.add_argument("--timeout", type=int, default=15)
    ap.add_argument("--insecure", action="store_true", help="skip TLS verification")
    ap.add_argument("--json", action="store_true", help="print JSON")
    args = ap.parse_args()

    target = args.target or input("Target URL (you must own it or have permission): ").strip()
    if not target:
        sys.exit("no target given")
    result = scan(target, args.timeout, args.insecure)
    text = render(result)
    print(json.dumps(result, indent=2, ensure_ascii=False) if args.json else text)
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        open(args.out + ".json", "w", encoding="utf-8").write(json.dumps(result, indent=2, ensure_ascii=False))
        open(args.out + ".md", "w", encoding="utf-8").write(text)
        print(f"\nwrote {args.out}.md and {args.out}.json", file=sys.stderr)


if __name__ == "__main__":
    main()
