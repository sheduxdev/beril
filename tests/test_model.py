import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from beril_model import Finding, Report, report_from_dict


def mk(check="web.header.csp", severity="high", confidence="high", subject="https://a.test/", **kw):
    evidence = kw.pop("evidence", "evidence")
    return Finding(
        check=check,
        title="t",
        severity=severity,
        confidence=confidence,
        evidence=evidence,
        impact="impact",
        fix="fix",
        subject=subject,
        **kw,
    )


def test_priority_orders_by_severity_and_confidence():
    report = Report(target="x")
    low = report.add(mk(severity="low", confidence="low", subject="a"))
    high = report.add(mk(severity="high", confidence="high", subject="b"))
    report.finish()
    assert report.findings[0].id == high.id
    assert high.priority() > low.priority()


def test_kev_and_epss_raise_priority():
    plain = mk(severity="medium", confidence="medium")
    enriched = mk(severity="medium", confidence="medium", kev=True, epss=0.9)
    assert enriched.priority() > plain.priority()
    assert "KEV" in enriched.priority_reason()


def test_dedupe_keeps_highest_confidence_and_merges_evidence():
    report = Report(target="x")
    first = report.add(mk(confidence="low", evidence="one"))
    report.add(mk(confidence="high", evidence="two"))
    assert len(report.findings) == 1
    assert report.findings[0].confidence == "high"
    assert "two" in report.findings[0].evidence
    assert first is report.findings[0]


def test_top_actions_capped_and_filtered():
    report = Report(target="x")
    for i in range(10):
        report.add(mk(severity="high", confidence="high", subject=f"https://a.test/{i}"))
    report.add(mk(severity="high", confidence="low", subject="https://a.test/low"))
    report.add(mk(severity="info", confidence="high", subject="https://a.test/info"))
    assert len(report.top_actions()) == 5
    assert all(f.confidence != "low" for f in report.top_actions())


def test_report_roundtrip():
    report = Report(target="https://a.test", mode="active")
    report.add(mk(cwe=["CWE-79"], tags=["xss"]))
    data = json.loads(report.to_json())
    back = report_from_dict(data)
    assert back.target == "https://a.test"
    assert back.findings[0].cwe == ["CWE-79"]
    assert back.findings[0].severity == "high"


def test_inferred_caps_high_confidence():
    finding = mk(confidence="high", state="inferred")
    assert finding.confidence == "medium"


def test_priority_reason_is_explainable():
    finding = mk()
    assert "base high" in finding.priority_reason()
    assert "confidence high" in finding.priority_reason()


def test_suppress_matches_id_and_fingerprint():
    base = Report(target="x")
    base.add(mk(check="a", subject="s1"))
    base.add(mk(check="b", subject="s2"))
    current = Report(target="x")
    current.add(mk(check="a", subject="s1"))
    current.add(mk(check="b", subject="s2", evidence="different"))
    current.add(mk(check="c", subject="s3"))
    removed = current.suppress(base)
    assert removed == 2
    assert current.meta["suppressed"] == 2
    assert [f.check for f in current.findings] == ["c"]


def test_exit_code_threshold():
    report = Report(target="x")
    report.add(mk(severity="medium"))
    assert report.exit_code("none") == 0
    assert report.exit_code("high") == 0
    assert report.exit_code("medium") == 1
    assert report.exit_code("info") == 1
