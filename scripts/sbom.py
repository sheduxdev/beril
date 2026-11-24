#!/usr/bin/env python3
"""Minimal CycloneDX 1.5 SBOM and license inventory.

This is not a certified SCA product. It exists so a review has a component
list and a license column instead of guesses. Versions come from lockfiles.

    python scripts/sbom.py --target ./repo --out sbom.cdx.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import uuid

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deps
import fileio
from beril_model import TOOL_VERSION

LICENSE_FILES = ("LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING")
PURL_TYPE = {
    "npm": "npm",
    "pypi": "pypi",
    "go": "golang",
    "cargo": "cargo",
    "composer": "composer",
    "rubygems": "gem",
    "maven": "maven",
}
SPDX_IDS = {
    "MIT",
    "Apache-2.0",
    "BSD-2-Clause",
    "BSD-3-Clause",
    "GPL-2.0-only",
    "GPL-3.0-only",
    "LGPL-2.1-only",
    "LGPL-3.0-only",
    "MPL-2.0",
    "ISC",
    "Unlicense",
    "CC0-1.0",
    "0BSD",
}


def declared_license(root: str) -> str:
    for name in LICENSE_FILES:
        path = os.path.join(root, name)
        if os.path.isfile(path):
            try:
                head = fileio.read_text(path, 600).lower()
            except OSError:
                continue
            for key, value in (
                ("mit", "MIT"),
                ("apache", "Apache-2.0"),
                ("bsd", "BSD"),
                ("gpl", "GPL"),
                ("mpl", "MPL-2.0"),
                ("unlicense", "Unlicense"),
            ):
                if key in head:
                    return value
    return ""


def package_licenses(root: str) -> dict[str, str]:
    found = {}
    skip = deps.SKIP - {"node_modules"}
    for seen_dirs, (dirpath, dirnames, filenames) in enumerate(os.walk(root)):
        dirnames[:] = [d for d in dirnames if d not in skip]
        if seen_dirs > 5_000:
            break
        if "package.json" in filenames:
            try:
                data = fileio.load_json(os.path.join(dirpath, "package.json"), {})
                if isinstance(data.get("license"), str):
                    found[data.get("name", "")] = data["license"]
            except (OSError, json.JSONDecodeError):
                pass
        if "pyproject.toml" in filenames:
            try:
                text = fileio.read_text(os.path.join(dirpath, "pyproject.toml"))
                match = re.search(r'license\s*=\s*["\']([^"\']+)', text)
                if match:
                    found[os.path.basename(dirpath)] = match.group(1)
            except OSError:
                pass
    return found


def purl_of(name: str, version: str, eco: str) -> str:
    return f"pkg:{PURL_TYPE.get(eco, eco)}/{name}@{version}"


def sha256_file(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65_536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def local_artifact(manifest: str, name: str, eco: str) -> str:
    """Find a vendored copy of a component next to its manifest."""
    base = os.path.dirname(manifest)
    candidates = []
    if eco == "npm":
        candidates = [os.path.join(base, "node_modules", *name.split("/"), "package.json")]
    elif eco == "composer":
        candidates = [os.path.join(base, "vendor", name, "composer.json")]
    elif eco == "go":
        candidates = [os.path.join(base, "vendor", name, "go.mod")]
    for candidate in candidates:
        if os.path.isfile(candidate):
            return candidate
    return ""


def build(root: str) -> dict:
    components = deps.collect(root)
    licenses = package_licenses(root)
    project = os.path.basename(os.path.abspath(root)) or "project"
    out_components = []
    seen = set()
    for name, version, eco, path, _line in components:
        key = (name, version, eco)
        if key in seen:
            continue
        seen.add(key)
        purl = purl_of(name, version, eco)
        component = {
            "type": "library",
            "bom-ref": purl,
            "name": name,
            "version": version,
            "purl": purl,
            "scope": "required",
            "properties": [{"name": "beril:manifest", "value": path}],
        }
        artifact = local_artifact(path, name, eco)
        if artifact:
            try:
                component["hashes"] = [{"alg": "SHA-256", "content": sha256_file(artifact)}]
            except OSError:
                pass
        license_value = licenses.get(name)
        if license_value:
            if license_value in SPDX_IDS:
                component["licenses"] = [{"license": {"id": license_value}}]
            else:
                component["licenses"] = [{"license": {"name": license_value}}]
        out_components.append(component)
    return {
        "bomFormat": "CycloneDX",
        "specVersion": "1.5",
        "serialNumber": "urn:uuid:" + str(uuid.uuid4()),
        "version": 1,
        "metadata": {
            "timestamp": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
            "tools": [{"name": "beril", "version": TOOL_VERSION}],
            "component": {
                "type": "application",
                "name": project,
                **({"licenses": [{"license": {"name": declared_license(root)}}]} if declared_license(root) else {}),
            },
        },
        "components": out_components,
    }


def spdx_ref(index: int, name: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9.-]+", "-", name).strip("-") or "component"
    return f"SPDXRef-Package-{index}-{slug}"


def build_spdx(root: str, sbom: dict) -> dict:
    """Render an SPDX 2.3 document from the CycloneDX component list."""
    project = os.path.basename(os.path.abspath(root)) or "project"
    root_license = declared_license(root) or "NOASSERTION"
    created = dt.datetime.now(dt.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    packages = [
        {
            "SPDXID": "SPDXRef-Package-root",
            "name": project,
            "versionInfo": "0.0.0",
            "downloadLocation": "NOASSERTION",
            "filesAnalyzed": False,
            "licenseConcluded": root_license,
            "licenseDeclared": root_license,
            "primaryPackagePurpose": "APPLICATION",
        }
    ]
    relationships = [
        {
            "spdxElementId": "SPDXRef-DOCUMENT",
            "relationshipType": "DESCRIBES",
            "relatedSpdxElement": "SPDXRef-Package-root",
        }
    ]
    for index, component in enumerate(sbom["components"]):
        ref = spdx_ref(index, component["name"])
        package = {
            "SPDXID": ref,
            "name": component["name"],
            "versionInfo": component.get("version", ""),
            "downloadLocation": "NOASSERTION",
            "filesAnalyzed": False,
            "licenseConcluded": "NOASSERTION",
            "licenseDeclared": "NOASSERTION",
            "externalRefs": [
                {
                    "referenceCategory": "PACKAGE-MANAGER",
                    "referenceType": "purl",
                    "referenceLocator": component["purl"],
                }
            ],
        }
        licenses = component.get("licenses") or []
        if licenses:
            value = licenses[0].get("license", {}).get("id") or licenses[0].get("expression", "")
            if value:
                package["licenseDeclared"] = value
                package["licenseConcluded"] = value
        for hashed in component.get("hashes") or []:
            package.setdefault("checksums", []).append({"algorithm": "SHA256", "checksumValue": hashed["content"]})
        packages.append(package)
        relationships.append(
            {"spdxElementId": "SPDXRef-Package-root", "relationshipType": "DEPENDS_ON", "relatedSpdxElement": ref}
        )
    return {
        "spdxVersion": "SPDX-2.3",
        "dataLicense": "CC0-1.0",
        "SPDXID": "SPDXRef-DOCUMENT",
        "name": f"{project} SBOM",
        "documentNamespace": f"https://beril.local/spdx/{uuid.uuid4()}",
        "creationInfo": {"created": created, "creators": [f"Tool: beril-{TOOL_VERSION}"]},
        "packages": packages,
        "relationships": relationships,
    }


def build_vex(sbom: dict, hits: list[dict]) -> dict:
    """Render an OpenVEX document from offline OSV hits."""
    purls = {(component["name"], component.get("version")): component["purl"] for component in sbom["components"]}
    statements = {}
    for hit in hits:
        purl = purls.get((hit.get("name"), hit.get("version")))
        if not purl:
            continue
        vuln = hit.get("id", "")
        statement = statements.setdefault(
            vuln,
            {
                "vulnerability": {"name": vuln},
                "products": [],
                "status": "affected",
                "action_statement": f"Upgrade to {hit.get('fixed') or 'a fixed version'} or later.",
            },
        )
        if purl not in statement["products"]:
            statement["products"].append({"@id": purl})
    return {
        "@context": "https://openvex.dev/ns/v0.2.0",
        "@id": f"https://beril.local/vex/{uuid.uuid4()}",
        "author": "Beril",
        "timestamp": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "version": 1,
        "tooling": f"beril-{TOOL_VERSION}",
        "statements": list(statements.values()),
    }


def license_table(sbom: dict) -> str:
    lines = ["# License inventory", "", "| Component | Version | License |", "|---|---|---|"]
    unknown = 0
    for component in sbom["components"]:
        lic = ", ".join(x["license"]["id"] for x in component.get("licenses", [])) or "bilinmiyor"
        if lic == "bilinmiyor":
            unknown += 1
        lines.append(f"| {component['name']} | {component['version']} | {lic} |")
    lines += [
        "",
        f"{len(sbom['components'])} components, {unknown} with an unknown license.",
        "Unknown licenses need legal review. This table is not legal advice.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--out", default="sbom.cdx.json")
    ap.add_argument("--spdx", default="", help="also write SPDX 2.3 JSON")
    ap.add_argument("--vex", default="", help="also write OpenVEX JSON from offline OSV hits")
    ap.add_argument("--licenses", default="")
    args = ap.parse_args()
    if not os.path.isdir(args.target):
        sys.exit("target must be a directory")
    sbom = build(args.target)
    fileio.write_json(args.out, sbom)
    print(f"wrote {len(sbom['components'])} components: {args.out}")
    if args.spdx:
        fileio.write_json(args.spdx, build_spdx(args.target, sbom))
        print(f"SPDX: {args.spdx}")
    if args.vex:
        hits = deps.offline_hits(deps.collect(args.target))
        fileio.write_json(args.vex, build_vex(sbom, hits))
        print(f"OpenVEX: {args.vex} ({len(hits)} offline hits)")
    if args.licenses:
        fileio.write_text(args.licenses, license_table(sbom) + "\n")
        print(f"license table: {args.licenses}")


if __name__ == "__main__":
    main()
