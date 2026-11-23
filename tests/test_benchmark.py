import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import benchmark

ROOT = Path(__file__).resolve().parents[1]


def test_score_math():
    assert benchmark.score({"tp": 3, "fp": 1, "fn": 1, "tn": 5}) == {
        "tp": 3,
        "fp": 1,
        "fn": 1,
        "tn": 5,
        "precision": 0.75,
        "recall": 0.75,
    }


def test_score_with_zero_denominator():
    result = benchmark.score({"tp": 0, "fp": 0, "fn": 0, "tn": 3})
    assert result["precision"] is None
    assert result["recall"] is None


def test_manifest_labels_every_file():
    manifest = json.loads((ROOT / "benchmarks" / "manifest.json").read_text())
    for section in ("owasp", "juliet", "cve"):
        for name in manifest[section]["cases"]:
            directory = "owasp" if name.endswith(".java") else "juliet" if name.endswith(".c") else "cve"
            assert (ROOT / "benchmarks" / directory / name).exists(), name
    for name in manifest["secrets"]["positives"]:
        assert (ROOT / "benchmarks" / "secrets" / name).exists(), name


def test_secrets_corpus_recalls_every_positive():
    manifest = json.loads((ROOT / "benchmarks" / "manifest.json").read_text())
    result = benchmark.secret_corpus(manifest["secrets"])
    assert result["total"]["recall"] == 1.0


def test_cve_corpus_has_full_recall():
    manifest = json.loads((ROOT / "benchmarks" / "manifest.json").read_text())
    result = benchmark.cve_corpus(manifest["cve"])
    assert result["total"]["recall"] == 1.0
    assert result["total"]["precision"] == 1.0


def test_markdown_has_a_row_per_corpus():
    text = benchmark.markdown(
        {"secrets": {"total": benchmark.score({"tp": 1, "fp": 0, "fn": 0, "tn": 0}), "categories": {}}}
    )
    assert "| secrets | 1 | 0 | 0 | 0 | 1.000 | 1.000 |" in text
