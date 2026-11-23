#!/usr/bin/env python3
"""Passive BGP posture lookup for a prefix or an ASN.

Uses public data only: RIPEstat for routing status and RPKI validation, and
links out to the Hurricane Electric BGP Toolkit and bgp.tools for a second view.
Nothing is announced and no router is touched.

    python scripts/bgp.py --prefix 203.0.113.0/24
    python scripts/bgp.py --asn AS64500 --json
"""

from __future__ import annotations

import argparse
import ipaddress
import json
import os
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import report_render
from beril_model import Finding, Report, load_report

BASE = "https://stat.ripe.net/data/{call}/data.json"
UA = "Beril/1.4 (passive BGP lookup; +https://github.com/sheduxdev/beril)"
TIMEOUT = 15
MAX_REQUESTS = 6


class Budget:
    """Tiny request budget for one lookup."""

    def __init__(self, limit: int = MAX_REQUESTS) -> None:
        self.limit = limit
        self.sent = 0

    def take(self) -> bool:
        if self.sent >= self.limit:
            return False
        self.sent += 1
        return True


def get_json(call: str, params: dict) -> tuple[dict, str]:
    """Fetch one RIPEstat call.

    Args:
        call: Data call name, such as ``prefix-overview``.
        params: Query parameters.

    Returns:
        Parsed payload and an error string. The payload is empty on failure.
    """
    url = BASE.format(call=call) + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return json.loads(response.read(500_000).decode("utf-8")), ""
    except Exception as exc:
        return {}, f"{type(exc).__name__}: {exc}"


def normalize_prefix(value: str) -> str:
    network = ipaddress.ip_network(value.strip(), strict=False)
    return str(network)


def normalize_asn(value: str) -> str:
    text = value.strip().upper().removeprefix("AS")
    if not text.isdigit():
        raise ValueError(f"bad ASN: {value}")
    return "AS" + text


def links(prefix: str = "", asn: str = "") -> list[Finding]:
    out = []
    if prefix:
        out.append(
            Finding(
                check="bgp.links",
                title="Second collector links",
                severity="info",
                confidence="high",
                evidence=(
                    f"https://bgp.he.net/net/{prefix} | "
                    f"https://bgp.tools/prefix/{prefix} | "
                    f"https://stat.ripe.net/{prefix}"
                ),
                impact="A single collector can be stale or filtered. Confirm on two.",
                fix="Open two links and compare origin, path and first seen.",
                subject=prefix,
                source="passive",
                tags=["bgp", "links"],
            )
        )
    if asn:
        out.append(
            Finding(
                check="bgp.links-asn",
                title="ASN contact links",
                severity="info",
                confidence="high",
                evidence=(
                    f"https://bgp.he.net/{asn} | https://bgp.tools/as/{asn.removeprefix('AS')} | "
                    f"https://www.peeringdb.com/asn/{asn.removeprefix('AS')}"
                ),
                impact="PeeringDB and the RIR hold the NOC and abuse contacts.",
                fix="Verify the contact before a routing incident.",
                subject=asn,
                source="passive",
                tags=["bgp", "contact"],
            )
        )
    return out


def lookup_prefix(prefix: str, budget: Budget) -> Report:
    report = Report(target=prefix, mode="passive", profile="engineer")
    report.scope["checked"] = [
        "RPKI validation state per origin ASN",
        "RIS routing status and visibility",
        "Prefix overview and origin ASNs",
        "Second collector links",
    ]
    report.scope["not_checked"] = [
        "Live router configuration",
        "IRR object quality",
        "PeeringDB contact accuracy",
        "Data plane path and latency",
    ]
    report.limits = {"max_requests": budget.limit, "sources": "RIPEstat, HE, bgp.tools links"}

    budget.take()
    overview, error = get_json("prefix-overview", {"resource": prefix})
    if error or overview.get("status") != "ok":
        report.errors.append(error or overview.get("status", "prefix-overview failed"))
        report.finish()
        return report
    data = overview.get("data", {})
    origins = [str(item.get("asn")) for item in data.get("asns", [])]
    report.meta["announced"] = bool(data.get("announced"))
    report.meta["origins"] = origins
    report.meta["holders"] = {str(item.get("asn")): item.get("holder", "") for item in data.get("asns", [])}

    if not data.get("announced"):
        report.add(
            Finding(
                check="bgp.not-announced",
                title="Prefix is not visible in RIS",
                severity="medium",
                confidence="medium",
                evidence=f"{prefix}: announced=false",
                impact="A planned prefix may be withdrawn, filtered or never announced.",
                fix="Check the border router and the upstream, then a second collector.",
                subject=prefix,
                source="passive",
                tags=["bgp"],
                false_positive="Very low visibility prefixes are excluded by RIS.",
            )
        )
    if len(origins) > 1:
        report.add(
            Finding(
                check="bgp.multi-origin",
                title="Multiple origin ASNs",
                severity="low",
                confidence="medium",
                evidence=f"{prefix}: origins {', '.join(origins)}",
                impact="Can be anycast or a hijack. RPKI state decides.",
                fix="Confirm each origin is authorized and covered by a ROA.",
                subject=prefix,
                source="passive",
                tags=["bgp"],
                false_positive="Anycast and multi-homing use several origins on purpose.",
            )
        )
    if data.get("related_prefixes"):
        report.meta["related_prefixes"] = data["related_prefixes"][:10]

    if budget.take():
        status, error = get_json("routing-status", {"resource": prefix})
        if status.get("status") == "ok":
            payload = status.get("data", {})
            first = payload.get("first_seen") or {}
            last = payload.get("last_seen") or {}
            report.meta["first_seen"] = first
            report.meta["last_seen"] = last
            visibility = payload.get("visibility", {}).get("v4", {})
            seen, total = visibility.get("ris_peers_seeing", 0), visibility.get("total_ris_peers", 0)
            report.meta["visibility"] = visibility
            if total and seen / total < 0.5:
                report.add(
                    Finding(
                        check="bgp.visibility.low",
                        title="Low RIS visibility",
                        severity="medium",
                        confidence="medium",
                        evidence=f"{prefix}: {seen}/{total} RIS peers see it",
                        impact="Partial visibility can mean a filter, a hijack or a broken session.",
                        fix="Compare with a second collector and the upstream.",
                        subject=prefix,
                        source="passive",
                        tags=["bgp"],
                        false_positive="A small or regional prefix can be legitimately sparse.",
                    )
                )
            if first.get("origin") and origins and first.get("origin") not in origins:
                report.add(
                    Finding(
                        check="bgp.origin-changed",
                        title="First seen origin differs from current origin",
                        severity="info",
                        confidence="medium",
                        evidence=f"first seen AS{first.get('origin')} at {first.get('time')}, now {', '.join(origins)}",
                        impact="An origin change can be a migration or a hijack.",
                        fix="Check the change record and the ROA history.",
                        subject=prefix,
                        source="passive",
                        tags=["bgp"],
                    )
                )

    for origin in origins:
        if not budget.take():
            break
        validation, error = get_json("rpki-validation", {"resource": f"AS{origin}", "prefix": prefix})
        if validation.get("status") != "ok":
            report.errors.append(error or f"rpki-validation failed for AS{origin}")
            continue
        rows = validation.get("data", {}).get("validating_roas", [])
        if not rows:
            continue
        states = {str(row.get("validity")) for row in rows}
        if "invalid" in states:
            report.add(
                Finding(
                    check="bgp.rpki.invalid",
                    title=f"RPKI invalid for AS{origin}",
                    severity="high",
                    confidence="high",
                    evidence=f"{prefix} origin AS{origin}: {rows}",
                    impact="A validating network should reject the route. Reachability depends on the rest of the path.",
                    fix="Fix the ROA or the origin AS, then re-check. Use a more specific only after confirmation.",
                    subject=prefix,
                    source="passive",
                    cwe=["CWE-345"],
                    tags=["bgp", "rpki"],
                    refs=[f"https://stat.ripe.net/{prefix}"],
                    false_positive="A stale validator or a mid-migration ROA can show invalid.",
                )
            )
        elif "not-found" in states:
            report.add(
                Finding(
                    check="bgp.rpki.not-found",
                    title=f"No covering ROA for AS{origin}",
                    severity="medium",
                    confidence="high",
                    evidence=f"{prefix} origin AS{origin}: {rows}",
                    impact="Validating networks accept it at lower preference, which makes a hijack easier.",
                    fix="Publish a ROA with the correct origin and maxLength.",
                    subject=prefix,
                    source="passive",
                    cwe=["CWE-345"],
                    tags=["bgp", "rpki"],
                )
            )
        else:
            report.meta.setdefault("rpki", {})[origin] = "valid"

    for finding in links(prefix=prefix):
        report.add(finding)
    report.finish()
    return report


def lookup_asn(asn: str, budget: Budget) -> Report:
    report = Report(target=asn, mode="passive", profile="engineer")
    report.scope["checked"] = ["AS overview", "Announced prefix count", "Contact links"]
    report.scope["not_checked"] = ["Announced prefix list quality", "IRR and ROA state per prefix", "Live sessions"]
    report.limits = {"max_requests": budget.limit, "sources": "RIPEstat, HE, bgp.tools, PeeringDB links"}
    budget.take()
    overview, error = get_json("as-overview", {"resource": asn})
    if error or overview.get("status") != "ok":
        report.errors.append(error or "as-overview failed")
        report.finish()
        return report
    data = overview.get("data", {})
    report.meta.update(
        {
            "holder": data.get("holder", ""),
            "announced": data.get("announced"),
            "type": data.get("type", ""),
            "announced_prefixes": data.get("announced_prefixes"),
        }
    )
    if budget.take():
        prefixes, error = get_json("announced-prefixes", {"resource": asn})
        if prefixes.get("status") == "ok":
            rows = prefixes.get("data", {}).get("prefixes", [])[:50]
            report.meta["sample_prefixes"] = rows
            if len(rows) >= 50:
                report.add(
                    Finding(
                        check="bgp.prefix-volume",
                        title="Large announcement count",
                        severity="info",
                        confidence="high",
                        evidence=f"{asn}: 50 or more prefixes in the sample",
                        impact="A large table needs max-prefix limits and filter automation.",
                        fix="Check max-prefix on every session and refresh filters daily.",
                        subject=asn,
                        source="passive",
                        tags=["bgp"],
                    )
                )
    for finding in links(asn=asn):
        report.add(finding)
    report.finish()
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prefix", default="")
    ap.add_argument("--asn", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", default="")
    ap.add_argument("--fail-on", default="none", choices=("none", "info", "low", "medium", "high", "critical"))
    ap.add_argument("--baseline", default="")
    args = ap.parse_args()
    if not args.prefix and not args.asn:
        sys.exit("give --prefix or --asn")
    budget = Budget()
    try:
        if args.prefix:
            report = lookup_prefix(normalize_prefix(args.prefix), budget)
        else:
            report = lookup_asn(normalize_asn(args.asn), budget)
    except ValueError as exc:
        sys.exit(str(exc))
    if args.baseline:
        report.suppress(load_report(args.baseline))
    text = report.to_json() if args.json else report_render.render_markdown(report, "engineer")
    print(text)
    if args.out:
        report.write_json(args.out + ".json")
        with open(args.out + ".md", "w", encoding="utf-8") as handle:
            handle.write(report_render.render_markdown(report, "engineer") + "\n")
        print(f"wrote {args.out}.md and {args.out}.json", file=sys.stderr)
    if args.fail_on != "none":
        raise SystemExit(report.exit_code(args.fail_on))


if __name__ == "__main__":
    main()
