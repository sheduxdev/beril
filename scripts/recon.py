#!/usr/bin/env python3
"""Passive subdomain and origin recon with evidence.

The pass answers four questions without sending a payload:

1. Which hostnames exist for the domain (certificate transparency, passive DNS,
   a small brute-force list)?
2. Which of them serve HTTP or HTTPS, what title, server and stack do they show?
3. Which CNAMEs point at services that hand out a claimable page?
4. Which IPs outside the CDN edge might be the origin?

Hosts are ranked by an exposure score, not by status alone. Output is a normal
Beril report plus an inventory table.

    ./beril recon --target example.com
    ./beril recon --target example.com --owned --out scans/example

Only GET requests and DNS lookups are used. No payload hits a parameter.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import functools
import http.cookiejar
import ipaddress
import json
import os
import random
import re
import shutil
import socket
import subprocess
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import authz
import paths
import web_checks
from beril_model import Finding, Report

DOMAIN_RE = re.compile(r"^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$")
EMAIL_RE = re.compile(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,63}", re.I)
IP_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
PASSWORD_RE = re.compile(r"<input[^>]+type=[\"']?password", re.I)
AUTH_LINK_RE = re.compile(r"href=[\"']([^\"']*(?:login|signin|sign-in|auth|reset|forgot)[^\"']*)", re.I)
VERSION_RE = r"(?:^|[/ ])(\d{1,4}(?:\.\d{1,4}){1,3})"

CHECKED = [
    "Passive hostname sources: crt.sh, Cert Spotter, HackerTarget, DNS Dumpster",
    "Small DNS brute-force list from data/recon.json",
    "A, AAAA and CNAME resolution, wildcard DNS check",
    "HTTP and HTTPS GET with title, server and status",
    "Technology fingerprints from headers, cookies, meta and body",
    "Subdomain takeover fingerprints (CNAME plus page marker)",
    "Origin IP candidates from MX, CT, headers and subdomain A records",
    "High-value host scoring (admin, database, backup, internal, dev, API, auth)",
    "Login and password reset surface on the apex host",
    "Email addresses published on the apex home page",
]
NOT_CHECKED = [
    "Hosts behind a login or a JavaScript-only shell",
    "DNS zone transfer, DNSSEC and cache snooping",
    "Port sweep beyond the origin candidate check",
    "Parameter injection, XSS and authorization bugs",
    "Third-party APIs that need a key",
    "Wildcard certificate coverage and certificate transparency logging",
]


def load_data() -> dict:
    """Load the recon seed file.

    Returns:
        Parsed data, or an empty dict when the file is missing.
    """
    try:
        with open(os.path.join(paths.DATA, "recon.json"), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError):
        return {}


def normalize_domain(value: str) -> str:
    """Turn a URL, host or bare domain into a lowercase host.

    Args:
        value: Raw target.

    Returns:
        Hostname without scheme, port, path or trailing dot.
    """
    raw = value.strip().lower()
    if raw.startswith(("http://", "https://")):
        raw = urllib.parse.urlsplit(raw).hostname or ""
    raw = raw.split("/")[0].split(":")[0].strip(".")
    return raw


def valid_domain(domain: str) -> bool:
    """Check a hostname before DNS work.

    Args:
        domain: Candidate host.

    Returns:
        True when it is a usable DNS name.
    """
    if not domain or len(domain) > 253:
        return False
    if re.match(r"^[\d.]+$", domain):
        return bool(ipaddress.ip_address(domain))
    return bool(DOMAIN_RE.match(domain))


def dig(name: str, record_type: str, timeout: int = 5) -> list[str]:
    """Query one DNS record type with the system resolver tools.

    Args:
        name: Record owner.
        record_type: A, AAAA, CNAME, MX or TXT.
        timeout: Per-command timeout in seconds.

    Returns:
        Record values without a trailing dot. Empty on any failure.
    """
    if shutil.which("dig"):
        cmd = ["dig", "+short", "+time=3", "+tries=1", record_type, name]
    elif shutil.which("nslookup"):
        cmd = ["nslookup", "-type=" + record_type, name]
    else:
        return []
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout).stdout
    except (OSError, subprocess.TimeoutExpired):
        return []
    values: list[str] = []
    for line in out.splitlines():
        value = line.strip().strip('"').rstrip(".")
        if not value or value.startswith(("Server:", "Address:", ";;")) or ("=" in value and record_type == "SOA"):
            continue
        if record_type == "MX":
            parts = value.split()
            value = parts[-1].rstrip(".") if parts else ""
            if value.isdigit() and len(parts) > 1:
                value = parts[-2].rstrip(".")
        if record_type == "TXT":
            value = value.strip('"')
        if value:
            values.append(value)
    return values


def resolve_host(host: str) -> tuple[list[str], list[str]]:
    """Resolve addresses and CNAMEs for a host.

    Args:
        host: Hostname.

    Returns:
        Sorted unique IPs and sorted unique CNAME targets.
    """
    ips: set[str] = set()
    try:
        for info in socket.getaddrinfo(host, None, proto=socket.IPPROTO_TCP):
            addr = str(info[4][0]).split("%")[0]
            if addr:
                ips.add(addr)
    except OSError:
        pass
    cnames = sorted({c.lower().rstrip(".") for c in dig(host, "CNAME")})
    return sorted(ips), cnames


def ip_private(ip: str) -> bool:
    """Check if an address is private, loopback or link local.

    Args:
        ip: Address text.

    Returns:
        True when the address is not a public destination.
    """
    try:
        obj = ipaddress.ip_address(ip)
    except ValueError:
        return True
    return obj.is_private or obj.is_loopback or obj.is_link_local or obj.is_multicast


@functools.lru_cache(maxsize=512)
def network(cidr: str) -> ipaddress.IPv4Network | ipaddress.IPv6Network | None:
    """Parse and cache a CIDR.

    Args:
        cidr: Network text.

    Returns:
        Network object, or None when invalid.
    """
    try:
        return ipaddress.ip_network(cidr, strict=False)
    except ValueError:
        return None


def cdn_name(ip: str, ranges: dict) -> str:
    """Return the CDN name that owns an address.

    Args:
        ip: Address text.
        ranges: Mapping of CDN name to CIDR list.

    Returns:
        CDN name, or an empty string.
    """
    try:
        obj = ipaddress.ip_address(ip)
    except ValueError:
        return ""
    for name, cidrs in ranges.items():
        for cidr in cidrs:
            net = network(cidr)
            if net and obj in net:
                return name
    return ""


def raw_get(url: str, timeout: int = 15) -> tuple[int, str]:
    """Fetch a passive source without the scan budget.

    Args:
        url: Source URL.
        timeout: Request timeout in seconds.

    Returns:
        Status and body. Status 0 on transport failure.
    """
    req = urllib.request.Request(url, headers={"User-Agent": web_checks.UA, "Accept": "application/json, text/plain"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read(2_000_000).decode("utf-8", "replace")
    except Exception:
        return 0, ""


def from_crtsh(domain: str) -> set[str]:
    """Certificate transparency names from crt.sh.

    Args:
        domain: Apex domain.

    Returns:
        Hostnames.
    """
    status, body = raw_get("https://crt.sh/?q=%25." + urllib.parse.quote(domain) + "&output=json")
    out: set[str] = set()
    if status != 200:
        return out
    try:
        rows = json.loads(body)
    except json.JSONDecodeError:
        return out
    for row in rows if isinstance(rows, list) else []:
        for name in str(row.get("name_value", "")).splitlines():
            out.add(name.strip().lower().removeprefix("*."))
    return out


def from_certspotter(domain: str) -> set[str]:
    """Certificate names from the Cert Spotter API.

    Args:
        domain: Apex domain.

    Returns:
        Hostnames.
    """
    url = (
        "https://api.certspotter.com/v1/issuances?domain="
        + urllib.parse.quote(domain)
        + "&include_subdomains=true&expand=dns_names"
    )
    status, body = raw_get(url)
    out: set[str] = set()
    if status != 200:
        return out
    try:
        rows = json.loads(body)
    except json.JSONDecodeError:
        return out
    for row in rows if isinstance(rows, list) else []:
        for name in row.get("dns_names", []):
            out.add(str(name).lower().removeprefix("*."))
    return out


def from_hackertarget(domain: str) -> set[str]:
    """Hostnames from the HackerTarget host search endpoint.

    Args:
        domain: Apex domain.

    Returns:
        Hostnames.
    """
    status, body = raw_get("https://api.hackertarget.com/hostsearch/?q=" + urllib.parse.quote(domain))
    out: set[str] = set()
    if status != 200 or "error" in body[:80].lower():
        return out
    for line in body.splitlines():
        if "," in line:
            out.add(line.split(",", 1)[0].strip().lower())
    return out


def from_dnsdumpster(domain: str) -> set[str]:
    """Hostnames from DNS Dumpster.

    Args:
        domain: Apex domain.

    Returns:
        Hostnames.
    """
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    try:
        with opener.open("https://dnsdumpster.com/", timeout=15) as resp:
            page = resp.read(400_000).decode("utf-8", "replace")
        token = re.search(r"name=[\"']csrfmiddlewaretoken[\"'] value=[\"']([^\"']+)", page)
        if not token:
            return set()
        data = urllib.parse.urlencode({"csrfmiddlewaretoken": token.group(1), "targetip": domain}).encode()
        req = urllib.request.Request(
            "https://dnsdumpster.com/",
            data=data,
            headers={"User-Agent": web_checks.UA, "Referer": "https://dnsdumpster.com/"},
        )
        with opener.open(req, timeout=20) as resp:
            body = resp.read(4_000_000).decode("utf-8", "replace")
    except Exception:
        return set()
    out: set[str] = set()
    for match in re.finditer(r">([a-z0-9.-]+\." + re.escape(domain) + r")<", body, re.I):
        out.add(match.group(1).lower())
    return out


def in_zone(host: str, domain: str) -> bool:
    """Check that a hostname belongs to the apex and is not a wildcard.

    Args:
        host: Candidate host.
        domain: Apex domain.

    Returns:
        True when the name is usable and in zone.
    """
    host = host.strip().lower().rstrip(".")
    return (
        bool(host)
        and (host == domain or host.endswith("." + domain))
        and "*" not in host
        and bool(DOMAIN_RE.match(host))
    )


def subdomain_score(host: str, data: dict) -> int:
    """Pre-rank a host by name before any request is sent.

    Args:
        host: Candidate host.
        data: Recon seed data.

    Returns:
        Keyword score.
    """
    name = host.split(".")[0].lower()
    return sum(points for word, points in data.get("scoring_keywords", {}).items() if word in name)


def brute(domain: str, data: dict, workers: int = 24) -> set[str]:
    """Resolve a small built-in wordlist against the domain.

    Args:
        domain: Apex domain.
        data: Recon seed data with subdomain_words.
        workers: Thread count.

    Returns:
        Resolved hostnames.
    """
    words = data.get("subdomain_words", [])
    out: set[str] = set()

    def one(word: str) -> str | None:
        host = f"{word}.{domain}"
        try:
            socket.getaddrinfo(host, None, proto=socket.IPPROTO_TCP)
            return host
        except OSError:
            return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for result in pool.map(one, words):
            if result:
                out.add(result)
    return out


def enumerate_subdomains(
    domain: str, data: dict, sources: list[str], bruteforce: bool
) -> tuple[set[str], dict, list[str]]:
    """Collect hostnames from the selected passive sources.

    Args:
        domain: Apex domain.
        data: Recon seed data.
        sources: Source names, or all when empty.
        bruteforce: Run the DNS wordlist.

    Returns:
        Hostnames, per-source counts and source errors.
    """
    selected = sources or ["crtsh", "certspotter", "hackertarget", "dnsdumpster"]
    funcs = {
        "crtsh": from_crtsh,
        "certspotter": from_certspotter,
        "hackertarget": from_hackertarget,
        "dnsdumpster": from_dnsdumpster,
    }
    found: set[str] = set()
    counts: dict[str, int] = {}
    errors: list[str] = []
    for name in selected:
        func = funcs.get(name)
        if not func:
            errors.append(f"unknown source: {name}")
            continue
        try:
            result = func(domain)
            counts[name] = len(result)
            found |= result
        except Exception as exc:
            counts[name] = 0
            errors.append(f"{name}: {type(exc).__name__}: {exc}")
    if bruteforce:
        try:
            result = brute(domain, data)
            counts["bruteforce"] = len(result)
            found |= result
        except Exception as exc:
            counts["bruteforce"] = 0
            errors.append(f"bruteforce: {type(exc).__name__}: {exc}")
    return {h for h in found if in_zone(h, domain)}, counts, errors


def header_map(res: dict) -> dict[str, str]:
    """Collapse response headers to lowercase names.

    Args:
        res: Fetcher response.

    Returns:
        Header mapping with the first value per name.
    """
    out: dict[str, str] = {}
    for key, value in res.get("headers", []):
        out.setdefault(str(key).lower(), str(value))
    return out


def http_probe(fetcher: web_checks.Fetcher, host: str) -> dict:
    """Probe HTTPS, then HTTP, and summarize the response.

    Args:
        fetcher: Budgeted client.
        host: Hostname.

    Returns:
        Observation with statuses, title and headers.
    """
    observation = {
        "host": host,
        "http_status": 0,
        "https_status": 0,
        "title": "",
        "server": "",
        "powered_by": "",
        "headers": {},
        "body": "",
        "url": "",
    }
    for scheme in ("https", "http"):
        try:
            res = fetcher.request(f"{scheme}://{host}/", max_body=200_000)
        except web_checks.BudgetExceeded:
            break
        status = res.get("status", 0)
        if scheme == "https":
            observation["https_status"] = status
        else:
            observation["http_status"] = status
        if status:
            headers = header_map(res)
            observation["headers"] = headers
            observation["server"] = headers.get("server", "")
            observation["powered_by"] = headers.get("x-powered-by", "")
            body = res.get("body", "")
            observation["body"] = body
            observation["url"] = res.get("url", f"{scheme}://{host}/")
            match = TITLE_RE.search(body)
            if match:
                observation["title"] = re.sub(r"\s+", " ", match.group(1)).strip()[:160]
            break
    return observation


def version_of(text: str, product: str) -> str:
    """Extract a version that follows a product name.

    Args:
        text: Header or body snippet.
        product: Product token.

    Returns:
        Version string, or an empty string.
    """
    match = re.search(re.escape(product) + r"(?:" + VERSION_RE + r")", text, re.I)
    return match.group(1) if match else ""


def fingerprint(observation: dict, data: dict) -> list[dict]:
    """Match technology fingerprints against one response.

    Args:
        observation: Probe result.
        data: Recon seed data.

    Returns:
        Matches with name, category, version, cpe and source.
    """
    headers = observation.get("headers", {})
    body = observation.get("body", "")[:200_000].lower()
    cookies = headers.get("set-cookie", "").lower()
    title = observation.get("title", "").lower()
    matches: list[dict] = []
    seen: set[str] = set()
    for item in data.get("tech", []):
        name = item.get("name", "")
        if not name or name in seen:
            continue
        hit = False
        source = ""
        for header, needle in item.get("header", {}).items():
            value = headers.get(header, "").lower()
            if value and (not needle or needle in value):
                hit = True
                source = header
                break
        if not hit and item.get("cookie") and item["cookie"] in cookies:
            hit = True
            source = "cookie"
        if not hit and item.get("meta") and item["meta"] in body:
            hit = True
            source = "meta"
        if not hit and item.get("title") and item["title"] in title:
            hit = True
            source = "title"
        if not hit:
            for marker in item.get("body", []):
                if marker.lower() in body:
                    hit = True
                    source = "body"
                    break
        if hit:
            seen.add(name)
            raw = headers.get(source, "") if source in headers else observation.get("body", "")[:20_000]
            matches.append(
                {
                    "name": name,
                    "category": item.get("category", "other"),
                    "version": version_of(raw, name.split()[0]) if source in ("server", "x-powered-by") else "",
                    "cpe": item.get("cpe", ""),
                    "source": source,
                }
            )
    return matches


def score_host(observation: dict, tech: list[dict], data: dict) -> tuple[int, str, list[str]]:
    """Score a host for testing priority.

    Args:
        observation: Probe result.
        tech: Matched technologies.
        data: Recon seed data.

    Returns:
        Score, risk label and reasons.
    """
    name = observation["host"].split(".")[0].lower()
    score = 0
    reasons: list[str] = []
    for word, points in data.get("scoring_keywords", {}).items():
        if word in name:
            score += points
            reasons.append(f"{word} system")
            break
    http_status = observation.get("http_status", 0)
    https_status = observation.get("https_status", 0)
    if 401 in (http_status, https_status):
        score += 25
        reasons.append("authentication required")
    elif 403 in (http_status, https_status):
        score += 20
        reasons.append("access forbidden")
    elif 200 in (http_status, https_status):
        score += 10
        reasons.append("accessible content")
    elif any(code in (500, 502, 503) for code in (http_status, https_status)):
        score += 15
        reasons.append("server error")
    if https_status:
        score += 5
    for item in tech:
        if item.get("category") in ("cms", "framework", "monitoring", "api"):
            score += 4
            reasons.append(item["name"] + " stack")
            break
    if score >= 60:
        label = "critical"
    elif score >= 40:
        label = "high"
    elif score >= 25:
        label = "medium"
    else:
        label = "low"
    return score, label, reasons


def takeover_matches(observation: dict, cnames: list[str], data: dict, dangling: set[str]) -> list[dict]:
    """Match CNAME and body markers for claimable services.

    Args:
        observation: Probe result.
        cnames: CNAME targets.
        data: Recon seed data.
        dangling: CNAME targets that do not resolve.

    Returns:
        Matches with service, cname and confidence.
    """
    body = observation.get("body", "").lower()
    status = observation.get("http_status") or observation.get("https_status") or 0
    out: list[dict] = []
    for item in data.get("takeovers", []):
        for cname in cnames:
            if not any(suffix in cname for suffix in item.get("cname", [])):
                continue
            marker = next((m for m in item.get("body", []) if m.lower() in body), "")
            if marker:
                out.append({"service": item["service"], "cname": cname, "marker": marker, "confidence": "high"})
            elif status == 404 or cname in dangling:
                out.append({"service": item["service"], "cname": cname, "marker": "", "confidence": "medium"})
            break
    return out


def dangling(cnames: list[str], data: dict) -> set[str]:
    """Return CNAMEs that match a takeover service but do not resolve.

    Args:
        cnames: CNAME targets.
        data: Recon seed data.

    Returns:
        Dangling CNAME targets.
    """
    suspects = {
        cname
        for cname in cnames
        if any(suffix in cname for item in data.get("takeovers", []) for suffix in item.get("cname", []))
    }
    return {cname for cname in suspects if not resolve_host(cname)[0]}


def origin_candidates(
    domain: str,
    apex_ips: list[str],
    observations: list[dict],
    ct_hosts: set[str],
    data: dict,
    cdn_ranges: dict,
) -> tuple[list[dict], bool]:
    """Rank public IPs that are not CDN edges.

    Args:
        domain: Apex domain.
        apex_ips: Apex addresses.
        observations: Host observations.
        ct_hosts: Hostnames from certificate transparency.
        data: Recon seed data.
        cdn_ranges: CDN CIDR map.

    Returns:
        Scored candidates and whether the apex sits behind a CDN.
    """
    apex_cdn = any(cdn_name(ip, cdn_ranges) for ip in apex_ips)
    methods: dict[str, set[str]] = {}
    for ip in apex_ips:
        methods.setdefault(ip, set()).add("apex")
    for mx in dig(domain, "MX"):
        for ip in resolve_host(mx)[0]:
            methods.setdefault(ip, set()).add("mail")
    for host in list(ct_hosts)[:60]:
        for ip in resolve_host(host)[0]:
            methods.setdefault(ip, set()).add("cert_transparency")
    for observation in observations:
        ip = observation.get("ip", "")
        if ip:
            methods.setdefault(ip, set()).add("subdomain")
        for header in data.get("ip_headers", []):
            value = observation.get("headers", {}).get(header, "")
            for found in IP_RE.findall(value):
                methods.setdefault(found, set()).add("http_header")
    scores: dict[str, dict] = {}
    for ip, found_by in methods.items():
        if ip_private(ip) or cdn_name(ip, cdn_ranges):
            continue
        score = 0
        for method in found_by:
            score += {"mail": 10, "http_header": 8, "apex": 6, "cert_transparency": 4, "subdomain": 3}[method]
        if len(found_by) > 1:
            score += 5 * len(found_by)
        answer = responds(ip)
        if answer:
            score += 10
        scores[ip] = {"ip": ip, "score": score, "methods": sorted(found_by), "responds": answer}
    ranked = sorted(scores.values(), key=lambda item: item["score"], reverse=True)
    return ranked[:10], apex_cdn


def responds(ip: str) -> bool:
    """Check for an open web port on an address.

    Args:
        ip: Address text.

    Returns:
        True when 80, 443, 8080 or 8443 accepts a connection.
    """
    for port in (443, 80, 8443, 8080):
        try:
            with socket.create_connection((ip, port), timeout=1.5):
                return True
        except OSError:
            continue
    return False


def auth_surface(fetcher: web_checks.Fetcher, base: str, data: dict) -> dict:
    """Find login and password reset pages on the apex host.

    Args:
        fetcher: Budgeted client.
        base: Normalized base URL.
        data: Recon seed data.

    Returns:
        Mapping of page type to URL list.
    """
    out = {"login": [], "reset": []}
    seen: set[str] = set()
    candidates: list[tuple[str, str]] = []
    for path in data.get("auth_paths", []):
        candidates.append(("login", urllib.parse.urljoin(base, path.lstrip("/"))))
    for path in data.get("reset_paths", []):
        candidates.append(("reset", urllib.parse.urljoin(base, path.lstrip("/"))))
    try:
        home = fetcher.request(base, max_body=200_000)
    except web_checks.BudgetExceeded:
        return out
    for link in AUTH_LINK_RE.findall(home.get("body", "")):
        url = urllib.parse.urljoin(base, link)
        if urllib.parse.urlsplit(url).hostname == urllib.parse.urlsplit(base).hostname:
            kind = "reset" if re.search(r"reset|forgot|recover", url, re.I) else "login"
            candidates.append((kind, url))
    for kind, url in candidates:
        if url in seen:
            continue
        seen.add(url)
        if len(seen) > 40:
            break
        try:
            res = fetcher.request(url, max_body=120_000)
        except web_checks.BudgetExceeded:
            break
        status = res.get("status", 0)
        body = res.get("body", "")
        text = body[:50_000].lower()
        looks = bool(PASSWORD_RE.search(body)) or any(word in text for word in data.get("auth_keywords", []))
        if status in (200, 401, 403) and looks:
            out[kind].append(url)
    return out


def emails_on(fetcher: web_checks.Fetcher, base: str, domain: str) -> list[str]:
    """Collect published addresses on the apex home page.

    Args:
        fetcher: Budgeted client.
        base: Normalized base URL.
        domain: Apex domain.

    Returns:
        Sorted unique addresses in zone.
    """
    try:
        res = fetcher.request(base, max_body=400_000)
    except web_checks.BudgetExceeded:
        return []
    found = {m.group(0).lower() for m in EMAIL_RE.finditer(res.get("body", ""))}
    return sorted(email for email in found if email.endswith(("@" + domain, "." + domain)))


def add(report: Report, **kwargs: object) -> None:
    """Add a finding when the required text is present.

    Args:
        report: Target report.
        kwargs: Finding fields.
    """
    report.add(Finding(**kwargs))  # type: ignore[arg-type]


def build_findings(
    report: Report,
    inventory: list[dict],
    takeovers: list[dict],
    origins: list[dict],
    apex_cdn: bool,
    auth: dict,
    emails: list[str],
    wildcard: list[str],
) -> None:
    """Translate observations into findings.

    Args:
        report: Target report.
        inventory: Scored host list.
        takeovers: Takeover matches.
        origins: Origin candidates.
        apex_cdn: Whether the apex is behind a CDN.
        auth: Auth surface result.
        emails: Published addresses.
        wildcard: Wildcard DNS addresses.
    """
    for item in takeovers:
        host = item["host"]
        add(
            report,
            check="recon.takeover",
            title=f"Subdomain takeover candidate: {host}",
            severity="high",
            confidence=item["confidence"],
            evidence=f"{host} CNAME {item['cname']} -> {item['service']}"
            + (f", marker {item['marker']!r}" if item["marker"] else ""),
            impact="A claimable service page can let a third party serve content on your hostname.",
            fix=f"Claim the {item['service']} resource or remove the dangling CNAME.",
            subject=host,
            cwe=["CWE-350"],
            tags=["takeover", "dns"],
            false_positive="A live but parked service can look the same. Confirm the resource owner.",
            state="observed" if item["marker"] else "inferred",
        )
    for item in inventory:
        if item["score"] < 40:
            continue
        severity = "medium" if item["score"] >= 60 else "info"
        status = item["https_status"] or item["http_status"]
        state_label = "exposed" if status else "in DNS only"
        tech = ", ".join(t["name"] for t in item["tech"][:4]) or "no stack marker"
        add(
            report,
            check="recon.high-value-host",
            title=f"High-value host {state_label}: {item['host']} ({item['risk']})",
            severity=severity,
            confidence="medium",
            evidence=f"{item['host']} score {item['score']}: {', '.join(item['reasons'])}; HTTP {status or 'none'}; {tech}",
            impact="Administrative, database, backup or development systems widen the entry surface.",
            fix="Confirm authentication, patch level and IP restrictions on this host.",
            subject=item["host"],
            cwe=["CWE-668"],
            tags=["exposure"],
        )
        if not item["https_status"] and item["http_status"]:
            add(
                report,
                check="recon.https-missing",
                title=f"High-value host speaks HTTP only: {item['host']}",
                severity="medium",
                confidence="high",
                evidence=f"{item['host']} answered HTTP {item['http_status']} and HTTPS did not answer",
                impact="Credentials and session cookies on an admin or API host can cross the wire in clear text.",
                fix="Serve the host over TLS and redirect HTTP.",
                subject=item["host"],
                cwe=["CWE-319"],
                tags=["tls"],
            )
        if any(code in (500, 502, 503) for code in (item["http_status"], item["https_status"])):
            add(
                report,
                check="recon.server-error",
                title=f"High-value host returns a server error: {item['host']}",
                severity="low",
                confidence="high",
                evidence=f"{item['host']} HTTP {item['http_status']} HTTPS {item['https_status']}",
                impact="Error pages often disclose stack traces, versions and path layouts.",
                fix="Read the full response and disable verbose errors in production.",
                subject=item["host"],
                tags=["disclosure"],
            )
    if apex_cdn:
        for item in origins[:3]:
            add(
                report,
                check="recon.origin-ip",
                title=f"Possible origin IP behind the CDN: {item['ip']}",
                severity="info",
                confidence="medium" if len(item["methods"]) > 1 else "low",
                evidence=f"{item['ip']} score {item['score']} via {', '.join(item['methods'])}",
                impact="If the origin accepts direct traffic, CDN WAF and rate rules can be bypassed.",
                fix="Firewall the origin to CDN ranges or require a host header and mTLS from the edge.",
                subject=item["ip"],
                cwe=["CWE-668"],
                tags=["origin", "cdn"],
                false_positive="A shared host or a second CDN node can look like an origin.",
                state="inferred",
            )
    for kind, label in (("login", "Login"), ("reset", "Password reset")):
        for url in auth.get(kind, []):
            add(
                report,
                check=f"recon.auth.{kind}",
                title=f"{label} page reachable",
                severity="info",
                confidence="high",
                evidence=f"GET {url} returned an auth form",
                impact="The endpoint is a target for credential stuffing, user enumeration and reset flaws.",
                fix="Add rate limiting, MFA and a generic error message.",
                subject=url,
                tags=["auth", "surface"],
            )
    if emails:
        add(
            report,
            check="recon.emails",
            title=f"{len(emails)} email address(es) published on the home page",
            severity="info",
            confidence="high",
            evidence=", ".join(emails[:8]) + (" ..." if len(emails) > 8 else ""),
            impact="Addresses feed phishing and password spray lists.",
            fix="Use role addresses where possible and keep the published set small.",
            subject=emails[0],
            tags=["osint"],
        )
    if wildcard:
        add(
            report,
            check="recon.wildcard-dns",
            title="Wildcard DNS is on",
            severity="info",
            confidence="high",
            evidence="random label resolved to " + ", ".join(wildcard[:3]),
            impact="Every made-up name resolves, so brute-force hits need an HTTP check before they count.",
            fix="Keep the wildcard if it serves a default app. Otherwise remove it.",
            subject="wildcard:" + report.target,
            tags=["dns"],
        )


def markdown(
    report: Report, inventory: list[dict], origins: list[dict], auth: dict, emails: list[str], apex_cdn: bool
) -> str:
    """Render the recon view. The JSON report stays the source of truth.

    Args:
        report: Target report.
        inventory: Scored hosts.
        origins: Origin candidates.
        auth: Auth surface.
        emails: Published addresses.
        apex_cdn: Whether the apex is behind a CDN.

    Returns:
        Markdown text.
    """
    c = report.counts()
    lines = [
        f"# Recon: {report.target}",
        "",
        f"Generated {report.finished_at} by Beril {report.tool_version}. Mode: {report.mode}.",
        "",
        f"{len(inventory)} hosts, {c['critical']} critical, {c['high']} high, {c['medium']} medium, "
        f"{c['low']} low, {c['info']} info.",
        "",
        "## Limits",
        "",
        f"- Requests sent: {report.limits.get('requests_sent', 0)} of {report.limits.get('max_requests', 0)}",
        f"- Rate: {report.limits.get('rate_per_second', '')}/s",
        f"- robots.txt: {report.limits.get('robots', 'off')}",
        "",
    ]
    if report.errors:
        lines += ["## Errors", ""] + [f"- {error}" for error in report.errors] + [""]
    lines += [
        "## Host inventory",
        "",
        "| Host | IP | HTTP | HTTPS | Title | Server | Score | Risk | Category | Tech |",
        "|---|---|---:|---:|---|---|---:|---|---|---|",
    ]
    for item in inventory[:250]:
        title = (item["title"] or "").replace("|", "/")[:60]
        server = (item["server"] or "").replace("|", "/")[:40]
        tech = ", ".join(t["name"] for t in item["tech"][:3])
        lines.append(
            f"| {item['host']} | {item['ip'] or '-'} | {item['http_status'] or '-'} | {item['https_status'] or '-'} "
            f"| {title} | {server} | {item['score']} | {item['risk']} | {item['category']} | {tech} |"
        )
    lines.append("")
    if apex_cdn:
        lines += ["## Origin candidates", ""]
        if origins:
            for item in origins:
                lines.append(f"- {item['ip']} score {item['score']} via {', '.join(item['methods'])}")
        else:
            lines.append("- None outside the CDN ranges.")
        lines.append("")
    lines += ["## Auth surface", ""]
    for kind in ("login", "reset"):
        for url in auth.get(kind, []):
            lines.append(f"- {kind}: {url}")
    if not auth.get("login") and not auth.get("reset"):
        lines.append("- No auth page matched.")
    lines.append("")
    lines += ["## Published emails", ""]
    lines += [f"- {email}" for email in emails[:30]] or ["- None found."]
    lines += ["", "## Findings", ""]
    for finding in report.findings:
        lines += [
            f"### [{finding.severity.upper()}] {finding.title}",
            "",
            f"- Confidence: {finding.confidence}",
            f"- Evidence: {finding.evidence}",
            f"- Impact: {finding.impact}",
            f"- Fix: {finding.fix}",
        ]
        if finding.false_positive:
            lines.append(f"- False positive: {finding.false_positive}")
        lines.append("")
    lines += ["## Scope", "", "**Checks attempted**"]
    lines += [f"- {item}" for item in report.checked()]
    lines += ["", "**Checks not attempted**"]
    lines += [f"- {item}" for item in report.not_checked()]
    if report.authorization:
        lines += ["", "**Authorization**", f"- {report.authorization.get('method', '')}"]
    lines.append("")
    return "\n".join(lines)


def recon(
    target: str,
    owned: bool = False,
    scope_file: str = "",
    timeout: int = 10,
    rate: float = 4.0,
    max_requests: int = 300,
    max_hosts: int = 120,
    sources: list[str] | None = None,
    bruteforce: bool = True,
    auth_pages: bool = True,
    profile: str = "engineer",
) -> Report:
    """Run the passive recon pass.

    Args:
        target: Domain or URL.
        owned: Record an ownership acknowledgement.
        scope_file: Hosts or patterns allowed by the engagement.
        timeout: HTTP timeout.
        rate: Requests per second.
        max_requests: Hard request budget.
        max_hosts: Cap on probed hosts.
        sources: Passive source names.
        bruteforce: Run the DNS wordlist.
        auth_pages: Probe the auth surface on the apex.
        profile: Report profile label.

    Returns:
        Finished report with inventory in meta.
    """
    domain = normalize_domain(target)
    report = Report(target=domain or target, mode="passive", profile=profile)
    report.scope["checked"] = list(CHECKED)
    report.scope["not_checked"] = list(NOT_CHECKED)
    report.scope["out_of_scope"] = ["Write operations", "Authenticated areas"]
    report.limits = {
        "user_agent": web_checks.UA,
        "max_requests": max_requests,
        "rate_per_second": rate,
        "robots": "off",
        "max_hosts": max_hosts,
    }
    if domain:
        report.authorization = authz.require(domain, owned=owned, note="recon acknowledgement") or {}
    if not valid_domain(domain):
        report.errors.append(f"invalid domain: {target}")
        return report.finish()

    data = load_data()
    if not data:
        report.errors.append("data/recon.json is missing or unreadable")
        return report.finish()

    scope = authz.load_scope(scope_file) if scope_file else []
    if scope:
        report.scope["in_scope"] = scope

    hosts, counts, source_errors = enumerate_subdomains(domain, data, sources or [], bruteforce)
    hosts.add(domain)
    if scope:
        hosts = {host for host in hosts if host == domain or authz.in_scope("https://" + host, scope)}
        report.scope["out_of_scope"].append("Discovered hosts outside the scope file")
    report.meta["sources"] = counts
    if source_errors:
        report.errors += ["source: " + error for error in source_errors]

    wildcard_ips = resolve_host(f"{random.randrange(10**11, 10**12)}.{domain}")[0]
    report.meta["wildcard_dns"] = wildcard_ips

    ranked = sorted(hosts, key=lambda host: (host != domain, -subdomain_score(host, data), host))[:max_hosts]
    fetcher = web_checks.Fetcher(timeout=timeout, rate=rate, max_requests=max_requests, respect_robots=False)

    resolved: dict[str, tuple[list[str], list[str]]] = {}

    def resolve_one(host: str) -> None:
        resolved[host] = resolve_host(host)

    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        list(pool.map(resolve_one, ranked))

    observations: list[dict] = []
    takeovers: list[dict] = []
    inventory: list[dict] = []

    def probe_one(host: str) -> tuple[dict, list[dict]]:
        ips, cnames = resolved.get(host, ([], []))
        observation = http_probe(fetcher, host)
        observation["ip"] = ips[0] if ips else ""
        observation["cnames"] = cnames
        tech = fingerprint(observation, data)
        observation["tech"] = tech
        return observation, takeover_matches(observation, cnames, data, dangling(cnames, data))

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(probe_one, host): host for host in ranked}
        for future in concurrent.futures.as_completed(futures):
            try:
                observation, hits = future.result()
            except Exception as exc:
                report.errors.append(f"{futures[future]}: {type(exc).__name__}: {exc}")
                continue
            observations.append(observation)
            for hit in hits:
                hit["host"] = observation["host"]
                takeovers.append(hit)

    cdn_ranges = data.get("cdn_ranges", {})
    for observation in observations:
        score, risk, reasons = score_host(observation, observation["tech"], data)
        category = "uncategorized"
        name = observation["host"].split(".")[0].lower()
        for _level, groups in data.get("categories", {}).items():
            for label, words in groups.items():
                if any(word in name for word in words):
                    category = label
                    break
            if category != "uncategorized":
                break
        observation["score"] = score
        observation["risk"] = risk
        observation["reasons"] = reasons
        observation["category"] = category
        ip = observation["ip"]
        observation["cdn"] = cdn_name(ip, cdn_ranges)
        inventory.append(
            {
                "host": observation["host"],
                "ip": ip,
                "http_status": observation["http_status"],
                "https_status": observation["https_status"],
                "title": observation["title"],
                "server": observation["server"],
                "tech": observation["tech"],
                "score": score,
                "risk": risk,
                "reasons": reasons,
                "category": category,
                "cname": observation["cnames"],
                "cdn": observation["cdn"],
            }
        )
    inventory.sort(key=lambda item: item["score"], reverse=True)
    origins, apex_cdn = origin_candidates(
        domain, resolved.get(domain, ([], []))[0], observations, hosts, data, cdn_ranges
    )

    base = f"https://{domain}/"
    auth = {"login": [], "reset": []}
    emails: list[str] = []
    if auth_pages:
        auth = auth_surface(fetcher, base, data)
        emails = emails_on(fetcher, base, domain)

    build_findings(report, inventory, takeovers, origins, apex_cdn, auth, emails, wildcard_ips)
    report.meta.update(
        {
            "inventory": inventory,
            "takeovers": takeovers,
            "origin_candidates": origins,
            "apex_behind_cdn": apex_cdn,
            "auth_surface": auth,
            "emails": emails,
        }
    )
    report.limits["requests_sent"] = fetcher.sent
    if fetcher.stopped:
        report.errors.append(f"request budget spent ({max_requests}); later hosts are missing")
    report.meta["risk"] = {
        "score": min(100, sum(item["score"] for item in inventory if item["score"] >= 40) // 4),
        "hosts": len(inventory),
        "active": sum(1 for item in inventory if item["http_status"] or item["https_status"]),
        "https": sum(1 for item in inventory if item["https_status"]),
    }
    report.finish()
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", default="", help="domain or URL")
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--profile", default="engineer", choices=("engineer", "bugbounty", "smb"))
    ap.add_argument("--owned", action="store_true", help="record an ownership acknowledgement")
    ap.add_argument("--scope", default="", help="scope file: hosts, *.hosts or host/path prefixes")
    ap.add_argument("--timeout", type=int, default=10)
    ap.add_argument("--rate", type=float, default=4.0)
    ap.add_argument("--max-requests", type=int, default=300)
    ap.add_argument("--max-hosts", type=int, default=120)
    ap.add_argument("--sources", default="", help="crtsh, certspotter, hackertarget, dnsdumpster")
    ap.add_argument("--no-bruteforce", action="store_true")
    ap.add_argument("--no-auth", action="store_true")
    ap.add_argument("--fail-on", default="none", choices=("none", "info", "low", "medium", "high", "critical"))
    args = ap.parse_args()
    target = args.target or input("Domain (own it or have permission): ").strip()
    if not target:
        sys.exit("no target given")
    report = recon(
        target,
        args.owned,
        args.scope,
        args.timeout,
        args.rate,
        args.max_requests,
        args.max_hosts,
        [s.strip().lower() for s in args.sources.split(",") if s.strip()],
        not args.no_bruteforce,
        not args.no_auth,
        args.profile,
    )
    text = (
        report.to_json()
        if args.json
        else markdown(
            report,
            report.meta.get("inventory", []),
            report.meta.get("origin_candidates", []),
            report.meta.get("auth_surface", {}),
            report.meta.get("emails", []),
            report.meta.get("apex_behind_cdn", False),
        )
    )
    print(text)
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "_", normalize_domain(target)).strip("_")[:80] or "recon"
    out = args.out or os.path.join("scans", "recon-" + slug)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    report.write_json(out + ".json")
    with open(out + ".md", "w", encoding="utf-8") as fh:
        fh.write(
            markdown(
                report,
                report.meta.get("inventory", []),
                report.meta.get("origin_candidates", []),
                report.meta.get("auth_surface", {}),
                report.meta.get("emails", []),
                report.meta.get("apex_behind_cdn", False),
            )
            + "\n"
        )
    print(f"\nwrote {out}.json and {out}.md", file=sys.stderr)
    if args.fail_on != "none":
        raise SystemExit(report.exit_code(args.fail_on))


if __name__ == "__main__":
    main()
