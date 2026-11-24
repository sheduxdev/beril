import datetime as dt
import json
import sys
import urllib.error
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import feeds


@pytest.fixture(autouse=True)
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(feeds, "CACHE", str(tmp_path / "cache"))
    monkeypatch.setattr(feeds, "ERRORS", [])
    return tmp_path / "cache"


def offline(_url, _body=None):
    raise AssertionError("network must stay off")


def test_kev_offline_reads_seed(isolated, monkeypatch):
    monkeypatch.setattr(feeds, "http_json", offline)
    data = feeds.load_kev()
    assert data["from"] == "seed"
    assert "CVE-2021-44228" in data["cves"]


def test_epss_offline_reads_seed(isolated, monkeypatch):
    monkeypatch.setattr(feeds, "http_json", offline)
    data = feeds.load_epss("CVE-2021-44228")
    assert data["from"] == "seed"
    assert data["score"] > 0.5


def test_osv_offline_reads_seed(isolated, monkeypatch):
    monkeypatch.setattr(feeds, "http_json", offline)
    data = feeds.osv_query("npm", "lodash", "4.17.20")
    assert data["from"] == "seed"
    assert data["vulns"][0]["id"] == "CVE-2021-23337"


def test_fresh_cache_avoids_network(isolated, monkeypatch):
    feeds.write_cache("kev", "", {"cves": {"CVE-2024-0001": {"name": "cached"}}}, "test")
    monkeypatch.setattr(feeds, "http_json", offline)
    data = feeds.load_kev()
    assert data["from"] == "cache"
    assert data["cves"]["CVE-2024-0001"]["name"] == "cached"


def test_online_success_writes_cache(isolated, monkeypatch):
    payload = {
        "vulnerabilities": [
            {
                "cveID": "CVE-2024-1111",
                "vulnerabilityName": "x",
                "vendorProject": "y",
                "dateAdded": "2024-01-01",
                "knownRansomwareCampaignUse": "Unknown",
            },
            {"cveID": "not-a-cve"},
        ]
    }
    monkeypatch.setattr(feeds, "http_json", lambda _url, _body=None: payload)
    data = feeds.load_kev(online=True)
    assert data["from"] == "network"
    assert set(data["cves"]) == {"CVE-2024-1111"}
    assert Path(feeds.cache_path("kev")).exists()


def test_online_timeout_falls_back_to_seed(isolated, monkeypatch):
    def boom(_url, _body=None):
        raise TimeoutError("too slow")

    monkeypatch.setattr(feeds, "http_json", boom)
    data = feeds.load_kev(online=True)
    assert data["from"] == "seed"
    assert feeds.ERRORS and "TimeoutError" in feeds.ERRORS[0]


def test_online_url_error_falls_back_to_stale_cache(isolated, monkeypatch):
    feeds.write_cache("epss", "CVE-2021-44228", {"cve": "CVE-2021-44228", "score": 0.5}, "test")
    path = feeds.cache_path("epss", "CVE-2021-44228")
    entry = json.loads(Path(path).read_text())
    entry["fetched_at"] = (dt.datetime.now(dt.UTC) - dt.timedelta(days=3)).isoformat()
    Path(path).write_text(json.dumps(entry))

    def boom(_url, _body=None):
        raise urllib.error.URLError("down")

    monkeypatch.setattr(feeds, "http_json", boom)
    data = feeds.load_epss("CVE-2021-44228", online=True)
    assert data["from"] == "stale-cache"
    assert data["score"] == 0.5
    assert "URLError" in feeds.ERRORS[0]


def test_write_is_atomic(isolated):
    feeds.write_cache("osv", "npm|a|1.0.0", {"vulns": []}, "test")
    path = Path(feeds.cache_path("osv", "npm|a|1.0.0"))
    assert path.exists()
    assert not path.with_suffix(".json.tmp").exists()


def test_osv_many_uses_cache_and_batches_misses(isolated, monkeypatch):
    feeds.write_cache("osv", "npm|lodash|4.17.20", {"vulns": [{"id": "cached"}]}, "test")
    calls = []

    def fake(url, body=None):
        calls.append((url, body))
        return {"results": [{"vulns": [{"id": "CVE-2024-2222"}]}]}

    monkeypatch.setattr(feeds, "http_json", fake)
    results, errors, marker = feeds.osv_query_many(
        [("npm", "lodash", "4.17.20"), ("npm", "axios", "1.5.0")], online=True
    )
    assert errors == []
    assert marker == "network"
    assert results[0][0]["id"] == "cached"
    assert results[1][0]["id"] == "CVE-2024-2222"
    assert len(calls) == 1
    assert calls[0][0].endswith("/querybatch")


def test_osv_many_offline_marks_seed(isolated, monkeypatch):
    monkeypatch.setattr(feeds, "http_json", offline)
    results, errors, marker = feeds.osv_query_many([("npm", "lodash", "4.17.20")])
    assert marker == "seed"
    assert results == [[]]
    assert errors == []


def test_status_reports_freshness(isolated, monkeypatch):
    monkeypatch.setattr(feeds, "http_json", offline)
    feeds.write_cache("kev", "", {"cves": {}}, "test")
    state = feeds.status()
    assert state["kev"]["fresh"] is True
    assert state["epss"]["fresh"] is False
    assert state["kev"]["seed"] is True


def test_update_offline_does_not_network(isolated, monkeypatch):
    monkeypatch.setattr(feeds, "http_json", offline)
    assert feeds.update(False)["online"] is False


def test_update_online_counts(isolated, monkeypatch):
    monkeypatch.setattr(feeds, "http_json", lambda _url, _body=None: {"vulnerabilities": [{"cveID": "CVE-2024-3333"}]})
    result = feeds.update(True)
    assert result["kev"] == 1
    assert result["online"] is True


def test_version_lt_numeric_not_string():
    assert feeds.version_lt("1.0.0", "10.0.0")
    assert not feeds.version_lt("10.0.0", "1.0.0")


def test_priority_reads_feed_cache(isolated):
    import priority

    feeds.write_cache("kev", "", {"cves": {"CVE-2024-4444": {"name": "x"}}}, "test")
    feeds.write_cache("epss", "CVE-2024-4444", {"cve": "CVE-2024-4444", "score": 0.77}, "test")
    data = priority.enrich("CVE-2024-4444")
    assert data["kev"] is True
    assert data["epss"] == 0.77


def test_deps_online_hits_reads_feed_batch(isolated, monkeypatch):
    import deps

    monkeypatch.setattr(
        feeds, "http_json", lambda _url, _body=None: {"results": [{"vulns": [{"id": "CVE-2024-5555", "summary": "x"}]}]}
    )
    hits, error = deps.online_hits([("lodash", "4.17.20", "npm", "package.json", 3)])
    assert error == ""
    assert hits[0]["id"] == "CVE-2024-5555"
    assert hits[0]["name"] == "lodash"


def test_deps_online_hits_reports_feed_error(isolated, monkeypatch):
    import deps

    def boom(_url, _body=None):
        raise TimeoutError("slow")

    monkeypatch.setattr(feeds, "http_json", boom)
    hits, error = deps.online_hits([("lodash", "4.17.20", "npm", "package.json", 3)])
    assert hits == []
    assert "TimeoutError" in error
