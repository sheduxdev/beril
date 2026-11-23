#!/usr/bin/env python3
"""Build an evidence dossier from a claims file.

A journalist or OSINT file is only as good as its source trail. Each claim in
``claims.jsonl`` names a source, a status and optionally a quote. The tool
hashes the local source, checks the quote, and reports claims that are marked
confirmed without a source.

    ./beril evidence --target ./story
    ./beril evidence --target ./story --fetch --out story/evidence

``--fetch`` downloads URL sources (2 MB cap, 15 s timeout) and stores the hash of
the bytes seen. Offline is the default and hashes stay empty for URLs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fileio
import report_render
import suppress
from beril_model import Finding, Report, load_report

UA = "Beril/1.4 evidence"
MAX_BYTES = 2_000_000
KINDS = ("confirmed", "inferred")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_claims(target: str) -> tuple[list[dict], list[str]]:
    path = os.path.join(target, "claims.jsonl")
    claims, errors = [], []
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            for number, line in enumerate(handle, 1):
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    claim = json.loads(line)
                except json.JSONDecodeError:
                    errors.append(f"claims.jsonl:{number} is not JSON")
                    continue
                if isinstance(claim, dict):
                    claim["_line"] = number
                    claims.append(claim)
    except OSError:
        errors.append("claims.jsonl missing")
    return claims, errors


def source_bytes(claim: dict, target: str, fetch: bool) -> tuple[bytes, str]:
    local = str(claim.get("local", ""))
    if local:
        path = local if os.path.isabs(local) else os.path.join(target, local)
        try:
            with open(path, "rb") as handle:
                return handle.read(MAX_BYTES), path
        except OSError:
            return b"", path
    url = str(claim.get("source", ""))
    if fetch and url.startswith(("http://", "https://")):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(request, timeout=15) as response:
                return response.read(MAX_BYTES), url
        except Exception:
            return b"", url
    return b"", url


def inspect(target: str, fetch: bool = False) -> Report:
    report = Report(target=target, mode="source", profile="evidence")
    report.scope["checked"] = [
        "Claim and source fields",
        "Status label",
        "Local source presence",
        "Source hash",
        "Quote against the source",
    ]
    report.scope["not_checked"] = [
        "Truth of the source itself",
        "Archive freshness",
        "Paywall or login-only pages",
        "Chain of custody before the file",
    ]
    claims, errors = load_claims(target)
    report.errors.extend(errors)
    confirmed = inferred = 0
    for claim in claims:
        line = claim["_line"]
        text = str(claim.get("claim", "")).strip()
        kind = str(claim.get("kind", "")).strip().lower()
        source = str(claim.get("source", "")).strip()
        visible = str(claim.get("local", "")) or source or "no source"
        subject = f"claims.jsonl:{line}"
        if not text:
            report.add(
                Finding(
                    check="evidence.empty-claim",
                    title="Empty claim",
                    severity="low",
                    confidence="high",
                    evidence=subject,
                    impact="The row carries no statement.",
                    fix="Write one sentence or remove the row.",
                    subject=subject,
                    source="static",
                )
            )
            continue
        if kind not in KINDS:
            report.add(
                Finding(
                    check="evidence.bad-status",
                    title="Claim has no confirmed/inferred label",
                    severity="medium",
                    confidence="high",
                    evidence=f"{subject} {visible}",
                    impact="The reader cannot tell evidence from inference.",
                    fix="Set kind to confirmed or inferred.",
                    subject=subject,
                    source="static",
                )
            )
        if kind == "confirmed":
            confirmed += 1
        elif kind == "inferred":
            inferred += 1
        data, resolved = source_bytes(claim, target, fetch)
        digest = sha256_bytes(data) if data else ""
        if not data:
            severity = "high" if kind == "confirmed" else "low"
            report.add(
                Finding(
                    check="evidence.missing-source",
                    title=text[:160],
                    severity=severity,
                    confidence="high",
                    evidence=f"{subject} {text[:100]}",
                    impact="The claim cannot be re-checked.",
                    fix="Add a local copy or a URL, then re-run.",
                    subject=subject,
                    source="static",
                    verified=False,
                )
            )
        else:
            report.add(
                Finding(
                    check="evidence.claim",
                    title=text[:160],
                    severity="info",
                    confidence="high",
                    evidence=f"{subject} {resolved} sha256:{digest[:16]}",
                    impact="Traceable claim with a hashed source.",
                    fix="Keep the source copy with this file.",
                    subject=subject,
                    source="static",
                    verified=True,
                )
            )
        quote = str(claim.get("quote", "")).strip()
        if quote and data:
            haystack = data.decode("utf-8", errors="replace")
            if quote not in haystack:
                report.add(
                    Finding(
                        check="evidence.quote-mismatch",
                        title=f"{text[:120]} (quote mismatch)",
                        severity="medium",
                        confidence="medium",
                        evidence=f"{subject} {resolved}",
                        impact="The quoted text may come from another version or page.",
                        fix="Fix the quote or pin the exact source copy.",
                        subject=subject,
                        source="static",
                    )
                )
    report.meta = {
        "claims": len(claims),
        "confirmed": confirmed,
        "inferred": inferred,
        "fetched": bool(fetch),
        "hashed": sum(1 for c in claims if c.get("local")),
    }
    report.finish()
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--baseline", default="")
    ap.add_argument("--suppress", default="")
    args = ap.parse_args()
    if not os.path.isdir(args.target):
        sys.exit("target must be a directory with claims.jsonl")
    report = inspect(args.target, args.fetch)
    if args.suppress:
        suppress.apply_file(report, args.suppress)
    if args.baseline:
        report.suppress(load_report(args.baseline))
    print(report.to_json() if args.json else report_render.render_markdown(report, "evidence"))
    if args.out:
        fileio.write_json(args.out + ".json", report.to_dict())
        fileio.write_text(args.out + ".md", report_render.render_markdown(report, "evidence") + "\n")
    raise SystemExit(0 if report.meta.get("claims") else 1)


if __name__ == "__main__":
    main()
