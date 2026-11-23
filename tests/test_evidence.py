import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import evidence


def write_claims(tmp_path, rows):
    (tmp_path / "src.txt").write_text("The council approved the budget on 3 March.\n")
    (tmp_path / "claims.jsonl").write_text("\n".join(json.dumps(row) for row in rows) + "\n")


def test_valid_claim_is_hashed_and_verified(tmp_path):
    write_claims(
        tmp_path,
        [{"claim": "Budget approved", "kind": "confirmed", "local": "src.txt", "quote": "approved the budget"}],
    )
    report = evidence.inspect(str(tmp_path))
    claim = next(f for f in report.findings if f.check == "evidence.claim")
    assert claim.verified is True
    assert "sha256:" in claim.evidence
    assert report.meta["confirmed"] == 1


def test_missing_source_high_for_confirmed(tmp_path):
    write_claims(tmp_path, [{"claim": "Unsupported", "kind": "confirmed"}])
    report = evidence.inspect(str(tmp_path))
    finding = next(f for f in report.findings if f.check == "evidence.missing-source")
    assert finding.severity == "high"
    assert finding.title == "Unsupported"


def test_inferred_without_source_is_low(tmp_path):
    write_claims(tmp_path, [{"claim": "Probably", "kind": "inferred"}])
    report = evidence.inspect(str(tmp_path))
    assert next(f for f in report.findings if f.check == "evidence.missing-source").severity == "low"


def test_quote_mismatch(tmp_path):
    write_claims(tmp_path, [{"claim": "Wrong quote", "kind": "confirmed", "local": "src.txt", "quote": "not present"}])
    report = evidence.inspect(str(tmp_path))
    assert "evidence.quote-mismatch" in {f.check for f in report.findings}


def test_bad_status_and_empty_claim(tmp_path):
    write_claims(tmp_path, [{"claim": "x", "kind": "maybe"}, {"claim": "", "kind": "confirmed"}])
    checks = {f.check for f in evidence.inspect(str(tmp_path)).findings}
    assert {"evidence.bad-status", "evidence.empty-claim"} <= checks
