#!/usr/bin/env python3
"""Passive web checks used by scan_app.py.

Read-only GETs, a request budget, a per-host rate limit and a robots.txt
check. Every finding carries the request line and a short response excerpt.
No payload hits a parameter here; that lives in active.py and needs an
ownership record.

The module is deliberately boring. Checks are small, named functions and each
one can be tested with a local server.
"""

from __future__ import annotations

import concurrent.futures
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import socket
import ssl
import subprocess
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser

import paths
from beril_model import Finding

UA = "Beril/1.4 (authorized read-only scan; +https://github.com/sheduxdev/beril)"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SECURITY_HEADERS = [
    (
        "strict-transport-security",
        "medium",
        "HSTS missing",
        "Add Strict-Transport-Security with a long max-age on HTTPS.",
    ),
    ("content-security-policy", "medium", "CSP missing", "Add a Content-Security-Policy that fits the app."),
    ("x-content-type-options", "low", "X-Content-Type-Options missing", "Set nosniff."),
    ("x-frame-options", "low", "X-Frame-Options missing", "Use CSP frame-ancestors or X-Frame-Options."),
    ("referrer-policy", "low", "Referrer-Policy missing", "Set strict-origin-when-cross-origin."),
    ("permissions-policy", "low", "Permissions-Policy missing", "Disable unused browser features."),
    ("cross-origin-opener-policy", "info", "COOP missing", "Consider same-origin."),
    ("cross-origin-resource-policy", "info", "CORP missing", "Consider same-site."),
]

PATHS = [
    ("/.git/HEAD", "high", "medium", "Git metadata is reachable", "Block .git or deploy without it."),
    ("/.env", "critical", "medium", "Environment file is reachable", "Block .env at the web server and rotate values."),
    ("/.env.local", "high", "medium", ".env.local is reachable", "Block it and rotate values."),
    ("/.env.production", "high", "medium", ".env.production is reachable", "Block it and rotate values."),
    ("/.svn/entries", "medium", "medium", "Subversion metadata is reachable", "Block .svn."),
    ("/.hg/requires", "medium", "medium", "Mercurial metadata is reachable", "Block .hg."),
    ("/backup.zip", "medium", "medium", "Backup archive is reachable", "Move backups out of the web root."),
    ("/backup.tar.gz", "medium", "medium", "Backup archive is reachable", "Move backups out of the web root."),
    ("/db.sql", "high", "medium", "Database dump is reachable", "Move dumps out of the web root."),
    ("/dump.sql", "high", "medium", "Database dump is reachable", "Move dumps out of the web root."),
    ("/server-status", "low", "high", "Apache server-status is public", "Restrict it to localhost."),
    ("/server-info", "low", "high", "Apache server-info is public", "Restrict it to localhost."),
    ("/phpinfo.php", "medium", "high", "phpinfo output is public", "Remove it after setup."),
    ("/info.php", "medium", "high", "phpinfo output is public", "Remove it after setup."),
    ("/.DS_Store", "low", "high", "macOS .DS_Store is public", "Block dotfiles."),
    ("/composer.json", "low", "medium", "Composer manifest is public", "Confirm it is intended."),
    ("/package.json", "low", "medium", "npm manifest is public", "Confirm it is intended."),
    ("/actuator", "medium", "medium", "Spring Actuator root is public", "Restrict actuator endpoints."),
    ("/actuator/env", "high", "medium", "Spring Actuator env is public", "Restrict or sanitize it."),
    ("/actuator/heapdump", "high", "low", "Spring heapdump may be public", "Restrict it; it can contain secrets."),
    ("/openapi.json", "info", "medium", "OpenAPI document is public", "Confirm the audience."),
    ("/swagger-ui/", "info", "medium", "Swagger UI is public", "Confirm the audience."),
    ("/swagger-ui.html", "info", "medium", "Swagger UI is public", "Confirm the audience."),
    ("/api-docs", "info", "medium", "API docs are public", "Confirm the audience."),
    ("/graphql", "info", "medium", "GraphQL endpoint responds", "Review auth and query limits."),
    ("/phpmyadmin/", "medium", "medium", "phpMyAdmin is public", "Restrict by IP or add MFA."),
    ("/adminer.php", "medium", "medium", "Adminer is public", "Restrict by IP."),
    ("/wp-admin/", "info", "medium", "WordPress admin is public", "Restrict by IP or add MFA."),
    ("/wp-login.php", "info", "medium", "WordPress login is public", "Add rate limiting and MFA."),
    ("/administrator/", "info", "medium", "Joomla administrator is public", "Restrict by IP or add MFA."),
    ("/user/login", "info", "medium", "Drupal login is public", "Add rate limiting and MFA."),
    ("/.well-known/security.txt", "info", "high", "security.txt exists", "Good sign. Keep the contact current."),
    ("/robots.txt", "info", "high", "robots.txt exists", "Check for sensitive paths in Disallow."),
    ("/sitemap.xml", "info", "medium", "Sitemap is public", "Confirm it does not list staging paths."),
]

SQL_ERRORS = [
    (re.compile(r"SQL syntax.*MySQL", re.I), "MySQL"),
    (re.compile(r"Warning.*mysqli?_", re.I), "MySQL"),
    (re.compile(r"PostgreSQL.*ERROR", re.I), "PostgreSQL"),
    (re.compile(r"invalid input syntax for (?:type )?\w+", re.I), "PostgreSQL"),
    (re.compile(r"Microsoft OLE DB Provider for SQL Server", re.I), "MSSQL"),
    (re.compile(r"Unclosed quotation mark after the character string", re.I), "MSSQL"),
    (re.compile(r"ORA-\d{5}", re.I), "Oracle"),
    (re.compile(r"SQLite/JDBCDriver|SQLite\.Exception", re.I), "SQLite"),
    (re.compile(r"System\.Data\.SQLite", re.I), "SQLite"),
]

DEBUG_MARKERS = [
    (re.compile(r"Werkzeug Debugger", re.I), "Werkzeug debugger"),
    (re.compile(r"You're seeing this error because you have .?DEBUG = True", re.I), "Django DEBUG=True"),
    (re.compile(r"<title>.*Traceback.*</title>", re.I), "Framework traceback"),
    (re.compile(r"X-Debug-Token", re.I), "Symfony debug token"),
    (re.compile(r"at [\w.$]+ \(/[\w./-]+:\d+:\d+\)", re.I), "Stack trace with file paths"),
]

SENSITIVE_DISALLOW = re.compile(
    r"(?i)disallow:\s*(/(admin|backup|config|db|\.git|private|internal|staging|dev|api/v\d))"
)

PORTS = [
    (3306, "MySQL", "high"),
    (5432, "PostgreSQL", "high"),
    (27017, "MongoDB", "high"),
    (6379, "Redis", "high"),
    (9200, "Elasticsearch", "high"),
    (11211, "Memcached", "medium"),
    (2375, "Docker API (plaintext)", "critical"),
    (8080, "HTTP alternate", "info"),
]


class BudgetExceeded(Exception):
    pass


class Fetcher:
    """Rate limited, budgeted HTTP client with one retry on 429/503."""

    def __init__(
        self,
        timeout: int = 15,
        insecure: bool = False,
        rate: float = 2.0,
        max_requests: int = 250,
        respect_robots: bool = True,
        extra_headers: dict | None = None,
    ) -> None:
        self.timeout = timeout
        self.insecure = insecure
        self.interval = 1.0 / max(rate, 0.1)
        self.max_requests = max_requests
        self.respect_robots = respect_robots
        self.sent = 0
        self.lock = threading.Lock()
        self.last = 0.0
        self.stopped = False
        self.robots: urllib.robotparser.RobotFileParser | None = None
        self.robots_host = ""
        self.ctx = ssl._create_unverified_context() if insecure else None
        self.backoff_events = 0
        self.extra_headers = extra_headers or {}

    def _wait(self) -> None:
        with self.lock:
            if self.sent >= self.max_requests:
                raise BudgetExceeded
            delta = time.monotonic() - self.last
            if delta < self.interval:
                time.sleep(self.interval - delta)
            self.last = time.monotonic()
            self.sent += 1

    def _robots_allows(self, url: str) -> bool:
        if not self.respect_robots:
            return True
        parsed = urllib.parse.urlsplit(url)
        host = f"{parsed.scheme}://{parsed.netloc}"
        if self.robots is None or host != self.robots_host:
            parser = urllib.robotparser.RobotFileParser()
            parser.set_url(host + "/robots.txt")
            try:
                parser.read()
            except Exception:
                parser = None  # type: ignore[assignment]
            self.robots, self.robots_host = parser, host
        if not self.robots:
            return True
        try:
            return self.robots.can_fetch(UA, url)
        except Exception:
            return True

    def request(self, url: str, method: str = "GET", origin: str = "", max_body: int = 400_000) -> dict:
        if not self._robots_allows(url):
            return {
                "url": url,
                "status": 0,
                "headers": [],
                "body": "",
                "error": "robots.txt disallow",
                "elapsed_ms": 0,
                "request": "",
            }
        attempt = 0
        while True:
            try:
                self._wait()
            except BudgetExceeded:
                self.stopped = True
                raise
            headers = {"User-Agent": UA, "Accept": "*/*", "Accept-Language": "tr,en;q=0.8"}
            headers.update(self.extra_headers)
            if origin:
                headers["Origin"] = origin
            request_line = f"{method} {urllib.parse.urlsplit(url).path or '/'} HTTP/1.1"
            req = urllib.request.Request(url, headers=headers, method=method)
            started = time.monotonic()
            try:
                opener = (
                    urllib.request.build_opener(urllib.request.HTTPSHandler(context=self.ctx))
                    if self.ctx
                    else urllib.request.build_opener()
                )
                with opener.open(req, timeout=self.timeout) as resp:
                    body = resp.read(max_body)
                    return {
                        "url": resp.geturl(),
                        "status": resp.status,
                        "headers": list(resp.headers.items()),
                        "body": body.decode("utf-8", "replace"),
                        "error": "",
                        "elapsed_ms": int((time.monotonic() - started) * 1000),
                        "request": request_line,
                    }
            except urllib.error.HTTPError as exc:
                body = exc.read(120_000)
                retry_after = exc.headers.get("Retry-After", "")
                if exc.code in (429, 503) and attempt < 1:
                    self.backoff_events += 1
                    delay = 2.0
                    try:
                        delay = min(float(retry_after), 10.0) if retry_after else 2.0
                    except ValueError:
                        pass
                    time.sleep(delay)
                    attempt += 1
                    continue
                return {
                    "url": url,
                    "status": exc.code,
                    "headers": list(exc.headers.items()),
                    "body": body.decode("utf-8", "replace"),
                    "error": f"HTTP {exc.code}",
                    "elapsed_ms": int((time.monotonic() - started) * 1000),
                    "request": request_line,
                }
            except Exception as exc:
                return {
                    "url": url,
                    "status": 0,
                    "headers": [],
                    "body": "",
                    "error": f"{type(exc).__name__}: {exc}",
                    "elapsed_ms": int((time.monotonic() - started) * 1000),
                    "request": request_line,
                }


def header_map(res: dict) -> dict:
    out = {}
    for key, value in res.get("headers", []):
        out.setdefault(key.lower(), []).append(value)
    return out


def first(headers: dict, name: str) -> str:
    return (headers.get(name) or [""])[0]


def excerpt(body: str, needle: str = "", size: int = 240) -> str:
    clean = re.sub(r"\s+", " ", body)
    if needle:
        idx = clean.lower().find(needle.lower())
        if idx > -1:
            clean = clean[max(0, idx - 80) : idx + size]
    return clean[:size]


def sha(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8", "replace")).hexdigest()[:16]


def check_headers(res: dict, url: str) -> list[Finding]:
    headers = header_map(res)
    out: list[Finding] = []
    for name, severity, title, fix in SECURITY_HEADERS:
        if name in headers:
            continue
        if name == "strict-transport-security" and not url.startswith("https://"):
            continue
        out.append(
            Finding(
                check=f"web.header.{name}",
                title=title,
                severity=severity,
                confidence="high",
                evidence=f"{url}: header missing",
                impact="Browser defence is weak, so the impact of the same bug class grows.",
                fix=fix,
                subject=url,
                cwe=["CWE-693"],
                tags=["header"],
                source="passive",
                request=res.get("request", ""),
                response=f"HTTP {res.get('status')}",
            ),
        )
    hsts = first(headers, "strict-transport-security")
    match = re.search(r"max-age=(\d+)", hsts or "")
    if hsts and match and int(match.group(1)) < 15_552_000:
        out.append(
            Finding(
                check="web.header.hsts-short",
                title="HSTS max-age is short",
                severity="low",
                confidence="high",
                evidence=f"{url}: {hsts}",
                impact="HSTS expires early and opens a downgrade window.",
                fix="Use max-age 31536000 and includeSubDomains when ready.",
                subject=url,
                source="passive",
            )
        )
    csp = first(headers, "content-security-policy")
    if csp:
        issues = []
        if "'unsafe-inline'" in csp:
            issues.append("unsafe-inline")
        if "'unsafe-eval'" in csp:
            issues.append("unsafe-eval")
        if re.search(r"(?:script-src|default-src)[^;]*\*", csp):
            issues.append("wildcard source")
        if issues:
            out.append(
                Finding(
                    check="web.header.csp-weak",
                    title="CSP present but weak",
                    severity="medium",
                    confidence="high",
                    evidence=f"{url}: CSP contains {', '.join(issues)}",
                    impact="CSP can be bypassed. A malicious inline script can run.",
                    fix="Use a nonce or hash based CSP, drop unsafe-eval and narrow wildcards.",
                    subject=url,
                    cwe=["CWE-1021"],
                    source="passive",
                    false_positive="Some old frameworks need inline script. Migrate to nonces.",
                )
            )
    if "server" in headers:
        out.append(
            Finding(
                check="web.header.server",
                title="Server version exposed",
                severity="info",
                confidence="high",
                evidence=f"{url}: {first(headers, 'server')}",
                impact="Makes version specific matching easier.",
                fix="Shorten the banner or hide the version.",
                subject=url,
                source="passive",
            )
        )
    if "x-powered-by" in headers:
        out.append(
            Finding(
                check="web.header.powered-by",
                title="X-Powered-By exposed",
                severity="info",
                confidence="high",
                evidence=f"{url}: {first(headers, 'x-powered-by')}",
                impact="Technology fingerprint.",
                fix="Turn it off in production.",
                subject=url,
                source="passive",
            )
        )
    if "x-aspnet-version" in headers or "x-aspnetmvc-version" in headers:
        out.append(
            Finding(
                check="web.header.aspnet",
                title="ASP.NET version exposed",
                severity="low",
                confidence="high",
                evidence=f"{url}: aspnet version header",
                impact="Version specific matching.",
                fix="Disable version headers.",
                subject=url,
                source="passive",
            )
        )
    return out


def check_cors(res: dict, url: str, origin: str) -> list[Finding]:
    headers = header_map(res)
    allow = first(headers, "access-control-allow-origin")
    creds = first(headers, "access-control-allow-credentials").lower() == "true"
    out = []
    if allow == "*" and creds:
        out.append(
            Finding(
                check="web.cors.wildcard-credentials",
                title="CORS open to all with credentials",
                severity="medium",
                confidence="high",
                evidence=f"{url}: ACAO * + ACAC true",
                impact="Credentialed CORS with a wildcard works poorly across browsers. A wrong setup exposes session data.",
                fix="Reflect the origin from an allowlist. Do not combine ACAO * with credentials.",
                subject=url,
                cwe=["CWE-942"],
                source="passive",
                false_positive="Behavior differs by browser version.",
            )
        )
    elif allow and allow != "*" and origin and allow.rstrip("/") == origin.rstrip("/"):
        out.append(
            Finding(
                check="web.cors.reflect",
                title="CORS reflects the request origin",
                severity="low",
                confidence="medium",
                evidence=f"{url}: ACAO {allow}",
                impact="Without an allowlist any origin can read.",
                fix="Compare Origin to an allowlist. Reflect known hosts only.",
                subject=url,
                cwe=["CWE-942"],
                source="passive",
            )
        )
    if allow == "null":
        out.append(
            Finding(
                check="web.cors.null",
                title="CORS accepts a null origin",
                severity="low",
                confidence="medium",
                evidence=f"{url}: ACAO null",
                impact="Reads from sandboxed iframes and file:// origins get through.",
                fix="Use a real origin list instead of null.",
                subject=url,
                cwe=["CWE-942"],
            )
        )
    return out


def check_cookies(res: dict, url: str) -> list[Finding]:
    out = []
    for key, value in res.get("headers", []):
        if key.lower() != "set-cookie":
            continue
        name = value.split("=", 1)[0].strip()
        low = value.lower()
        missing = [flag for flag in ("secure", "httponly", "samesite") if flag not in low]
        if not missing:
            continue
        severity = "medium" if "session" in name.lower() or "sid" in name.lower() else "low"
        out.append(
            Finding(
                check="web.cookie.flags",
                title=f"Cookie flags missing: {name}",
                severity=severity,
                confidence="high",
                evidence=f"{url}: {name} missing: {', '.join(missing)}",
                impact="The cookie can be read over the network or by JS, and a CSRF window opens.",
                fix="Add Secure, HttpOnly and SameSite=Lax or Strict. A session cookie needs all three.",
                subject=f"{url}#{name}",
                cwe=["CWE-614"],
                source="passive",
            )
        )
    return out


def analyze_html(url: str, body: str, headers: dict) -> list[Finding]:
    out: list[Finding] = []
    low = body.lower()
    tech = []
    for name, needle in (
        ("WordPress", "/wp-content/"),
        ("WordPress", "/wp-includes/"),
        ("Drupal", "drupal"),
        ("Joomla", "joomla"),
        ("Next.js", "__next_data__"),
        ("React", "react"),
        ("Vue", "vue"),
        ("Angular", "ng-version"),
        ("Shopify", "cdn.shopify"),
        ("Laravel", "laravel"),
        ("Django", "csrfmiddlewaretoken"),
    ):
        if needle in low:
            tech.append(name)
    tech = sorted(set(tech))
    if tech:
        out.append(
            Finding(
                check="web.fingerprint",
                title="Technology hints",
                severity="info",
                confidence="medium",
                evidence=f"{url}: {', '.join(tech)}",
                impact="Makes component and version matching easier.",
                fix="Keep versions current and trim banner and generator tags.",
                subject=url,
                tags=["fingerprint"],
            )
        )
    match = re.search(r'<meta[^>]+name=["\']generator["\'][^>]+content=["\']([^"\']+)', body, re.I)
    if match:
        out.append(
            Finding(
                check="web.generator",
                title="Generator version exposed",
                severity="low",
                confidence="high",
                evidence=f"{url}: {match.group(1)[:120]}",
                impact="The CMS version is readable.",
                fix="Remove the generator tag or hide the version.",
                subject=url,
                tags=["fingerprint"],
            )
        )
        out += cms_version_hint(url, match.group(1))
    if url.startswith("http://") and re.search(r"<input[^>]+type=[\"']?password", low):
        out.append(
            Finding(
                check="web.http-password",
                title="Password form over HTTP",
                severity="medium",
                confidence="high",
                evidence=f"{url}: password input",
                impact="Session data travels in clear text.",
                fix="Move to HTTPS and redirect HTTP permanently.",
                subject=url,
                cwe=["CWE-319"],
            )
        )
    for pattern, _name in SQL_ERRORS:
        if pattern.search(body):
            out.append(
                Finding(
                    check="web.sql-error",
                    title="Database error signature in the page",
                    severity="low",
                    confidence="medium",
                    evidence=f"{url}: {excerpt(body, pattern.search(body).group(0))}",
                    impact="The error leaks schema and engine detail and hints at injection.",
                    fix="Simplify error pages and disable detail in production.",
                    subject=url,
                    cwe=["CWE-209"],
                    false_positive="The page may only appear when triggered.",
                )
            )
            break
    for pattern, name in DEBUG_MARKERS:
        if pattern.search(body):
            out.append(
                Finding(
                    check="web.debug",
                    title=f"Debug trace: {name}",
                    severity="medium",
                    confidence="medium",
                    evidence=f"{url}: {excerpt(body, pattern.search(body).group(0))}",
                    impact="Leaks paths, versions and variable values.",
                    fix="Disable debug in production.",
                    subject=url,
                    cwe=["CWE-215"],
                )
            )
            break
    if re.search(r"<title>\s*Index of /", body, re.I):
        out.append(
            Finding(
                check="web.listing",
                title="Directory listing enabled",
                severity="low",
                confidence="high",
                evidence=f"{url}: Index of",
                impact="File inventory and backup discovery get easier.",
                fix="Disable autoindex or keep it only where needed.",
                subject=url,
                cwe=["CWE-548"],
            )
        )
    for match in re.finditer(r'<script[^>]+src=["\']([^"\']+\.js[^"\']*)', body, re.I):
        if src := match.group(1):
            out.append(
                Finding(
                    check="web.js-asset",
                    title="JavaScript asset",
                    severity="info",
                    confidence="high",
                    evidence=f"{url}: {src[:160]}",
                    impact="Worth review for source maps and client secrets.",
                    fix="Disable source maps in production or restrict access.",
                    subject=src,
                    tags=["asset"],
                )
            )
            break
    if 'name="robots"' in low and "noindex" in low:
        out.append(
            Finding(
                check="web.noindex",
                title="Page is noindex",
                severity="info",
                confidence="high",
                evidence=url,
                impact="Search engines skip it, so it stays out of inventories.",
                fix="Check whether that is intended.",
                subject=url,
            )
        )
    return out


def cms_version_hint(url: str, generator: str) -> list[Finding]:
    try:
        with open(os.path.join(paths.DATA, "cms_vulns.json"), encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return []
    version = re.search(r"(\d+\.\d+(?:\.\d+)?)", generator)
    if not version:
        return []
    found = version.group(1)
    out = []
    for item in data.get("wordpress", {}).get("known", []):
        below = item.get("below", "0")
        if _version_lt(found, below):
            out.append(
                Finding(
                    check="web.cms-outdated",
                    title=f"Component version falls in a known fix range: {found} < {below}",
                    severity=item.get("severity", "medium"),
                    confidence="low",
                    evidence=f"{url}: generator {generator[:80]}",
                    impact=item.get("title", "Known fix range."),
                    fix=f"Move the version to {below} or later and check plugins separately.",
                    subject=url,
                    tags=["cms", item.get("cve", "")],
                    cwe=["CWE-1104"],
                    false_positive="The range is rough. The real version behind a deployment can differ.",
                )
            )
    return out


def _version_lt(a: str, b: str) -> bool:
    try:
        pa = tuple(int(x) for x in a.split("."))
        pb = tuple(int(x) for x in b.split("."))
        return pa < pb
    except ValueError:
        return False


def probe_paths(base: str, fetcher: Fetcher, soft404: tuple[int, str], origin: str) -> list[Finding]:
    out: list[Finding] = []

    def one(item: tuple[str, str, str, str, str]) -> Finding | None:
        path, severity, confidence, title, advice = item
        if base.rstrip("/").endswith(path.rstrip("/")):
            return None
        url = urllib.parse.urljoin(base.rstrip("/") + "/", path.lstrip("/"))
        try:
            res = fetcher.request(url, origin=origin, max_body=120_000)
        except BudgetExceeded:
            return None
        status = res.get("status", 0)
        body = res.get("body", "")
        if status not in (200, 401, 403) or not body.strip():
            return None
        if _marker_ok(path, body):
            if status == 200 and _looks_like_soft404(body, soft404) and not _strong_marker(path, body):
                return None
            slug = re.sub(r"[^a-z0-9]+", "-", path.strip("/").lower()).strip("-")
            return Finding(
                check="web.path." + slug,
                title=f"{title}: {path}",
                severity=severity,
                confidence=confidence,
                evidence=f"GET {url} -> HTTP {status}, {len(body)} bytes, hash {sha(body)}",
                impact=advice,
                fix=_path_fix(path),
                subject=url,
                request=res.get("request", ""),
                response=excerpt(body, size=200),
                false_positive="Can be a soft 404. Check the soft 404 baseline.",
                cwe=["CWE-538"],
                tags=["exposure"],
            )
        if status == 200 and severity not in ("info",) and _looks_like_soft404(body, soft404):
            return None
        return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for finding in pool.map(one, PATHS):
            if finding:
                out.append(finding)
    return out


def _strong_marker(path: str, body: str) -> bool:
    """A marker that a friendly 404 page rarely satisfies."""
    if path.startswith("/.env"):
        lines = [ln for ln in body.splitlines() if re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", ln)]
        return len(lines) >= 2 and "<html" not in body[:200].lower()
    if path == "/.git/HEAD":
        return body.startswith("ref:") or bool(re.match(r"^[0-9a-f]{40}\s*$", body.strip()))
    if path.endswith((".json", "/graphql", "/actuator", "/actuator/env", "/api-docs")):
        return body.lstrip()[:1] in ("{", "[")
    if path.startswith("/."):
        return "<html" not in body[:200].lower()
    return True


def _marker_ok(path: str, body: str) -> bool:
    checks = {
        "/.git/HEAD": lambda s: s.startswith("ref:") or bool(re.match(r"^[0-9a-f]{40}\s*$", s.strip())),
        "/.env": lambda s: "=" in s and not s.lstrip().startswith("<"),
        "/.env.local": lambda s: "=" in s and not s.lstrip().startswith("<"),
        "/.env.production": lambda s: "=" in s and not s.lstrip().startswith("<"),
        "/.svn/entries": lambda s: s.strip()[:1].isdigit() or "dir" in s[:40],
        "/.hg/requires": lambda s: "revlog" in s or "store" in s,
        "/backup.zip": lambda s: s[:2] in ("PK", "\x1f\x8b") or "PK" in s[:4],
        "/backup.tar.gz": lambda s: s[:2] in ("PK", "\x1f\x8b") or "ustar" in s[:300],
        "/db.sql": lambda s: "CREATE TABLE" in s.upper() or "INSERT INTO" in s.upper(),
        "/dump.sql": lambda s: "CREATE TABLE" in s.upper() or "INSERT INTO" in s.upper(),
        "/server-status": lambda s: "Apache Server Status" in s,
        "/server-info": lambda s: "Apache Server Information" in s,
        "/phpinfo.php": lambda s: "PHP Version" in s or "phpinfo()" in s,
        "/info.php": lambda s: "PHP Version" in s or "phpinfo()" in s,
        "/.DS_Store": lambda s: "Bud1" in s or "\x00\x00\x00\x01Bud1" in s,
        "/composer.json": lambda s: '"require"' in s or '"name"' in s,
        "/package.json": lambda s: '"dependencies"' in s or '"name"' in s,
        "/actuator": lambda s: "_links" in s or "self" in s,
        "/actuator/env": lambda s: "propertySources" in s or "activeProfiles" in s,
        "/actuator/heapdump": lambda s: "\x00" in s or "JAVA PROFILE" in s,
        "/openapi.json": lambda s: '"openapi"' in s or '"swagger"' in s or '"paths"' in s,
        "/swagger-ui/": lambda s: "swagger" in s.lower(),
        "/swagger-ui.html": lambda s: "swagger" in s.lower(),
        "/api-docs": lambda s: '"openapi"' in s or '"swagger"' in s or '"paths"' in s,
        "/graphql": lambda s: "graphql" in s.lower() or '"data"' in s or '"errors"' in s,
        "/phpmyadmin/": lambda s: "phpMyAdmin" in s or "pma" in s.lower(),
        "/adminer.php": lambda s: "adminer" in s.lower(),
        "/wp-admin/": lambda s: "wp-admin" in s or "wordpress" in s.lower() or "log in" in s.lower(),
        "/wp-login.php": lambda s: "wp-login" in s or "wordpress" in s.lower(),
        "/administrator/": lambda s: "joomla" in s.lower() or "administrator" in s.lower(),
        "/user/login": lambda s: "drupal" in s.lower() or "log in" in s.lower(),
        "/.well-known/security.txt": lambda s: "Contact:" in s,
        "/robots.txt": lambda s: "user-agent" in s.lower() or "disallow" in s.lower(),
        "/sitemap.xml": lambda s: "<urlset" in s or "<sitemapindex" in s,
    }
    return checks.get(path, lambda s: bool(s.strip()))(body)


def _path_fix(path: str) -> str:
    if path.startswith(("/.git", "/.svn", "/.hg")):
        return "Move the metadata directory out of the web root or block it."
    if path.startswith("/.") or path in ("/backup.zip", "/backup.tar.gz", "/db.sql", "/dump.sql"):
        return "Move the file outside the web root and allowlist it."
    if "admin" in path or "phpmyadmin" in path or "adminer" in path:
        return "Put the admin panel behind an IP allowlist or MFA."
    return "Check whether the exposure is intended. Otherwise remove it or add authentication."


def _looks_like_soft404(body: str, soft404: tuple[int, str]) -> bool:
    size, digest = soft404
    if not size:
        return False
    if sha(body) == digest:
        return True
    return abs(len(body) - size) < max(40, size // 20)


def check_robots_disclosure(body: str, url: str) -> list[Finding]:
    hits = sorted({m.group(1).rstrip("/") for m in SENSITIVE_DISALLOW.finditer(body)})
    if not hits:
        return []
    return [
        Finding(
            check="web.robots.disclosure",
            title="robots.txt lists sensitive paths",
            severity="low",
            confidence="high",
            evidence=f"{url}: {', '.join(hits[:6])}",
            impact="Admin and backup paths show without discovery.",
            fix="Protect those paths with IP limits or auth. robots.txt is not a security boundary.",
            subject=url,
            cwe=["CWE-538"],
            tags=["disclosure"],
        )
    ]


def tls_info(url: str, timeout: int = 12) -> dict:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https":
        return {"enabled": False, "reason": "not https"}
    host, port = parsed.hostname, parsed.port or 443
    try:
        ctx = ssl.create_default_context()
        with (
            socket.create_connection((host, port), timeout=timeout) as sock,
            ctx.wrap_socket(sock, server_hostname=host) as tls,
        ):
            cert = tls.getpeercert() or {}
            not_after = cert.get("notAfter", "")
            days = None
            if not_after:
                expiry = dt.datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z").replace(tzinfo=dt.timezone.utc)
                days = (expiry - dt.datetime.now(dt.timezone.utc)).days
            return {
                "enabled": True,
                "version": tls.version(),
                "issuer": {item[0][0]: item[0][1] for item in cert.get("issuer", [])},
                "subject": {item[0][0]: item[0][1] for item in cert.get("subject", [])},
                "not_after": not_after,
                "days_left": days,
                "san": [x[1] for x in cert.get("subjectAltName", [])][:20],
            }
    except Exception as exc:
        return {"enabled": False, "error": f"{type(exc).__name__}: {exc}"}


def check_tls(tls: dict, url: str) -> list[Finding]:
    out = []
    if not tls.get("enabled"):
        if tls.get("error"):
            out.append(
                Finding(
                    check="web.tls.connect",
                    title="TLS connection failed",
                    severity="medium",
                    confidence="high",
                    evidence=f"{url}: {tls['error']}",
                    impact="The certificate cannot be verified or the service does not serve TLS.",
                    fix="Fix the certificate chain and SNI configuration.",
                    subject=url,
                    cwe=["CWE-295"],
                )
            )
        return out
    if tls.get("days_left") is not None and tls["days_left"] < 21:
        severity = "high" if tls["days_left"] < 7 else "medium"
        out.append(
            Finding(
                check="web.tls.expiry",
                title="TLS certificate is expiring",
                severity=severity,
                confidence="high",
                evidence=f"{url}: {tls['days_left']} days left, {tls.get('not_after')}",
                impact="Expiry brings browser warnings and an outage.",
                fix="Renew it and automate renewal.",
                subject=url,
                cwe=["CWE-298"],
            )
        )
    if tls.get("version") in ("TLSv1", "TLSv1.1"):
        out.append(
            Finding(
                check="web.tls.version",
                title="Old TLS version",
                severity="low",
                confidence="high",
                evidence=f"{url}: {tls.get('version')}",
                impact="Old protocols offer weak ciphers.",
                fix="Require TLS 1.2 and 1.3.",
                subject=url,
                cwe=["CWE-326"],
            )
        )
    return out


def dns_txt(name: str) -> list[str]:
    if shutil.which("dig"):
        out = subprocess.run(["dig", "+short", "TXT", name], capture_output=True, text=True, timeout=8).stdout
    elif shutil.which("nslookup"):
        out = subprocess.run(["nslookup", "-type=TXT", name], capture_output=True, text=True, timeout=8).stdout
    else:
        return []
    return [m.group(1) for m in re.finditer(r'"([^"]+)"', out)]


def check_email(host: str) -> list[Finding]:
    out: list[Finding] = []
    if not host or re.match(r"^[\d.]+$", host):
        return out
    try:
        spf = [r for r in dns_txt(host) if r.lower().startswith("v=spf1")]
    except Exception:
        spf = []
    if not spf:
        out.append(
            Finding(
                check="email.spf",
                title="No SPF record",
                severity="medium",
                confidence="high",
                evidence=f"TXT {host}: no v=spf1",
                impact="Forged mail can use your domain.",
                fix="Publish an SPF record with legitimate senders only and end it with -all.",
                subject=host,
                cwe=["CWE-290"],
                tags=["email"],
            )
        )
    else:
        record = spf[0]
        if record.strip().endswith("?all"):
            out.append(
                Finding(
                    check="email.spf-weak",
                    title="SPF ends with ?all",
                    severity="medium",
                    confidence="high",
                    evidence=f"TXT {host}: {record[:160]}",
                    impact="The policy is not enforced and receivers stay undecided.",
                    fix="Use -all.",
                    subject=host,
                    cwe=["CWE-290"],
                )
            )
        elif record.strip().endswith("~all"):
            out.append(
                Finding(
                    check="email.spf-soft",
                    title="SPF soft fail",
                    severity="low",
                    confidence="high",
                    evidence=f"TXT {host}: {record[:160]}",
                    impact="Forged mail is marked, not rejected.",
                    fix="Use -all after the migration.",
                    subject=host,
                    cwe=["CWE-290"],
                )
            )
        if "include:" in record and len(record) > 400:
            out.append(
                Finding(
                    check="email.spf-long",
                    title="SPF record is long",
                    severity="low",
                    confidence="medium",
                    evidence=f"TXT {host}: {len(record)} karakter",
                    impact="The DNS lookup limit can be exceeded and SPF stops working.",
                    fix="Simplify the include chain.",
                    subject=host,
                    cwe=["CWE-290"],
                )
            )
    try:
        dmarc = [r for r in dns_txt("_dmarc." + host) if "v=dmarc1" in r.lower()]
    except Exception:
        dmarc = []
    if not dmarc:
        out.append(
            Finding(
                check="email.dmarc",
                title="No DMARC record",
                severity="medium",
                confidence="high",
                evidence=f"TXT _dmarc.{host}: missing",
                impact="The SPF and DKIM result is not enforced by policy.",
                fix="Start with v=DMARC1; p=quarantine; rua=... then move to p=reject.",
                subject=host,
                cwe=["CWE-290"],
                tags=["email"],
            )
        )
    else:
        policy = re.search(r"p=(\w+)", dmarc[0], re.I)
        if policy and policy.group(1).lower() == "none":
            out.append(
                Finding(
                    check="email.dmarc-none",
                    title="DMARC p=none",
                    severity="low",
                    confidence="high",
                    evidence=f"TXT _dmarc.{host}: {dmarc[0][:160]}",
                    impact="The policy only reports, it does not stop spoofing.",
                    fix="After watching reports, move to p=quarantine and p=reject.",
                    subject=host,
                    cwe=["CWE-290"],
                )
            )
    selectors = ("default", "google", "selector1", "selector2", "k1", "s1", "mail", "dkim")
    dkim = []
    for selector in selectors:
        try:
            if dns_txt(f"{selector}._domainkey.{host}"):
                dkim.append(selector)
        except Exception:
            pass
    if not dkim:
        out.append(
            Finding(
                check="email.dkim",
                title="No record on common DKIM selectors",
                severity="low",
                confidence="low",
                evidence=f"{host}: {', '.join(selectors)}",
                impact="DKIM validation is weak, which risks DMARC alignment.",
                fix="Enable DKIM signing and publish the selector.",
                subject=host,
                cwe=["CWE-290"],
                false_positive="A custom selector name stays invisible here.",
            )
        )
    return out


def check_ports(host: str, timeout: float = 2.0) -> list[Finding]:
    out: list[Finding] = []
    if not host or not re.match(r"^[\w.-]+$", host):
        return out

    def one(item: tuple[int, str, str]) -> Finding | None:
        port, name, severity = item
        try:
            with socket.create_connection((host, port), timeout=timeout) as sock:
                banner = ""
                try:
                    sock.settimeout(1.0)
                    banner = sock.recv(256).decode("utf-8", "replace").strip()
                except Exception:
                    pass
                return Finding(
                    check=f"net.port.{port}",
                    title=f"Open port: {port} ({name})",
                    severity=severity,
                    confidence="high",
                    evidence=f"{host}:{port} TCP open" + (f", banner {banner[:80]!r}" if banner else ""),
                    impact="The service is reachable from outside, so auth and updates matter.",
                    fix="Put the admin interface behind an IP allowlist, and require TLS and a strong password.",
                    subject=f"{host}:{port}",
                    cwe=["CWE-284"],
                    tags=["network"],
                    false_positive="An open port does not prove the service is unprotected.",
                )
        except OSError:
            return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for finding in pool.map(one, PORTS):
            if finding:
                out.append(finding)
    return out


def check_redirect_https(url: str, fetcher: Fetcher) -> list[Finding]:
    if not url.startswith("http://"):
        return []
    try:
        res = fetcher.request(url, max_body=10_000)
    except BudgetExceeded:
        return []
    location = first(header_map(res), "location")
    if res.get("status") in (301, 302, 307, 308) and location.startswith("https://"):
        return [
            Finding(
                check="web.https-redirect",
                title="HTTP redirects to HTTPS",
                severity="info",
                confidence="high",
                evidence=f"GET {url} -> {res.get('status')} {location}",
                impact="Good configuration.",
                fix="Keep it and add HSTS.",
                subject=url,
            )
        ]
    if res.get("status") == 200:
        return [
            Finding(
                check="web.https-missing",
                title="HTTP answers and does not force HTTPS",
                severity="medium",
                confidence="high",
                evidence=f"GET {url} -> HTTP 200",
                impact="An active attacker can change the content.",
                fix="Add a permanent redirect and HSTS.",
                subject=url,
                cwe=["CWE-319"],
            )
        ]
    return []
