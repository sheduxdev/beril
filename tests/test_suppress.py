import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import suppress
from beril_model import Finding, Report


def report_with(*findings):
    report = Report(target="https://a.test")
    for finding in findings:
        report.add(finding)
    report.finish()
    return report


def test_rule_suppresses_and_counts(tmp_path):
    path = tmp_path / ".berilignore"
    path.write_text(json.dumps({"check": "secret.*", "subject": "src/*", "reason": "test key"}) + "\n")
    report = report_with(
        Finding(
            check="secret.aws",
            title="t",
            severity="high",
            confidence="high",
            evidence="src/a.py:1",
            impact="i",
            fix="f",
        )
    )
    assert suppress.apply_file(report, str(path)) == 1
    assert report.findings == []
    assert report.meta["suppressed"] == 1


def test_subject_must_match(tmp_path):
    path = tmp_path / ".berilignore"
    path.write_text(json.dumps({"check": "secret.*", "subject": "other/*"}) + "\n")
    report = report_with(
        Finding(
            check="secret.aws",
            title="t",
            severity="high",
            confidence="high",
            evidence="src/a.py:1",
            impact="i",
            fix="f",
        )
    )
    assert suppress.apply_file(report, str(path)) == 0


def test_expired_rule_is_ignored():
    rule = {"check": "x", "expires": "2020-01-01"}
    finding = Finding(check="x", title="t", severity="low", confidence="low", evidence="e", impact="i", fix="f")
    assert suppress.expired(rule)
    assert not suppress.matches(rule, finding)


def test_bad_lines_and_missing_file(tmp_path):
    path = tmp_path / ".berilignore"
    path.write_text("# comment\nnot json\n" + json.dumps({"check": "x"}) + "\n")
    assert len(suppress.load(str(path))) == 1
    assert suppress.apply_file(Report(target="x"), str(tmp_path / "nope")) == 0


def test_exact_id_matches():
    finding = Finding(check="x", title="t", severity="low", confidence="low", evidence="e", impact="i", fix="f")
    assert suppress.matches({"id": finding.id}, finding)
