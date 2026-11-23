# Finding schema

Every scanner writes `Finding` objects from `scripts/beril_model.py`. Hand edits
are allowed, but a missing field fails the renderer quality gate.

## Required

| Field | Type | Notes |
|---|---|---|
| `check` | string | Stable dotted id, e.g. `web.header.csp` |
| `title` | string | One line, no marketing |
| `severity` | enum | `critical high medium low info` |
| `confidence` | enum | `high medium low` |
| `evidence` | string | File:line or request summary, no raw secret |
| `impact` | string | One sentence in business language |
| `fix` | string | Copyable step |

`subject` defaults to the first token of evidence. Set it explicitly for URLs
and network findings.

## Optional

`source`, `state`, `cwe`, `tags`, `request`, `response`, `false_positive`,
`verified`, `cvss_score`, `cvss_vector`, `refs`, `kev`, `epss`.

## Rules

1. `state: inferred` cannot keep `confidence: high`. The constructor lowers it.
2. `verified` only with a live provider check, a sandbox crash or a human
   replay.
3. Generic regex hits stay at `low` confidence.
4. A missing header is `high` confidence and low severity. Confidence is about
   detection, not impact.
5. Evidence must identify the asset. "Header absent" alone is not enough.
6. The fix names the layer: server config, code, DNS, CI.

## Severity anchors

| Level | Anchor |
|---|---|
| critical | No-auth full control, bulk data, code execution |
| high | One step to serious data or account impact |
| medium | Weakens defense or feeds a chain |
| low | Hygiene and hardening |
| info | Decision support |

## Priority

`priority = severity_weight × confidence_factor × verified × source × KEV × EPSS`

Weights: critical 100, high 60, medium 30, low 10, info 2. Confidence: high 1.0,
medium 0.7, low 0.4. Verified 1.2, active 1.1, KEV 1.5, EPSS `1 + 0.8 × score`.

The number is for ordering only. `priority_reason` explains it.

## Dedupe

`check + normalize(subject)` is the fingerprint. The merge keeps the highest
confidence, the verified flag, the longest evidence and the higher severity.
IDs are content addressed and stable.

## Example

```json
{"check": "active.traversal", "title": "Path traversal read: file",
 "severity": "high", "confidence": "high", "evidence": "GET /download?file=../../etc/passwd -> root:x:0:0",
 "impact": "Readable server files leak.", "fix": "Resolve realpath and enforce a prefix.",
 "subject": "https://app.example/download", "source": "active", "cwe": ["CWE-22"],
 "request": "GET /download?file=../../etc/passwd HTTP/1.1", "response": "root:x:0:0:...",
 "verified": true, "false_positive": "Path normalisation may differ per framework."}
```
