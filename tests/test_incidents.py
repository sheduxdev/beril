import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import incidents


def test_every_case_passes_its_own_lab():
    cases = incidents.load()
    assert len(cases) >= 5
    for case in cases:
        report = incidents.evaluate(case)
        assert report.meta["passed"] is True, case["id"]


def test_lab_files_are_written(tmp_path, monkeypatch):
    monkeypatch.setattr(incidents, "LAB_DIR", str(tmp_path))
    case = incidents.find("log4shell")
    assert case
    log, noise = incidents.write_lab(case)
    assert Path(log).exists() and Path(noise).exists()
    assert "jndi" in Path(log).read_text()


def test_incident_rules_are_in_the_scanner():
    import source_audit

    checks = {f.check for f in source_audit.scan_text("x.log", "${jndi:ldap://x/y}", "")}
    assert "src.incident-log4shell" in checks


def test_case_has_all_required_fields():
    for case in incidents.load():
        for field in ("id", "source", "event", "root_cause", "detection", "fix", "rule"):
            assert case.get(field), (case["id"], field)
        assert case["source"].startswith("https://")
