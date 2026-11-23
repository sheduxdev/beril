import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import adapters


def test_nuclei_line():
    line = json.dumps(
        {
            "template-id": "CVE-2024-1",
            "matched-at": "https://a.test/x",
            "info": {"name": "Test CVE", "severity": "high", "description": "x"},
        }
    )
    findings = adapters.parse_nuclei(line)
    assert findings
    assert findings[0].severity == "high"
    assert findings[0].check.startswith("tool.nuclei.")


def test_trivy_vuln_and_secret():
    payload = json.dumps(
        {
            "Results": [
                {
                    "Target": "app",
                    "Vulnerabilities": [
                        {
                            "VulnerabilityID": "CVE-2024-2",
                            "PkgName": "lodash",
                            "InstalledVersion": "4.17.20",
                            "Severity": "high",
                        }
                    ],
                    "Secrets": [{"Title": "AWS", "StartLine": 3, "Match": "AKIA"}],
                }
            ]
        }
    )
    findings = adapters.parse_trivy(payload)
    assert {f.check.split(".")[1] for f in findings} >= {"trivy"}


def test_gitleaks_json():
    payload = json.dumps([{"RuleID": "aws", "File": "a.py", "StartLine": 3}])
    assert adapters.parse_gitleaks(payload)[0].severity == "high"


def test_severity_map():
    assert adapters.SEVERITY_MAP["error"] == "high"
    assert adapters.SEVERITY_MAP["warning"] == "medium"


def test_build_args_nuclei_headers():
    args = adapters.build_args("nuclei", "https://a.test", {"Authorization": "Bearer x"}, False)
    assert "Authorization: Bearer x" in args


ZAP = json.dumps(
    {
        "site": [
            {
                "@name": "https://a.test",
                "alerts": [
                    {
                        "pluginid": "10038",
                        "alert": "CSP Header Not Set",
                        "riskcode": "2",
                        "confidence": "3",
                        "desc": "<p>No CSP.</p>",
                        "solution": "<p>Add one.</p>",
                        "cweid": "693",
                        "instances": [{"uri": "https://a.test/x", "method": "GET", "evidence": "<script>"}],
                    }
                ],
            }
        ]
    }
)


def test_zap_maps_to_schema():
    findings = adapters.parse_zap(ZAP)
    finding = findings[0]
    assert finding.severity == "medium"
    assert finding.confidence == "high"
    assert finding.check == "tool.zap.10038"
    assert finding.subject == "https://a.test/x"
    assert finding.cwe == ["CWE-693"]
    assert "<" not in finding.impact
    assert adapters.validate_findings(findings) == []


def test_zap_bad_json_is_empty():
    assert adapters.parse_zap("not json") == []


def test_every_parser_output_is_schema_valid():
    samples = {
        "nuclei": json.dumps(
            {"template-id": "CVE-2024-1", "matched-at": "https://a.test", "info": {"name": "x", "severity": "high"}}
        ),
        "semgrep": json.dumps(
            {
                "results": [
                    {
                        "check_id": "r.x",
                        "path": "a.py",
                        "start": {"line": 1},
                        "extra": {"severity": "medium", "message": "m"},
                    }
                ]
            }
        ),
        "trivy": json.dumps(
            {
                "Results": [
                    {
                        "Target": "app",
                        "Vulnerabilities": [{"VulnerabilityID": "CVE-1", "PkgName": "p", "InstalledVersion": "1"}],
                    }
                ]
            }
        ),
        "gitleaks": json.dumps([{"RuleID": "aws", "File": "a.py", "StartLine": 1}]),
        "grype": json.dumps({"matches": [{"vulnerability": {"id": "CVE-2"}, "artifact": {"name": "p"}}]}),
        "zap": ZAP,
    }
    for name, payload in samples.items():
        findings = adapters.PARSERS[name](payload)
        assert findings, name
        assert adapters.validate_findings(findings) == [], name
