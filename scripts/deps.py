#!/usr/bin/env python3
"""Dependency inventory, offline OSV seed match, optional OSV API and reachability.

The point is signal: a vulnerable package that is never imported is a lower
priority than one on the request path. Reachability here is a grep, not a call
graph, and says so.

    python scripts/deps.py --target ./repo --reachability
    python scripts/deps.py --target ./repo --online --out scans/deps
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

import fileio
import paths
import suppress

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import feeds
import priority
from beril_model import Finding, Report

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SKIP = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".next", "coverage"}
ECOSYSTEM = {
    "npm": "npm",
    "pypi": "PyPI",
    "go": "Go",
    "cargo": "crates.io",
    "composer": "Packagist",
    "rubygems": "RubyGems",
    "maven": "Maven",
}

IMPORT_PATTERNS = {
    "npm": re.compile(r"""(?:from\s+['"]([^'"]+)['"]|require\(\s*['"]([^'"]+)['"]\s*\))"""),
    "pypi": re.compile(r"^\s*(?:from|import)\s+([\w.]+)", re.M),
    "go": re.compile(r'"([\w./-]+)"'),
    "composer": re.compile(r"use\s+([\w\\]+)"),
    "rubygems": re.compile(r"^\s*require\s+['\"]([^'\"]+)", re.M),
}


def load_seed() -> dict:
    try:
        with open(os.path.join(paths.DATA, "osv_seed.json"), encoding="utf-8") as fh:
            return json.load(fh).get("packages", {})
    except (OSError, json.JSONDecodeError):
        return {}


def parse_requirements(path: str) -> list[tuple[str, str, str, int]]:
    out = []
    try:
        for i, line in enumerate(fileio.read_text(path).splitlines(), 1):
            line = line.split("#", 1)[0].strip()
            if not line or "==" not in line:
                continue
            name, _, version = line.partition("==")
            name = re.split(r"[\[; ]", name)[0].strip().lower()
            version = version.split(";", 1)[0].strip()
            if name and re.match(r"^[\d.]+", version):
                out.append((name, version, path, i))
    except OSError:
        pass
    return out


def parse_package_lock(path: str) -> list[tuple[str, str, str, int]]:
    out = []
    try:
        data = fileio.load_json(path, {})
    except OSError:
        return out
    packages = data.get("packages") if isinstance(data, dict) else None
    if isinstance(packages, dict):
        for key, meta in packages.items():
            if not key.startswith("node_modules/"):
                continue
            name = key.rsplit("node_modules/", 1)[-1]
            version = (meta or {}).get("version", "")
            if version:
                out.append((name, version, path, 0))
    deps = data.get("dependencies") if isinstance(data, dict) else None
    if isinstance(deps, dict):
        for name, meta in deps.items():
            version = (meta or {}).get("version", "")
            if version:
                out.append((name, version, path, 0))
    return out


def parse_generic(path: str, kind: str) -> list[tuple[str, str, str, int]]:
    out = []
    try:
        lines = fileio.read_text(path).splitlines()
    except OSError:
        return out
    for i, line in enumerate(lines, 1):
        if kind == "go" and line.strip().startswith("require"):
            match = re.search(r"([\w./-]+)\s+v([\d.]+)", line)
            if match:
                out.append((match.group(1), match.group(2), path, i))
        elif kind == "go":
            match = re.match(r"\s*([\w./-]+)\s+v([\d.]+)", line)
            if match:
                out.append((match.group(1), match.group(2), path, i))
        elif kind == "cargo":
            if line.startswith("name = "):
                name = line.split("=", 1)[1].strip().strip('"')
                version = ""
                for follow in lines[i : i + 3]:
                    if follow.startswith("version = "):
                        version = follow.split("=", 1)[1].strip().strip('"')
                        break
                if name and version:
                    out.append((name, version, path, i))
        elif kind == "composer":
            match = re.match(r'\s*"([\w/-]+)"\s*:\s*"([^"]+)"', line)
            if match and "/" in match.group(1):
                out.append((match.group(1), match.group(2), path, i))
        elif kind == "rubygems":
            match = re.match(r"^ {4}([\w-]+) \(([\d.]+)\)", line)
            if match:
                out.append((match.group(1), match.group(2), path, i))
        elif kind == "maven":
            art = re.search(r"<artifactId>([\w.-]+)</artifactId>", line)
            if art:
                block = "\n".join(lines[i - 2 : i + 4])
                ver = re.search(r"<version>([\w.-]+)</version>", block)
                if ver:
                    out.append((art.group(1), ver.group(1), path, i))
    return out


def collect(root: str) -> list[tuple[str, str, str, str, int]]:
    found: list[tuple[str, str, str, str, int]] = []
    seen_files = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for name in filenames:
            seen_files += 1
            if seen_files > 50_000:
                return found
            path = os.path.join(dirpath, name)
            if name in ("package-lock.json", "npm-shrinkwrap.json"):
                for pkg in parse_package_lock(path):
                    found.append((pkg[0], pkg[1], "npm", pkg[2], pkg[3]))
            elif name in ("requirements.txt", "requirements-dev.txt", "constraints.txt"):
                for pkg in parse_requirements(path):
                    found.append((pkg[0], pkg[1], "pypi", pkg[2], pkg[3]))
            elif name == "go.mod":
                for pkg in parse_generic(path, "go"):
                    found.append((pkg[0], pkg[1], "go", pkg[2], pkg[3]))
            elif name == "Cargo.lock":
                for pkg in parse_generic(path, "cargo"):
                    found.append((pkg[0], pkg[1], "cargo", pkg[2], pkg[3]))
            elif name == "composer.lock":
                for pkg in parse_generic(path, "composer"):
                    found.append((pkg[0], pkg[1], "composer", pkg[2], pkg[3]))
            elif name == "Gemfile.lock":
                for pkg in parse_generic(path, "rubygems"):
                    found.append((pkg[0], pkg[1], "rubygems", pkg[2], pkg[3]))
            elif name == "pom.xml":
                for pkg in parse_generic(path, "maven"):
                    found.append((pkg[0], pkg[1], "maven", pkg[2], pkg[3]))
            elif name == "poetry.lock":
                for pkg in parse_generic(path, "cargo"):
                    found.append((pkg[0], pkg[1], "pypi", pkg[2], pkg[3]))
    # de-dupe
    seen = set()
    unique = []
    for item in found:
        key = (item[0].lower(), item[1], item[2])
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def version_lt(version: str, below: str) -> bool:
    def parts(value: str) -> tuple[int, ...]:
        nums = re.findall(r"\d+", value)
        return tuple(int(n) for n in nums[:4]) if nums else (0,)

    return parts(version) < parts(below)


def offline_hits(components: list[tuple]) -> list[dict]:
    seed = load_seed()
    hits = []
    for name, version, eco, path, line in components:
        table = seed.get(ECOSYSTEM.get(eco, eco), {})
        for pkg, ranges in table.items():
            if pkg.lower() != name.lower():
                continue
            for below, meta in ranges.items():
                if version_lt(version, below.lstrip("<")):
                    hits.append(
                        {"name": name, "version": version, "ecosystem": eco, "path": path, "line": line, **meta}
                    )
    return hits


def online_hits(components: list[tuple]) -> tuple[list[dict], str]:
    pairs = [(n, v, e, path, line) for n, v, e, path, line in components if ECOSYSTEM.get(e)]
    if not pairs:
        return [], "no components"
    results, errors, _marker = feeds.osv_query_many([(ECOSYSTEM[e], n, v) for n, v, e, _p, _line in pairs], online=True)
    out = []
    for component, vulns in zip(pairs, results, strict=False):
        for vuln in vulns[:3]:
            sev = "medium"
            score = None
            for rating in vuln.get("severity", []):
                if rating.get("type") == "CVSS_V3" and rating.get("score"):
                    try:
                        score = float(rating["score"].split("/")[0])
                    except ValueError:
                        pass
            if score:
                sev = "critical" if score >= 9 else "high" if score >= 7 else "medium" if score >= 4 else "low"
            out.append(
                {
                    "name": component[0],
                    "version": component[1],
                    "ecosystem": component[2],
                    "path": component[3],
                    "line": component[4],
                    "id": vuln.get("id", ""),
                    "summary": (vuln.get("summary") or vuln.get("details", ""))[:240],
                    "severity": sev,
                    "fixed": _fixed(vuln),
                    "cvss": score,
                }
            )
    return out, "; ".join(errors)


def _fixed(vuln: dict) -> str:
    for affected in vuln.get("affected", []):
        for rng in affected.get("ranges", []):
            for event in rng.get("events", []):
                if "fixed" in event:
                    return event["fixed"]
    return ""


def reachability(root: str, package: str, eco: str) -> str:
    pattern = IMPORT_PATTERNS.get(eco)
    if not pattern:
        return "unknown"
    needle = package.split("/")[-1].split(":")[-1].lower()
    seen = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for name in filenames:
            seen += 1
            if seen > 20_000:
                return "unknown"
            if os.path.splitext(name)[1] not in (
                ".py",
                ".js",
                ".jsx",
                ".ts",
                ".tsx",
                ".go",
                ".php",
                ".rb",
                ".java",
                ".kt",
            ):
                continue
            try:
                text = fileio.read_text(os.path.join(dirpath, name), 200_000)
            except OSError:
                continue
            for match in pattern.finditer(text):
                candidate = "".join(g or "" for g in match.groups()).lower()
                if needle and needle in candidate:
                    return "reachable"
    return "not-found"


def scan(target: str, online: bool = False, do_reach: bool = False) -> Report:
    report = Report(target=target, mode="source")
    report.scope["checked"] = ["Manifest and lockfile inventory", "Offline OSV seed match"]
    if online:
        report.scope["checked"].append("OSV API sorgusu")
    if do_reach:
        report.scope["checked"].append("Import based reachability grep")
    report.scope["not_checked"] = ["Full call graph", "All transitive dependencies", "Runtime use", "Lisans uyumu"]
    components = collect(target)
    report.meta["components"] = len(components)
    if not components:
        report.errors.append("could not build a dependency inventory (no supported lockfile)")
        return report.finish()
    hits = offline_hits(components)
    if online:
        extra, error = online_hits(components)
        if error:
            report.errors.append("OSV: " + error)
        hits += extra
    seen = set()
    for hit in hits:
        key = (hit["name"], hit.get("id"))
        if key in seen:
            continue
        seen.add(key)
        reach = reachability(target, hit["name"], hit["ecosystem"]) if do_reach else "unknown"
        confidence = "high" if not do_reach else ("medium" if reach == "reachable" else "low")
        enrich = priority.enrich(hit.get("id", ""))
        finding = Finding(
            check="dep." + (hit.get("id", "osv") or "osv").replace("-", ".").lower(),
            title=f"Known dependency issue: {hit['name']} {hit['version']}",
            severity=hit.get("severity", "medium"),
            confidence=confidence,
            evidence=f"{hit['path']}:{hit.get('line', 0)} {hit['name']}=={hit['version']} -> {hit.get('id', '')}",
            impact=hit.get("summary", "Bilinen zafiyet.") + f" (reachability: {reach})",
            fix=(
                f"Upgrade to {hit['fixed']} or later. "
                if hit.get("fixed")
                else "Confirm the upgrade version with the vendor. "
            )
            + "Check the API surface you use and quarantine the package if needed.",
            subject=f"{hit['name']}@{hit['version']}",
            source="dependency",
            cwe=["CWE-1104"],
            tags=["dependency", hit["ecosystem"]],
            false_positive=(
                "The package is not imported in the project (grep). It can still be used transitively."
                if reach == "not-found"
                else ""
            ),
        )
        finding.kev = bool(enrich.get("kev"))
        if enrich.get("epss") is not None:
            finding.epss = enrich["epss"]
        if hit.get("cvss") is not None:
            finding.cvss_score = hit["cvss"]
        report.add(finding)
    report.finish()
    return report


def render(report: Report) -> str:
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
    lines = [f"# Dependency scan: {report.target}", "", f"Matches: {len(report.findings)}.", ""]
    for f in sorted(report.findings, key=lambda x: order.get(x.severity, 9)):
        lines.append(f"- [{f.severity}/{f.confidence}] {f.title}: {f.evidence}")
        lines.append(f"  - {f.fix}")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--online", action="store_true")
    ap.add_argument("--reachability", action="store_true")
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--suppress", default="", help="JSON Lines ignore file")
    args = ap.parse_args()
    report = scan(args.target, args.online, args.reachability)
    if args.suppress:
        suppress.apply_file(report, args.suppress)
    print(report.to_json() if args.json else render(report))
    if args.out:
        fileio.write_json(args.out + ".json", json.loads(report.to_json()))
        fileio.write_text(args.out + ".md", render(report) + "\n")


if __name__ == "__main__":
    main()
