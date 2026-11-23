import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import report_render
import sarif_schema
from beril_model import Finding, Report


def valid_doc() -> dict:
    return {
        "$schema": sarif_schema.SCHEMA_URL,
        "version": "2.1.0",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "Beril",
                        "rules": [
                            {
                                "id": "web.header.csp",
                                "shortDescription": {"text": "CSP"},
                                "fullDescription": {"text": "impact"},
                                "defaultConfiguration": {"level": "warning"},
                            }
                        ],
                    }
                },
                "results": [
                    {
                        "ruleId": "web.header.csp",
                        "ruleIndex": 0,
                        "level": "warning",
                        "message": {"text": "missing"},
                        "locations": [
                            {
                                "physicalLocation": {
                                    "artifactLocation": {"uri": "https://a.test"},
                                    "region": {"startLine": 1},
                                }
                            }
                        ],
                        "partialFingerprints": {"beril/v1": "abc"},
                    }
                ],
                "invocations": [
                    {
                        "executionSuccessful": True,
                        "startTimeUtc": "2026-01-01T00:00:00+00:00",
                        "endTimeUtc": "2026-01-01T00:00:01+00:00",
                    }
                ],
            }
        ],
    }


def test_valid_document_passes():
    assert sarif_schema.validate(valid_doc()) == []


def test_version_is_required():
    doc = valid_doc()
    doc["version"] = "2.0.0"
    assert any("version" in error for error in sarif_schema.validate(doc))


def test_driver_name_is_required():
    doc = valid_doc()
    del doc["runs"][0]["tool"]["driver"]["name"]
    assert any("driver.name" in error for error in sarif_schema.validate(doc))


def test_duplicate_rule_fails():
    doc = valid_doc()
    doc["runs"][0]["tool"]["driver"]["rules"].append(
        {"id": "web.header.csp", "shortDescription": {"text": "x"}, "fullDescription": {"text": "y"}}
    )
    assert any("duplicate" in error for error in sarif_schema.validate(doc))


def test_unknown_rule_and_bad_level_fail():
    doc = valid_doc()
    doc["runs"][0]["results"][0]["ruleId"] = "nope"
    doc["runs"][0]["results"][0]["level"] = "severe"
    errors = sarif_schema.validate(doc)
    assert any("unknown rule" in error for error in errors)
    assert any("unknown level" in error for error in errors)


def test_rule_index_out_of_range_fails():
    doc = valid_doc()
    doc["runs"][0]["results"][0]["ruleIndex"] = 7
    assert any("out of range" in error for error in sarif_schema.validate(doc))


def test_message_required_and_fingerprint_types():
    doc = valid_doc()
    doc["runs"][0]["results"][0]["message"] = {}
    doc["runs"][0]["results"][0]["partialFingerprints"] = {"a": 1}
    errors = sarif_schema.validate(doc)
    assert any("message.text" in error for error in errors)
    assert any("strings" in error for error in errors)


def test_bad_invocation_timestamp_and_bool():
    doc = valid_doc()
    doc["runs"][0]["invocations"][0] = {"executionSuccessful": "yes", "startTimeUtc": "yesterday"}
    errors = sarif_schema.validate(doc)
    assert any("executionSuccessful" in error for error in errors)
    assert any("RFC 3339" in error for error in errors)


def test_ensure_raises():
    with pytest.raises(ValueError):
        sarif_schema.ensure({"version": "1.0", "runs": []})


def test_render_output_is_valid():
    report = Report(target="https://a.test")
    report.add(
        Finding(
            check="web.header.csp",
            title="CSP missing",
            severity="medium",
            confidence="high",
            evidence="https://a.test",
            impact="Clickjacking",
            fix="Add CSP",
        )
    )
    report.finish()
    doc = json.loads(report_render.render_sarif(report))
    assert sarif_schema.validate(doc) == []


def test_render_matches_official_schema():
    jsonschema = pytest.importorskip("jsonschema")
    schema_path = Path(__file__).resolve().parents[1] / "references" / "sarif-2.1.0.schema.json"
    schema = json.loads(schema_path.read_text())
    report = Report(target="https://a.test")
    report.add(
        Finding(
            check="web.header.csp",
            title="CSP missing",
            severity="medium",
            confidence="high",
            evidence="https://a.test",
            impact="Clickjacking",
            fix="Add CSP",
        )
    )
    report.finish()
    doc = json.loads(report_render.render_sarif(report))
    jsonschema.validate(doc, schema)


def test_every_location_matches_schema():
    jsonschema = pytest.importorskip("jsonschema")
    schema_path = Path(__file__).resolve().parents[1] / "references" / "sarif-2.1.0.schema.json"
    schema = json.loads(schema_path.read_text())
    report = Report(target="https://a.test")
    report.add(
        Finding(
            check="source.xss",
            title="XSS",
            severity="low",
            confidence="low",
            evidence="src/app.py:12",
            impact="Script runs",
            fix="Escape",
        )
    )
    report.finish()
    jsonschema.validate(json.loads(report_render.render_sarif(report)), schema)


def test_official_schema_catches_missing_required():
    pytest.importorskip("jsonschema")
    assert sarif_schema.official_errors(valid_doc()) == []
    errors = sarif_schema.official_errors({"version": "2.1.0", "runs": [{}]})
    assert errors
