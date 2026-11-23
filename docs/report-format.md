# Report format and finding schema

A finding can be as small as a file line or as large as a production outage.
Both carry the same fields: severity, confidence, evidence, impact, fix and a
false positive note. The renderer refuses a finding with a missing field.

## Schema

```json
{
  "schema": "beril.report/1",
  "tool_version": "1.4.0",
  "target": "https://app.example",
  "mode": "active",
  "profile": "bugbounty",
  "started_at": "2026-11-23T09:00:00+00:00",
  "finished_at": "2026-11-23T09:02:00+00:00",
  "authorization": {"method": "dns", "evidence": "TXT matched", "verified_at": "..."},
  "scope": {"in_scope": ["app.example"], "out_of_scope": [], "checked": [], "not_checked": []},
  "limits": {"max_requests": 250, "requests_sent": 90, "rate_per_second": 2.0},
  "counts": {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 1},
  "score": 140,
  "top_actions": ["id1"],
  "findings": [{
    "id": "a1b2c3d4e5f6",
    "check": "active.traversal",
    "title": "Path traversal file read: file",
    "severity": "high",
    "confidence": "high",
    "state": "observed",
    "verified": true,
    "source": "active",
    "subject": "https://app.example/download",
    "evidence": "GET ... -> /etc/passwd content",
    "impact": "Readable server files leak.",
    "fix": "Resolve realpath and enforce a prefix.",
    "false_positive": "",
    "cwe": ["CWE-22"],
    "tags": ["traversal"],
    "request": "GET /download?file=../../etc/passwd HTTP/1.1",
    "response": "root:x:0:0:...",
    "cvss_score": null,
    "cvss_vector": "",
    "refs": [],
    "kev": false,
    "epss": null,
    "priority": 79,
    "priority_reason": "base high, confidence high, verified"
  }]
}
```

## Field rules

| Field | Rule |
|---|---|
| `id` | `sha1(check + normalize(subject) + evidence[:120])[:12]`. Stable across runs. |
| `check` | Dotted, stable id. Example: `web.header.csp`, `secret.aws`, `dep.cve.2021.44228`. |
| `severity` | `critical`, `high`, `medium`, `low`, `info`. |
| `confidence` | `high`, `medium`, `low`. Detection quality, not impact. |
| `state` | `observed` or `inferred`. An inferred finding cannot carry high confidence. |
| `verified` | True only after a live check or sandbox evidence. |
| `evidence` | File:line or request summary. No raw secret. |
| `subject` | Dedupe key. URL, `file:line` or host:port. |
| `impact` | One sentence in business language. CVSS is not impact. |
| `fix` | Copyable step. "Fix it" is not enough. |
| `false_positive` | Why the finding may be wrong. An empty value is fine, a lie is not. |
| `cwe` | List. At least one CWE is preferred. |
| `request` / `response` | At most 1200 characters. Secrets masked. |
| `kev` / `epss` | From the local data set. Empty when unknown. |
| `priority` | `severity × confidence × verification × KEV × EPSS`, as an integer. |
| `priority_reason` | Explains the score. No magic. |

## Severity anchors

| Level | Anchor |
|---|---|
| critical | No-auth full control, bulk data, code execution |
| high | Serious data or account impact in one step |
| medium | Weakens the defense or feeds a chain |
| low | Hygiene, hardening, information leak |
| info | Decision support, not a risk alone |

When CVSS exists, it maps to a band, but the score alone does not set the order.

## Top five

`top_actions` selects only `critical`, `high` and `medium` findings with
confidence above `low`, and stops at five. The aim is six real tasks instead of
134 lines.

## Profiles

| Profile | Reader | Shape |
|---|---|---|
| `engineer` | The person fixing it | Full technical detail |
| `bugbounty` | Program triage | CVSS, CWE, request pair |
| `smb` | Non-technical decision maker | One page, traffic light, KVKK note |
| `maintainer` | Open source maintainer | Smallest reproduction, patch suggestion, product block |
| `cra` | EU CRA handler and product security team | Article map, timeline, fixed version, evidence boundary |

The `cra` and `maintainer` profiles read optional metadata: `product`, `version`,
`contact`, `fixed_version` or a `fixed_versions` map by finding id, and the
`found_at`, `reported_at`, `acknowledged_at`, `fix_target`, `disclosure_at`
timeline. Missing values render as `TBD`, never as a guess.

## Outputs

- `.json`: the source of truth. Every other view derives from it.
- `.md`: the human file.
- `.sarif`: CI integration, version 2.1.0.

Every SARIF document is checked by `scripts/sarif_schema.py` before it is
returned. The validator covers the emitted shape (version, tool driver, rule
ids, levels, message, location, fingerprints, invocation time) and is not a
full JSON Schema implementation. When `jsonschema` is installed it also validates
against the vendored official schema at `references/sarif-2.1.0.schema.json`. A
violation raises instead of writing a file a consumer would reject. `jsonschema`
is a dev dependency; without it the structural checks still run.

```bash
./beril report --input scans/app.json --profile smb --out app-smb.md
./beril report --input scans/app.json --profile sarif --out app.sarif
```

## Empty report

An empty result says: "No finding inside these checks. The skipped list is below.
This is not a certificate."

Three sections are mandatory: attempted, skipped, limits. A missing
authorization record is written down too.

## Accuracy rules

1. A scanner line alone is not a finding. Evidence must identify the asset.
2. The same `check` and `subject` dedupe. The highest confidence and all
   evidence merge.
3. An inferred finding cannot be high confidence.
4. Secret values are masked. The first four and last four characters are enough.
5. Every report carries a `limits` block. A report without limits is incomplete.
