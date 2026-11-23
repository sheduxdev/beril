#!/usr/bin/env python3
"""Audit exported network device and service config files.

Point it at a directory of saved configs: sshd_config, nftables, unbound,
nginx, HAProxy, Kubernetes network policy. Static only, no device login.

    ./beril netcheck --target ./configs/router
"""

from __future__ import annotations

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import report_render
import suppress
from beril_model import Finding, Report, load_report

RULES = [
    (
        "sshd",
        r"^\s*PermitRootLogin\s+yes",
        "high",
        "SSH root login enabled",
        "Set PermitRootLogin prohibit-password.",
        "CWE-306",
    ),
    (
        "sshd",
        r"^\s*PasswordAuthentication\s+yes",
        "medium",
        "SSH password auth enabled",
        "Prefer keys, keep passwords as fallback.",
        "CWE-521",
    ),
    (
        "sshd",
        r"^\s*PermitEmptyPasswords\s+yes",
        "medium",
        "SSH empty passwords allowed",
        "Set PermitEmptyPasswords no.",
        "CWE-258",
    ),
    ("sshd", r"^\s*X11Forwarding\s+yes", "info", "SSH X11 forwarding enabled", "Disable if unused.", "CWE-693"),
    ("sshd", r"^\s*PermitTunnel\s+yes", "low", "SSH tunneling allowed", "Confirm it is intended.", "CWE-693"),
    (
        "sshd",
        r"^\s*(?:Ciphers|MACs|KexAlgorithms).*(?:3des|sha1|diffie-hellman-group1)",
        "medium",
        "Legacy SSH algorithm",
        "Remove SHA1 and group1.",
        "CWE-326",
    ),
    (
        "nftables",
        r"^\s*policy\s+accept\s*;",
        "high",
        "Firewall chain defaults to accept",
        "Set policy drop on input and forward.",
        "CWE-284",
    ),
    (
        "nftables",
        r"^\s*tcp\s+dport\s+\{\s*22\s*\}",
        "info",
        "SSH open in firewall",
        "Restrict the source range.",
        "CWE-284",
    ),
    (
        "nftables",
        r"^\s*(?:ip|ip6)\s+saddr\s+0\.0\.0\.0/0|^\s*ip\s+saddr\s+0\.0\.0\.0/0",
        "medium",
        "Rule matches any source",
        "Restrict to known ranges.",
        "CWE-284",
    ),
    (
        "unbound",
        r"^\s*access-control:\s*0\.0\.0\.0/0\s+allow",
        "medium",
        "Recursive DNS open to all",
        "Restrict to client ranges.",
        "CWE-284",
    ),
    (
        "unbound",
        r"^\s*auto-trust-anchor-file",
        "info",
        "DNSSEC validation configured",
        "Good sign. Keep the anchor updated.",
        "",
    ),
    ("unbound", r"^\s*hide-identity:\s*no", "low", "DNS identity exposed", "Set hide-identity yes.", "CWE-200"),
    ("nginx", r"^\s*server_tokens\s+on\s*;", "low", "nginx version exposed", "Set server_tokens off.", "CWE-200"),
    (
        "nginx",
        r"ssl_protocols\s+[^;]*(?:TLSv1|TLSv1\.1)",
        "medium",
        "Old TLS enabled",
        "Allow TLS 1.2 and 1.3 only.",
        "CWE-326",
    ),
    ("nginx", r"add_header\s+Strict-Transport-Security", "info", "HSTS configured", "Keep it.", ""),
    ("haproxy", r"^\s*mode\s+tcp", "info", "TCP mode proxy", "TLS terminates elsewhere; confirm.", "CWE-319"),
    (
        "haproxy",
        r"^\s*ssl-server-verify\s+none",
        "medium",
        "Backend TLS not verified",
        "Set ssl-server-verify required.",
        "CWE-295",
    ),
    ("k8s", r"kind:\s*NetworkPolicy", "info", "Network policy present", "Keep policy coverage.", ""),
    ("k8s", r"ingress:\s*\\[\\s*\\]", "low", "Empty ingress rule", "Empty rules allow all.", "CWE-284"),
]

DEFAULT_NAMES = {"sshd_config", "nftables.conf", "unbound.conf", "nginx.conf", "haproxy.cfg"}


def classify(path: str, text: str) -> str:
    name = os.path.basename(path).lower()
    if "sshd" in name:
        return "sshd"
    if "nftables" in name or "iptables" in name:
        return "nftables"
    if "unbound" in name:
        return "unbound"
    if "nginx" in name:
        return "nginx"
    if "haproxy" in name:
        return "haproxy"
    if "networkpolicy" in name or "kind: NetworkPolicy" in text:
        return "k8s"
    return ""


def scan(target: str) -> Report:
    report = Report(target=target, mode="source")
    report.scope["checked"] = ["sshd", "nftables", "unbound", "nginx", "HAProxy", "Kubernetes policy", "line numbers"]
    report.scope["not_checked"] = [
        "Live device state",
        "Applied vs saved config",
        "Routing and switching config",
        "TLS certificate chain",
    ]
    if not os.path.isdir(target):
        report.errors.append("target must be a directory of exported configs")
        return report.finish()
    found = 0
    for dirpath, dirnames, filenames in os.walk(target):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules", "__pycache__"}]
        for name in filenames:
            path = os.path.join(dirpath, name)
            try:
                with open(path, encoding="utf-8", errors="replace") as handle:
                    text = handle.read(400_000)
            except OSError:
                continue
            kind = classify(path, text)
            if not kind:
                continue
            found += 1
            for rule_kind, pattern, severity, title, fix, cwe in RULES:
                if rule_kind != kind:
                    continue
                for match in re.finditer(pattern, text, re.M):
                    line = text[: match.start()].count("\n") + 1
                    slug = re.sub(r"\W+", "-", title).lower()[:50]
                    report.add(
                        Finding(
                            check=f"netcheck.{kind}.{slug}",
                            title=title,
                            severity=severity,
                            confidence="high",
                            evidence=f"{path}:{line} {match.group(0).strip()[:120]}",
                            impact="Config gap on the saved device state.",
                            fix=fix,
                            subject=f"{path}:{line}",
                            source="static",
                            cwe=[cwe] if cwe else [],
                            tags=["config"],
                            false_positive="The saved file may differ from the running config.",
                        )
                    )
    if not found:
        report.errors.append("no recognized config file")
    report.meta["config_files"] = found
    report.finish()
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument("--fail-on", default="none", choices=("none", "info", "low", "medium", "high", "critical"))
    ap.add_argument("--baseline", default="")
    ap.add_argument("--suppress", default="", help="JSON Lines ignore file")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    report = scan(args.target)
    if args.suppress:
        suppress.apply_file(report, args.suppress)
    if args.baseline:
        report.suppress(load_report(args.baseline))
    print(report.to_json() if args.json else report_render.render_markdown(report, "engineer"))
    if args.out:
        report.write_json(args.out + ".json")
        with open(args.out + ".md", "w", encoding="utf-8") as handle:
            handle.write(report_render.render_markdown(report, "engineer") + "\n")
    if args.fail_on != "none":
        raise SystemExit(report.exit_code(args.fail_on))


if __name__ == "__main__":
    main()
