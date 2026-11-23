import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import authz


def test_scope_matching():
    assert authz.in_scope("https://example.com/a", ["example.com"])
    assert authz.in_scope("https://api.example.com/a", ["*.example.com"])
    assert not authz.in_scope("https://example.com/a", ["other.com"])
    assert authz.in_scope("https://example.com/admin/x", ["example.com/admin/*"])
    assert not authz.in_scope("https://example.com/public", ["example.com/admin/*"])


def test_record_expires(tmp_path, monkeypatch):
    monkeypatch.setattr(authz, "STORE", str(tmp_path))
    authz.record("a.test", "dns", "tok", "matched")
    assert authz.load("a.test")["method"] == "dns"
    path = Path(authz._path("a.test"))
    data = json.loads(path.read_text())
    data["expires_at"] = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=1)).isoformat()
    path.write_text(json.dumps(data))
    assert authz.load("a.test") is None


def test_require_without_owned_returns_none(tmp_path, monkeypatch):
    monkeypatch.setattr(authz, "STORE", str(tmp_path))
    assert authz.require("a.test") is None
    entry = authz.require("a.test", owned=True)
    assert entry["method"] == "ack"
    assert authz.require("a.test")["method"] == "ack"


def test_verify_dns(monkeypatch, tmp_path):
    monkeypatch.setattr(authz, "STORE", str(tmp_path))
    token = "beril-abc"
    monkeypatch.setattr(authz, "dns_token", lambda host: token)
    result = authz.verify("a.test", token)
    assert result["method"] == "dns"


def test_verify_mismatch_stays_unverified(monkeypatch, tmp_path):
    monkeypatch.setattr(authz, "STORE", str(tmp_path))
    monkeypatch.setattr(authz, "dns_token", lambda host: "wrong")
    monkeypatch.setattr(authz, "file_token", lambda base: "")
    monkeypatch.setattr(authz, "meta_token", lambda base: "")
    result = authz.verify("a.test", "beril-abc")
    assert result["method"] == "unverified"
    assert authz.require("a.test") is None
