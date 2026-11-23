#!/usr/bin/env python3
"""Static checks for vibe-coded apps: Supabase RLS, client-side keys, CORS.

Born from the 2026 Supabase exposure wave. The anon key is public by design;
the data is protected only by Row Level Security. The dangerous pattern is a
table created through an API or a migration without RLS, or a service_role
key shipped to the browser.

Static only, no database connection.

    python scripts/scan_vibe.py --target ./my-lovable-app
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections.abc import Iterator

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fileio
from beril_model import Finding, Report

SKIP = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".next", ".nuxt", "coverage"}
CLIENT_HINTS = (
    "components",
    "pages",
    "app/",
    "src/app",
    "src/components",
    "src/pages",
    "public/",
    "hooks/",
    "lib/",
    "utils/",
)
CODE_EXT = {".ts", ".tsx", ".js", ".jsx", ".vue", ".svelte"}
SQL_EXT = {".sql"}
MAX_FILES = 12_000

TABLE = re.compile(r"create\s+table\s+(?:if\s+not\s+exists\s+)?[\"`]?([\w.]+)", re.I)
RLS = re.compile(r"enable\s+row\s+level\s+security", re.I)
POLICY = re.compile(r"create\s+policy", re.I)
PUBLIC_BUCKET = re.compile(r"(?i)public\s*[:=]\s*true|create\s+bucket\s+[^;]+public", re.I)
SERVICE = re.compile(r"service[_-]?role", re.I)
NEXT_PUBLIC_SECRET = re.compile(r"NEXT_PUBLIC_[\w]*(?:SECRET|SERVICE|PRIVATE|TOKEN|KEY)[\w]*", re.I)
VITE_SECRET = re.compile(r"VITE_[\w]*(?:SECRET|SERVICE|PRIVATE)[\w]*", re.I)
DANGEROUS_HTML = re.compile(r"dangerouslySetInnerHTML|v-html")
SANITIZE = re.compile(r"(?i)(dompurify|sanitize-html|xss|marked\s*\(\s*.+\s*\)\s*$)")
AUTH_HINT = re.compile(
    r"(?i)(getserversession|getuser\(|auth\(\)|currentuser|requireauth|withauth|clerk|"
    r"better-auth|supabase\.auth|verifytoken|jwt\.verify)"
)
CORS_STAR = re.compile(r"(?i)(cors\(|access-control-allow-origin).{0,80}['\"]\*['\"]")
FIREBASE_OPEN = re.compile(r"allow\s+(?:read|write)\s*:\s*if\s+true", re.I)


def iter_files(root: str) -> Iterator[str]:
    count = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for name in filenames:
            path = os.path.join(dirpath, name)
            if os.path.splitext(name)[1].lower() in CODE_EXT | SQL_EXT | {".rules", ".json"}:
                yield path
                count += 1
                if count >= MAX_FILES:
                    return


def is_client(rel: str) -> bool:
    return any(hint in rel.replace(os.sep, "/").lower() for hint in CLIENT_HINTS)


def scan(target: str) -> Report:
    report = Report(target=target, mode="source")
    report.scope["checked"] = [
        "RLS presence in SQL migrations",
        "service_role in the client bundle",
        "NEXT_PUBLIC and VITE secret names",
        "Open CORS and v-html",
        "Firebase rules",
        "Auth hints in API routes",
    ]
    report.scope["not_checked"] = [
        "Live database policies",
        "Supabase storage settings (live)",
        "Edge function code",
        "Real key validity",
    ]
    if not os.path.exists(target):
        report.errors.append("target missing")
        return report.finish()
    files = list(iter_files(target))
    if not files:
        report.errors.append("no code file to scan")
        return report.finish()
    for path in files:
        rel = os.path.relpath(path, target)
        try:
            with open(path, encoding="utf-8", errors="replace") as handle:
                text = handle.read()
        except OSError:
            continue
        ext = os.path.splitext(path)[1].lower()
        report_findings = scan_sql(rel, text) if ext in SQL_EXT else scan_code(rel, text)
        for finding in report_findings:
            report.add(finding)
    report.finish()
    return report


def scan_sql(rel: str, text: str) -> list[Finding]:
    out = []
    for match in TABLE.finditer(text):
        table = match.group(1)
        window = text[match.end() : match.end() + 1500]
        if RLS.search(window) or POLICY.search(window):
            continue
        out.append(
            Finding(
                check="vibe.rls-missing",
                title=f"Table created without RLS: {table}",
                severity="high",
                confidence="medium",
                evidence=f"{rel}: {match.group(0)[:120]}",
                impact="The anon key is public. Without RLS the table is read and written over REST.",
                fix="Add `alter table ... enable row level security` and a fitting policy to the migration. "
                "Tables created through the API have no default protection.",
                subject=f"{rel}:{text[:match.start()].count(chr(10)) + 1}",
                source="static",
                cwe=["CWE-284"],
                tags=["supabase", "rls"],
                false_positive="RLS may be enabled in another migration. Verify with `\\dt+` and pg_policies.",
            )
        )
    if PUBLIC_BUCKET.search(text):
        out.append(
            Finding(
                check="vibe.public-bucket",
                title="Public storage bucket",
                severity="low",
                confidence="medium",
                evidence=f"{rel}: public bucket declaration",
                impact="Bucket content is read without a key.",
                fix="Open only the bucket that must be public.",
                subject=rel,
                source="static",
                cwe=["CWE-284"],
            )
        )
    return out


def scan_code(rel: str, text: str) -> list[Finding]:
    out = []
    client = is_client(rel)
    if SERVICE.search(text) and client:
        lines = [i + 1 for i, line in enumerate(text.splitlines()) if SERVICE.search(line)]
        out.append(
            Finding(
                check="vibe.service-role-client",
                title="service_role on the client side",
                severity="high",
                confidence="medium",
                evidence=f"{rel}:{lines[0]} service_role reference",
                impact="service_role bypasses RLS. If it reaches the browser, all data access opens.",
                fix="Use it on the server (server component, route handler, edge function). "
                "Keep only the anon key in the client.",
                subject=f"{rel}:{lines[0]}",
                source="static",
                cwe=["CWE-522"],
                tags=["supabase"],
                false_positive="Harmless when the file is shared but imported on the server only.",
            )
        )
    for match in NEXT_PUBLIC_SECRET.finditer(text):
        name = match.group(0)
        if "ANON" in name.upper():
            continue
        out.append(
            Finding(
                check="vibe.public-secret",
                title=f"Public prefixed secret: {name}",
                severity="high",
                confidence="medium",
                evidence=rel,
                impact="The value lands in the browser bundle.",
                fix="Drop the prefix or move the value to a server function.",
                subject=rel,
                source="static",
                cwe=["CWE-522"],
                tags=["build"],
                false_positive="Being public can be intended (Supabase anon, Stripe publishable).",
            )
        )
    for match in VITE_SECRET.finditer(text):
        out.append(
            Finding(
                check="vibe.vite-secret",
                title=f"VITE prefixed secret: {match.group(0)}",
                severity="high",
                confidence="medium",
                evidence=rel,
                impact="Vite bakes the value into the client bundle.",
                fix="Keep it on the server or drop the prefix.",
                subject=rel,
                source="static",
                cwe=["CWE-522"],
            )
        )
    if DANGEROUS_HTML.search(text) and not SANITIZE.search(text):
        line = text[: DANGEROUS_HTML.search(text).start()].count("\n") + 1
        out.append(
            Finding(
                check="vibe.dangerous-html",
                title="Unsanitized HTML sink",
                severity="medium",
                confidence="low",
                evidence=f"{rel}:{line}",
                impact="User data here becomes stored XSS.",
                fix="Sanitize with DOMPurify or sanitize-html.",
                subject=f"{rel}:{line}",
                source="static",
                cwe=["CWE-79"],
                false_positive="Risk drops when the content is fixed and trusted.",
            )
        )
    if CORS_STAR.search(text) and re.search(r"(?i)credentials\s*:\s*true", text):
        out.append(
            Finding(
                check="vibe.cors-star-credentials",
                title="CORS wildcard with credentials",
                severity="medium",
                confidence="medium",
                evidence=rel,
                impact="Origin allowlist yoksa oturum verisi okunabilir.",
                fix="Reflect the origin from an allowlist.",
                subject=rel,
                source="static",
                cwe=["CWE-942"],
            )
        )
    if FIREBASE_OPEN.search(text):
        out.append(
            Finding(
                check="vibe.firebase-open",
                title="Firebase rule open to all",
                severity="high",
                confidence="high",
                evidence=rel,
                impact="The collection is open to every client.",
                fix="Add `if request.auth != null` and field level conditions.",
                subject=rel,
                source="static",
                cwe=["CWE-284"],
            )
        )
    if re.search(r"/api/[\w/\[\]-]+/route\.(?:ts|js)$", rel.replace(os.sep, "/")) and not AUTH_HINT.search(text):
        out.append(
            Finding(
                check="vibe.route-no-auth",
                title="No auth hint in an API route",
                severity="medium",
                confidence="low",
                evidence=rel,
                impact="The route may be public, which risks data leak.",
                fix="Add a session check or document that the route is intentionally public.",
                subject=rel,
                source="static",
                cwe=["CWE-306"],
                false_positive="Public endpoint'lerde auth gerekmez.",
            )
        )
    return out


def render(report: Report) -> str:
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
    lines = [f"# Vibe-coding audit: {report.target}", "", f"{len(report.findings)} findings. Static.", ""]
    for f in sorted(report.findings, key=lambda x: order.get(x.severity, 9)):
        lines += [f"- [{f.severity}/{f.confidence}] {f.title}: {f.evidence}", f"  - {f.fix}"]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    report = scan(args.target)
    print(report.to_json() if args.json else render(report))
    if args.out:
        fileio.write_json(args.out + ".json", report.to_dict())
        fileio.write_text(args.out + ".md", render(report) + "\n")


if __name__ == "__main__":
    main()
