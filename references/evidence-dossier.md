# Evidence dossier template

For a story, an OSINT file or a fact-check. The unit is a claim, not a
document. Each claim names a source, a status and optionally a quote.

```jsonl
{"claim": "The contract was signed on 12 May", "kind": "confirmed", "local": "sources/contract.pdf.txt", "quote": "signed on 12 May"}
{"claim": "The site was already empty in April", "kind": "inferred"}
{"claim": "The company denied it", "kind": "confirmed", "source": "https://example.org/reply"}
```

## Fields

| Field | Required | Notes |
|---|---|---|
| `claim` | yes | One sentence |
| `kind` | yes | `confirmed` or `inferred` |
| `local` | for offline | Path relative to `claims.jsonl` |
| `source` | for URLs | Absolute URL |
| `quote` | recommended | Exact words from the source |

## Rules

1. A confirmed claim needs a local copy or a URL. The run flags it as high when
   both are missing.
2. Keep the local copy next to the file and keep its hash in the report.
3. A hash proves the copy did not change, not that the source is truthful.
4. An inferred claim is allowed to have no source. It is labelled low.
5. A quote must appear in the source. A mismatch is a finding.
6. `--fetch` downloads URL sources at 2 MB and 15 s. Offline is the default.

## Output

`./beril evidence --target ./story --out story/evidence` writes a table with
claim, status, source and the first 16 hex characters of the hash, followed by
the flags and the limit block. The JSON holds the full hash.

## Before publishing

- Archive each URL yourself. A live page changes.
- Re-run after the last edit.
- Keep the dossier and the source copies together.
- The tool does not check the claim against the source semantics; a human does.
