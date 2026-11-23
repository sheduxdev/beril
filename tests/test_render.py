import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import report_render
from beril_model import Finding, Report


def report():
    r = Report(target="https://a.test", mode="active", profile="engineer")
    r.authorization = {"method": "dns", "evidence": "TXT matched", "verified_at": "2026-11-22T10:00:00+00:00"}
    r.scope["checked"] = ["headers"]
    r.scope["not_checked"] = ["auth flows"]
    r.add(
        Finding(
            check="web.header.csp",
            title="CSP missing",
            severity="high",
            confidence="high",
            evidence="https://a.test: header missing",
            impact="XSS impact grows",
            fix="Add CSP",
            subject="https://a.test",
            cwe=["CWE-693"],
            request="GET / HTTP/1.1",
            response="HTTP 200",
        )
    )
    r.add(
        Finding(
            check="web.tls.expiry",
            title="Certificate expiring",
            severity="medium",
            confidence="high",
            evidence="12 days",
            impact="outage",
            fix="renew",
            subject="https://a.test",
        )
    )
    r.finish()
    return r


def test_engineer_has_actions_scope_and_evidence():
    text = report_render.render_markdown(report(), "engineer")
    assert "## Fix now" in text
    assert "Checks attempted" in text
    assert "Checks not attempted" in text
    assert "Add CSP" in text
    assert "```http" in text


def test_smb_has_kvkk_note():
    text = report_render.render_markdown(report(), "smb")
    assert "Do today" in text
    assert "KVKK" in text
    assert "72 hours" in text
    assert "RED" in text


def test_bugbounty_has_cwe_cvss_sections():
    text = report_render.render_markdown(report(), "bugbounty")
    assert "## Findings" in text
    assert "CWE" in text


def test_maintainer_profile():
    text = report_render.render_markdown(report(), "maintainer")
    assert "Security report" in text
    assert "Coordinated disclosure" in text


def test_sarif_is_valid_shape():
    doc = json.loads(report_render.render_sarif(report()))
    assert doc["version"] == "2.1.0"
    run = doc["runs"][0]
    assert run["tool"]["driver"]["name"] == "Beril"
    assert run["results"][0]["ruleId"] == "web.header.csp"
    assert run["results"][0]["partialFingerprints"]
    assert run["results"][0]["locations"][0]["physicalLocation"]["artifactLocation"]["uri"] == "https://a.test"


def test_empty_report_is_honest():
    text = report_render.render_markdown(Report(target="https://a.test"), "engineer")
    assert "not a certificate" in text
    assert "Checks not attempted" in text


def test_cra_profile_has_articles_and_timeline():
    report = Report(target="pkg", mode="source")
    report.meta.update({"product": "Widget", "version": "1.2.3", "contact": "sec@x"})
    report.add(
        Finding(
            check="src.x",
            title="XSS",
            severity="high",
            confidence="high",
            evidence="a.py:1",
            impact="runs",
            fix="encode",
            cwe=["CWE-79"],
        )
    )
    report.finish()
    text = report_render.render_markdown(report, "cra")
    assert "CRA vulnerability report" in text
    assert "| 14 |" in text
    assert "| Found | TBD |" in text


def test_maintainer_profile_has_product_block():
    report = Report(target="pkg")
    report.meta.update({"product": "Widget", "version": "1.0"})
    text = report_render.render_markdown(report, "maintainer")
    assert "Product: Widget" in text
