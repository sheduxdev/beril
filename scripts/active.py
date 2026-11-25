#!/usr/bin/env python3
"""Minimal, non-destructive active probes.

Only runs after an ownership record exists. One parameter at a time, GET only,
small payloads, one baseline per URL. No writes, no fuzzing, no brute force.

Probe set:

- a single quote for error based SQL injection;
- a unique marker for reflected XSS;
- a protocol relative URL for open redirect;
- a traversal string for file read;
- arithmetic template expressions for SSTI;
- an expanded shell marker for command injection;
- OPTIONS/TRACE method behavior.

Each result is a lead with a request pair. A reflected marker is not an XSS
proof until you show execution context; the finding says so. The SSTI and
command probes prove evaluation, not full exploitation.
"""

from __future__ import annotations

import re
import urllib.parse

from beril_model import Finding
from web_checks import BudgetExceeded, Fetcher, excerpt, first, header_map

MAX_URLS = 8
MAX_PARAMS = 3
MARKER = "beril9f7z"
REDIRECT_PARAMS = {
    "url",
    "uri",
    "redirect",
    "redirect_uri",
    "next",
    "return",
    "returnurl",
    "callback",
    "continue",
    "target",
    "dest",
    "destination",
    "goto",
    "out",
}
FILE_PARAMS = {
    "file",
    "filename",
    "path",
    "page",
    "template",
    "view",
    "include",
    "doc",
    "document",
    "download",
    "dir",
    "folder",
    "src",
    "resource",
}
SQL_RE = re.compile(
    r"(SQL syntax|SQL error|mysqli?_|PostgreSQL.*ERROR|ORA-\d{5}|SQLite|sqlite3\.|"
    r"Unclosed quotation mark|ODBC SQL Server|syntax error at or near|"
    r"near \"[^\"]+\": syntax error|no such column|unrecognized token)",
    re.I,
)
SSTI_PAYLOADS = ("{{7*7}}", "${7*7}", "<%= 7*7 %>")
CMDI_PAYLOAD = ";echo beril$((6*7))"
CMDI_MARKER = "beril42"


def targets_from_page(base: str, body: str) -> list[tuple[str, dict]]:
    """Collect same-host URLs with query parameters from the landing page."""
    found: dict[str, dict] = {}
    for match in re.finditer(r"""(?:href|action)=["']([^"'#]+)""", body, re.I):
        raw = match.group(1).replace("&amp;", "&")
        url = urllib.parse.urljoin(base, raw)
        parts = urllib.parse.urlsplit(url)
        if parts.hostname != urllib.parse.urlsplit(base).hostname:
            continue
        params = dict(urllib.parse.parse_qsl(parts.query, keep_blank_values=True))
        if params and url not in found:
            found[url] = params
    if not found:
        parts = urllib.parse.urlsplit(base)
        if parts.query:
            found[base] = dict(urllib.parse.parse_qsl(parts.query, keep_blank_values=True))
    return list(found.items())[:MAX_URLS]


def _with_param(url: str, name: str, value: str) -> str:
    parts = urllib.parse.urlsplit(url)
    params = dict(urllib.parse.parse_qsl(parts.query, keep_blank_values=True))
    params[name] = value
    return urllib.parse.urlunsplit(parts._replace(query=urllib.parse.urlencode(params)))


def _diff(baseline: str, mutated: str) -> float:
    if not baseline and not mutated:
        return 0.0
    a, b = len(baseline), len(mutated)
    if max(a, b) == 0:
        return 0.0
    return abs(a - b) / max(a, b)


def run(base: str, body: str, fetcher: Fetcher, origin: str = "") -> list[Finding]:
    out: list[Finding] = []
    for url, params in targets_from_page(base, body):
        try:
            baseline = fetcher.request(url, origin=origin, max_body=200_000)
        except BudgetExceeded:
            fetcher.stopped = True
            break
        if baseline.get("status") in (0, 429, 503) or fetcher.stopped:
            continue
        base_body = baseline.get("body", "")
        base_status = baseline.get("status", 0)
        names = [n for n in params if len(n) <= 40][:MAX_PARAMS]
        for name in names:
            if fetcher.stopped:
                break
            lowered = name.lower()
            out += _sqli(url, name, baseline, fetcher, origin, base_body, base_status)
            out += _xss(url, name, baseline, fetcher, origin, base_body)
            out += _ssti(url, name, fetcher, origin, base_body)
            out += _cmdi(url, name, fetcher, origin, base_body)
            if lowered in REDIRECT_PARAMS:
                out += _redirect(url, name, fetcher, origin, base_body, base_status)
            if lowered in FILE_PARAMS:
                out += _traversal(url, name, fetcher, origin, base_body)
    out += _methods(base, fetcher, origin)
    return out


def _sqli(
    url: str, name: str, baseline: dict, fetcher: Fetcher, origin: str, base_body: str, base_status: int
) -> list[Finding]:
    mutated_url = _with_param(
        url, name, (dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(url).query)).get(name, "") + "'")
    )
    try:
        res = fetcher.request(mutated_url, origin=origin, max_body=200_000)
    except BudgetExceeded:
        return []
    body = res.get("body", "")
    match = SQL_RE.search(body)
    status = res.get("status", 0)
    evidence = f"GET {mutated_url} -> HTTP {status}, {len(body)} bytes (baseline {base_status}, {len(base_body)} bytes)"
    if match:
        return [
            Finding(
                check="active.sqli.error",
                title=f"SQL error signature: {name}",
                severity="medium",
                confidence="medium",
                evidence=evidence + f"; signature: {excerpt(body, match.group(0), 140)}",
                impact="The parameter may reach the query. Error based injection candidate.",
                fix="Move to parameterised queries and hide error detail. Then confirm with a boolean pair and a timing check.",
                subject=url,
                source="active",
                cwe=["CWE-89"],
                tags=["sqli"],
                request=res.get("request", ""),
                response=excerpt(body, match.group(0), 300),
                false_positive="The quote can break another layer. The signature matters, a diff alone is not enough.",
            )
        ]
    if status >= 500 and base_status < 500:
        return [
            Finding(
                check="active.sqli.error500",
                title=f"Quote caused a 500: {name}",
                severity="low",
                confidence="low",
                evidence=evidence,
                impact="Input is processed and error handling may be weak.",
                fix="Read the error body and use parameterised queries.",
                subject=url,
                source="active",
                cwe=["CWE-89"],
                tags=["sqli"],
                false_positive="A 500 can come from another validation error.",
            )
        ]
    if _diff(base_body, body) > 0.25 and base_status == status == 200:
        return [
            Finding(
                check="active.sqli.diff",
                title=f"Quote changed the response size: {name}",
                severity="low",
                confidence="low",
                evidence=evidence,
                impact="Injection candidate. The result set may have changed.",
                fix="Confirm the same parameter with a boolean pair.",
                subject=url,
                source="active",
                cwe=["CWE-89"],
                tags=["sqli"],
                false_positive="Dynamic content such as ads or counters also changes body size.",
            )
        ]
    return []


def _xss(url: str, name: str, baseline: dict, fetcher: Fetcher, origin: str, base_body: str) -> list[Finding]:
    payload = f"<{MARKER}>"
    mutated_url = _with_param(url, name, payload)
    try:
        res = fetcher.request(mutated_url, origin=origin, max_body=200_000)
    except BudgetExceeded:
        return []
    body = res.get("body", "")
    if payload in body:
        return [
            Finding(
                check="active.xss.reflect",
                title=f"Marker reflected without encoding: {name}",
                severity="medium",
                confidence="medium",
                evidence=f"GET {mutated_url} -> marker appears verbatim",
                impact="Reflection in an HTML context. Execution still needs an event handler proof.",
                fix="Encode output for the context and add a CSP nonce.",
                subject=url,
                source="active",
                cwe=["CWE-79"],
                tags=["xss"],
                request=res.get("request", ""),
                response=excerpt(body, MARKER, 300),
                false_positive="Reflection is not XSS on its own. Test attribute, script and URL contexts.",
            )
        ]
    if f"&lt;{MARKER}&gt;" in body or f"&#60;{MARKER}" in body:
        return [
            Finding(
                check="active.xss.encoded",
                title=f"Marker reflected encoded: {name}",
                severity="info",
                confidence="high",
                evidence=f"GET {mutated_url} -> encoded marker",
                impact="Basic HTML escaping works.",
                fix="Keep context aware escaping.",
                subject=url,
                source="active",
                cwe=["CWE-79"],
                tags=["xss"],
            )
        ]
    return []


def _ssti(url: str, name: str, fetcher: Fetcher, origin: str, base_body: str) -> list[Finding]:
    for payload in SSTI_PAYLOADS:
        mutated_url = _with_param(url, name, payload)
        try:
            res = fetcher.request(mutated_url, origin=origin, max_body=120_000)
        except BudgetExceeded:
            return []
        body = res.get("body", "")
        if payload in body or not re.search(r"\b49\b", body) or re.search(r"\b49\b", base_body):
            continue
        return [
            Finding(
                check="active.ssti",
                title=f"Template expression evaluated: {name}",
                severity="medium",
                confidence="medium",
                evidence=f"GET {mutated_url} -> {payload} became 49, literal payload absent",
                impact="The value reaches a template engine. Sandbox escape may reach code execution.",
                fix="Treat input as data, not template source. Use a logic-less template where possible.",
                subject=url,
                source="active",
                cwe=["CWE-1336"],
                tags=["ssti", "rce"],
                request=res.get("request", ""),
                response=excerpt(body, "49", 240),
                false_positive="A page can contain 49 for other reasons. Confirm with a second expression and a version probe.",
            )
        ]
    return []


def _cmdi(url: str, name: str, fetcher: Fetcher, origin: str, base_body: str) -> list[Finding]:
    mutated_url = _with_param(url, name, CMDI_PAYLOAD)
    try:
        res = fetcher.request(mutated_url, origin=origin, max_body=120_000)
    except BudgetExceeded:
        return []
    body = res.get("body", "")
    if CMDI_MARKER not in body or CMDI_PAYLOAD in body or CMDI_MARKER in base_body:
        return []
    return [
        Finding(
            check="active.cmdi",
            title=f"Shell expansion in parameter: {name}",
            severity="high",
            confidence="medium",
            evidence=f"GET {mutated_url} -> arithmetic expansion produced {CMDI_MARKER}",
            impact="The value reaches a shell. A separator and an arbitrary command may execute.",
            fix="Avoid shell=True. Pass an argv list and validate against an allowlist.",
            subject=url,
            source="active",
            cwe=["CWE-78"],
            tags=["cmdi", "rce"],
            request=res.get("request", ""),
            response=excerpt(body, CMDI_MARKER, 240),
            false_positive="The shell syntax can be expanded by another layer. Confirm with a second command and a callback.",
        )
    ]


def _redirect(url: str, name: str, fetcher: Fetcher, origin: str, base_body: str, base_status: int) -> list[Finding]:
    payload = "//beril.example/"
    mutated_url = _with_param(url, name, payload)
    try:
        res = fetcher.request(mutated_url, origin=origin, max_body=60_000)
    except BudgetExceeded:
        return []
    location = first(header_map(res), "location")
    if res.get("status") in (301, 302, 303, 307, 308) and "beril.example" in location:
        return [
            Finding(
                check="active.redirect",
                title=f"Open redirect candidate: {name}",
                severity="medium",
                confidence="high",
                evidence=f"GET {mutated_url} -> {res.get('status')} Location: {location[:160]}",
                impact="Useful for phishing and OAuth token carriage.",
                fix="Validate the redirect target against an allowlist and normalise relative paths.",
                subject=url,
                source="active",
                cwe=["CWE-601"],
                tags=["redirect"],
                request=res.get("request", ""),
                response=f"HTTP {res.get('status')} Location: {location[:200]}",
                false_positive="Path only redirects can still be safe. Check scheme and host.",
            )
        ]
    return []


def _traversal(url: str, name: str, fetcher: Fetcher, origin: str, base_body: str) -> list[Finding]:
    # The app's working depth is unknown, so try shallow first and stop at proof.
    for depth in (4, 6, 8):
        payload = "../" * depth + "etc/passwd"
        mutated_url = _with_param(url, name, payload)
        try:
            res = fetcher.request(mutated_url, origin=origin, max_body=200_000)
        except BudgetExceeded:
            return []
        body = res.get("body", "")
        if "root:x:0:0" in body or "root:*:0:0" in body:
            return [
                Finding(
                    check="active.traversal",
                    title=f"Path traversal file read: {name}",
                    severity="high",
                    confidence="high",
                    evidence=f"GET {mutated_url} -> /etc/passwd content",
                    impact="Readable files on the server leak.",
                    fix="Resolve realpath and block escapes from the base directory with a prefix check.",
                    subject=url,
                    source="active",
                    cwe=["CWE-22"],
                    tags=["traversal"],
                    request=res.get("request", ""),
                    response=excerpt(body, "root:", 300),
                )
            ]
        if fetcher.stopped:
            return []
    return []


def _methods(base: str, fetcher: Fetcher, origin: str) -> list[Finding]:
    out = []
    try:
        res = fetcher.request(base, method="OPTIONS", origin=origin, max_body=20_000)
    except BudgetExceeded:
        return out
    allow = first(header_map(res), "allow")
    if allow and re.search(r"\b(PUT|DELETE|PATCH)\b", allow, re.I):
        out.append(
            Finding(
                check="active.methods.allow",
                title="Write methods advertised",
                severity="info",
                confidence="high",
                evidence=f"OPTIONS {base} -> Allow: {allow[:160]}",
                impact="Write endpoints are visible to clients.",
                fix="Disable methods you do not need and check auth and CSRF on PUT and DELETE.",
                subject=base,
                source="active",
                cwe=["CWE-650"],
                tags=["method"],
            )
        )
    try:
        res = fetcher.request(base, method="TRACE", origin=origin, max_body=20_000)
    except BudgetExceeded:
        return out
    ctype = first(header_map(res), "content-type")
    if res.get("status") == 200 and "message/http" in ctype:
        out.append(
            Finding(
                check="active.methods.trace",
                title="TRACE enabled",
                severity="info",
                confidence="high",
                evidence=f"TRACE {base} -> 200 message/http",
                impact="Request headers are reflected. This matters for XST in old browsers.",
                fix="Kenarda TRACE'i kapat.",
                subject=base,
                source="active",
                cwe=["CWE-693"],
            )
        )
    return out
