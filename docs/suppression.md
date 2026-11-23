# Suppression and baseline

Two mechanisms, different jobs:

- A **baseline** compares two reports of the same target. Everything already in
  the baseline stays quiet. Use it for a re-scan.
- An **ignore file** records a reviewed decision. Use it for a finding accepted
  for a reason, with an owner and an expiry.

## Baseline

```bash
./beril scan --target https://staging.example --out scans/base
./beril scan --target https://staging.example --baseline scans/base.json --fail-on high
```

Matching is by finding id and normalized fingerprint. The count lands in
`meta.suppressed`. Baseline exists on `scan`, `run`, `ingest`, `deps`, `secrets`,
`infra`, `image` and `netcheck`.

## Ignore file

`.berilignore` is JSON Lines. One object per rule:

```json
{"check": "infra.tf-public-acl", "subject": "examples/*", "reason": "demo bucket", "expires": "2027-01-01"}
{"id": "a1b2c3d4e5f6", "reason": "fixed in the next release"}
```

- `check` is a glob over the check id.
- `subject` is an optional glob over the subject.
- `tag` is an optional exact tag.
- `id` matches one finding fingerprint.
- `expires` is ISO date; an expired rule stops matching.
- `reason` is for humans. A rule without one still applies.

```bash
./beril scan --target ./src --suppress .berilignore
./beril secrets --target . --suppress .berilignore
./beril deps --target . --suppress .berilignore
./beril mcp --target . --suppress .berilignore
```

Only an explicit `--suppress` reads the file; a stray `.berilignore` in a
directory does nothing until passed. Suppressed findings are removed from the
report, not hidden in the Markdown, and the count is in `meta.suppressed` plus
`meta.suppressed_by`.

## Review rule

- Suppress a check, not a whole scanner.
- Give a glob narrow enough to notice a new path.
- Set an expiry on anything temporary.
- Re-read the file when the rule table changes.
