import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import bgp


def fake(payloads):
    def get(call, params):
        return payloads.get(call, ({}, "missing")), ""

    return get


def overview(asn=64500, announced=True):
    return {
        "status": "ok",
        "data": {"announced": announced, "asns": [{"asn": asn, "holder": "TEST"}]},
    }


def status(seen=100, total=100):
    return {
        "status": "ok",
        "data": {
            "first_seen": {"origin": "64500", "time": "2020-01-01T00:00:00"},
            "last_seen": {"origin": "64500", "time": "2026-11-23T00:00:00"},
            "visibility": {"v4": {"ris_peers_seeing": seen, "total_ris_peers": total}},
        },
    }


def rpki(validity):
    return {
        "status": "ok",
        "data": {
            "validating_roas": [{"origin": "64500", "prefix": "203.0.113.0/24", "validity": validity, "max_length": 24}]
        },
    }


def test_normalize_prefix():
    assert bgp.normalize_prefix("203.0.113.7/24") == "203.0.113.0/24"


def test_normalize_asn():
    assert bgp.normalize_asn("as64500") == "AS64500"
    assert bgp.normalize_asn("64500") == "AS64500"


def test_rpki_invalid_is_high(monkeypatch):
    monkeypatch.setattr(
        bgp,
        "get_json",
        fake(
            {
                "prefix-overview": overview(),
                "routing-status": status(),
                "rpki-validation": rpki("invalid"),
            }
        ),
    )
    report = bgp.lookup_prefix("203.0.113.0/24", bgp.Budget())
    finding = next(f for f in report.findings if f.check == "bgp.rpki.invalid")
    assert finding.severity == "high"
    assert finding.confidence == "high"


def test_rpki_not_found_is_medium(monkeypatch):
    monkeypatch.setattr(
        bgp,
        "get_json",
        fake(
            {
                "prefix-overview": overview(),
                "routing-status": status(),
                "rpki-validation": rpki("not-found"),
            }
        ),
    )
    report = bgp.lookup_prefix("203.0.113.0/24", bgp.Budget())
    finding = next(f for f in report.findings if f.check == "bgp.rpki.not-found")
    assert finding.severity == "medium"


def test_not_announced(monkeypatch):
    monkeypatch.setattr(
        bgp,
        "get_json",
        fake(
            {
                "prefix-overview": overview(announced=False),
                "routing-status": status(),
                "rpki-validation": rpki("valid"),
            }
        ),
    )
    report = bgp.lookup_prefix("203.0.113.0/24", bgp.Budget())
    assert "bgp.not-announced" in {f.check for f in report.findings}


def test_multi_origin(monkeypatch):
    payload = overview()
    payload["data"]["asns"].append({"asn": 64501, "holder": "OTHER"})
    monkeypatch.setattr(
        bgp,
        "get_json",
        fake(
            {
                "prefix-overview": payload,
                "routing-status": status(),
                "rpki-validation": rpki("valid"),
            }
        ),
    )
    report = bgp.lookup_prefix("203.0.113.0/24", bgp.Budget())
    assert "bgp.multi-origin" in {f.check for f in report.findings}


def test_budget_stops_requests(monkeypatch):
    calls = []

    def get(call, params):
        calls.append(call)
        return {"status": "ok", "data": {}}, ""

    monkeypatch.setattr(bgp, "get_json", get)
    bgp.lookup_prefix("203.0.113.0/24", bgp.Budget(limit=1))
    assert calls == ["prefix-overview"]
