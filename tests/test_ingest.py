import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import ingest


def test_sarif_maps_result():
    data = {
        "runs": [
            {
                "tool": {
                    "driver": {
                        "rules": [
                            {
                                "id": "R1",
                                "shortDescription": {"text": "Rule one"},
                                "fullDescription": {"text": "Impact"},
                                "help": {"text": "Fix it"},
                            }
                        ]
                    }
                },
                "results": [
                    {
                        "ruleId": "R1",
                        "level": "error",
                        "message": {"text": "hit"},
                        "locations": [
                            {"physicalLocation": {"artifactLocation": {"uri": "a.py"}, "region": {"startLine": 4}}}
                        ],
                    }
                ],
            }
        ]
    }
    findings = ingest.sarif_findings(data)
    assert findings[0].severity == "high"
    assert findings[0].subject == "a.py:4"


def test_generic_list():
    findings = ingest.generic_findings([{"check": "x", "title": "t", "severity": "low"}])
    assert findings[0].check == "import.x"


def test_zap_format():
    payload = json.dumps(
        {
            "site": [
                {
                    "@name": "https://a.test",
                    "alerts": [
                        {
                            "pluginid": "1",
                            "alert": "x",
                            "riskcode": "1",
                            "confidence": "2",
                            "instances": [{"uri": "https://a.test"}],
                        }
                    ],
                }
            ]
        }
    )
    findings = ingest.parse(payload, "zap")
    assert findings[0].severity == "low"
