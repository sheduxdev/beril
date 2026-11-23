import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import sbom


def make_tree(tmp_path, license_value="MIT", version="4.17.20"):
    lock = {
        "packages": {
            "": {"name": "app", "version": "1.0.0"},
            "node_modules/lodash": {"version": version},
        }
    }
    (tmp_path / "package-lock.json").write_text(json.dumps(lock))
    pkg = tmp_path / "node_modules" / "lodash"
    pkg.mkdir(parents=True)
    (pkg / "package.json").write_text(json.dumps({"name": "lodash", "version": version, "license": license_value}))
    return pkg / "package.json"


def test_component_has_hash_and_license(tmp_path):
    artifact = make_tree(tmp_path)
    doc = sbom.build(str(tmp_path))
    component = doc["components"][0]
    assert component["licenses"] == [{"license": {"id": "MIT"}}]
    expected = hashlib.sha256(artifact.read_bytes()).hexdigest()
    assert component["hashes"] == [{"alg": "SHA-256", "content": expected}]
    assert component["bom-ref"] == component["purl"]
    assert component["properties"][0]["name"] == "beril:manifest"


def test_non_spdx_license_becomes_expression(tmp_path):
    make_tree(tmp_path, license_value="SEE LICENSE IN LICENSE.md")
    doc = sbom.build(str(tmp_path))
    assert doc["components"][0]["licenses"] == [{"expression": "SEE LICENSE IN LICENSE.md"}]


def test_unvendored_component_has_no_hash(tmp_path):
    (tmp_path / "requirements.txt").write_text("requests==2.31.0\n")
    doc = sbom.build(str(tmp_path))
    assert "hashes" not in doc["components"][0]
    assert "licenses" not in doc["components"][0]


def test_spdx_document_shape(tmp_path):
    make_tree(tmp_path)
    doc = sbom.build(str(tmp_path))
    spdx = sbom.build_spdx(str(tmp_path), doc)
    assert spdx["spdxVersion"] == "SPDX-2.3"
    assert spdx["dataLicense"] == "CC0-1.0"
    assert spdx["SPDXID"] == "SPDXRef-DOCUMENT"
    refs = [p["SPDXID"] for p in spdx["packages"]]
    assert len(refs) == len(set(refs)) == 2
    package = spdx["packages"][1]
    assert package["versionInfo"] == "4.17.20"
    assert package["licenseDeclared"] == "MIT"
    assert package["checksums"][0]["algorithm"] == "SHA256"
    assert package["externalRefs"][0]["referenceLocator"].startswith("pkg:npm/lodash@")
    kinds = {r["relationshipType"] for r in spdx["relationships"]}
    assert kinds == {"DESCRIBES", "DEPENDS_ON"}


def test_vex_marks_offline_hit(tmp_path):
    make_tree(tmp_path)
    doc = sbom.build(str(tmp_path))
    hits = [{"name": "lodash", "version": "4.17.20", "id": "CVE-2021-23337", "fixed": "4.17.21"}]
    vex = sbom.build_vex(doc, hits)
    assert vex["@context"] == "https://openvex.dev/ns/v0.2.0"
    statement = vex["statements"][0]
    assert statement["status"] == "affected"
    assert statement["vulnerability"]["name"] == "CVE-2021-23337"
    assert statement["products"][0]["@id"] == "pkg:npm/lodash@4.17.20"
    assert "4.17.21" in statement["action_statement"]


def test_vex_without_hits_is_empty(tmp_path):
    make_tree(tmp_path)
    vex = sbom.build_vex(sbom.build(str(tmp_path)), [])
    assert vex["statements"] == []


def test_vex_skips_unknown_product(tmp_path):
    make_tree(tmp_path)
    vex = sbom.build_vex(sbom.build(str(tmp_path)), [{"name": "other", "version": "1.0", "id": "CVE-1"}])
    assert vex["statements"] == []


def test_cli_writes_all_three_formats(tmp_path, monkeypatch):
    make_tree(tmp_path)
    out = tmp_path / "out.cdx.json"
    spdx = tmp_path / "out.spdx.json"
    vex = tmp_path / "out.vex.json"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "sbom.py",
            "--target",
            str(tmp_path),
            "--out",
            str(out),
            "--spdx",
            str(spdx),
            "--vex",
            str(vex),
        ],
    )
    sbom.main()
    assert out.exists() and spdx.exists() and vex.exists()
    assert json.loads(vex.read_text())["statements"][0]["vulnerability"]["name"] == "CVE-2021-23337"
