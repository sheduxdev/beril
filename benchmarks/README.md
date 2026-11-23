# Benchmark corpora

Small, labeled samples with a pinned source. They measure the offline detectors,
not the adapters and not a full product. Results live in `docs/benchmarks.md`.

| Corpus | Files | Labels | Source | Commit | Licence |
|---|---:|---|---|---|---|
| OWASP Benchmark | 59 | vulnerable / safe per file | [BenchmarkJava](https://github.com/OWASP-Benchmark/BenchmarkJava) | `10dfcc54ad02dcfcb358b0ba4a0fef8c919a6d17` | GPL-2.0 |
| Juliet CWE-78 | 24 | vulnerable | [juliet-test-suite-c](https://github.com/arichardson/juliet-test-suite-c) | `f88433e3443648a17671398797a04ea1f8e1a274` | CC0-1.0 |
| Secrets | 34 | provider / none | crafted from `data/secret_providers.json` | n/a | MIT |
| CVE lockfiles | 12 | vulnerable / clean | `data/osv_seed.json` | n/a | MIT |

OWASP files are a deterministic slice: the first three vulnerable and first
three safe cases in ten categories. One file (`BenchmarkTest00015.java`) failed
to download and is absent from the manifest, so the count is 59.

Juliet files are one variant per test case from CWE-78 s01 and s02. Every file
contains a bad function, so the corpus measures recall only.

The secret corpus pairs 18 positives with 16 near misses: wrong length, wrong
charset, a missing header, a URL without a password.

The CVE corpus pairs six seed-affected versions with the matching fixed version.

`manifest.json` is the label source. `scripts/benchmark.py` reads it and writes
the score.

```bash
python scripts/benchmark.py --corpus all
python scripts/benchmark.py --corpus secrets --json
```
