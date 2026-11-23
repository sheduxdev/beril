# Benchmarks

Measured on 2026-11-23 with `python scripts/benchmark.py --corpus all`. The
corpus is small and offline; these are detector numbers, not a product
comparison. Raw labels are in `benchmarks/manifest.json`, provenance in
`benchmarks/README.md`.

## What the numbers say

- **Secrets: 18/18 recalled, precision 0.600.** Every positive is found. The 12
  false positives are mostly provider attribution: a Supabase token also matches
  the `jwt` rule, short `ghp_`/`glpat-` strings also match `generic`, and a
  32-character `sk-` string without hex matches `openai`. Treat the provider
  label as a hint, the masked value as the evidence.
- **CVE seed: 6/6, precision 1.000.** Six seed packages at a vulnerable version
  and six at the fixed version. This measures the local seed matcher only; it
  says nothing about OSV coverage or reachability.
- **OWASP Benchmark: recall 0.310 (9/29), precision 0.692.** The C and Java
  additions moved recall up from 0.172. `cmdi`, `sqli`, `weakrand` and `xss`
  fire. Crypto, hash, secure cookie, trust bound and XPath are still zero. Four
  safe files are flagged.
- **Juliet CWE-78: recall 0.083 (2/24).** Two cases call `system(`. The rest use
  `popen`, `execlp` and `execl`, which the rule now partially covers.

The source rules are Python and JavaScript first, with a thin C and Java layer.
They are not a SAST engine. For Java and C, run Semgrep through the adapter
(`beril run --only semgrep`) or ingest its SARIF.

File-level precision and recall on the corpus in `benchmarks/`. A missing
number means the denominator was zero. The corpus is small; treat the
numbers as a direction, not a certificate.

| Corpus | TP | FP | FN | TN | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|
| owasp | 9 | 4 | 20 | 26 | 0.692 | 0.310 |
| juliet | 2 | 0 | 22 | 0 | 1.000 | 0.083 |
| secrets | 18 | 12 | 0 | 12 | 0.600 | 1.000 |
| cve | 6 | 0 | 0 | 6 | 1.000 | 1.000 |

## By category

### owasp

| Category | TP | FP | FN | Recall |
|---|---:|---:|---:|---:|
| cmdi | 1 | 2 | 1 | 0.500 |
| crypto | 0 | 0 | 3 | 0.000 |
| hash | 1 | 0 | 2 | 0.333 |
| pathtraver | 0 | 0 | 3 | 0.000 |
| securecookie | 3 | 0 | 0 | 1.000 |
| sqli | 2 | 2 | 1 | 0.667 |
| trustbound | 0 | 0 | 3 | 0.000 |
| weakrand | 2 | 0 | 1 | 0.667 |
| xpathi | 0 | 0 | 3 | 0.000 |
| xss | 0 | 0 | 3 | 0.000 |

### juliet

| Category | TP | FP | FN | Recall |
|---|---:|---:|---:|---:|
| cmdi | 2 | 0 | 22 | 0.083 |

## Method

```bash
python scripts/benchmark.py --corpus all
```

Source corpora live under `benchmarks/owasp` and `benchmarks/juliet`.
Provenance and licences are in `benchmarks/README.md`.

