import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import coverage
import quiz

CARD = {
    "id": "test-card",
    "title": "A test card",
    "claim": "The claim",
    "test": "The test",
    "proof": "The proof",
    "failure": "The failure",
    "tags": ["web"],
}


def test_quiz_modes():
    question, answer = quiz.card_text(CARD, "test")
    assert "The test" in question
    assert "The claim" in answer
    question, answer = quiz.card_text(CARD, "claim")
    assert question == "The claim"
    assert "The proof" in answer
    question, answer = quiz.card_text(CARD, "title")
    assert question == "A test card"


def test_coverage_counts():
    counts = coverage.count_cards([CARD])
    assert counts["web"] == 1
    assert counts["cloud"] == 0


def test_every_domain_has_a_target():
    assert coverage.TARGET >= 10
    assert len(coverage.DOMAINS) > 20
