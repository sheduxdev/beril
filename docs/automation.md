# Automation and adapters

Beril runs specialist tools instead of reimplementing them. The adapter layer
keeps one report schema and one scope gate across the chain.

## Tool inventory

```bash
./beril run --list
```

`ok` means the binary exists. Missing tools are named, never simulated. Adapters:

| Adapter | Target | Active |
|---|---|---|
| Nuclei | URL | Yes |
| testssl | URL | Yes |
| Semgrep | Directory | No |
| Trivy | Directory or image | No |
| Gitleaks | Directory | No |
| OSV-Scanner | Directory | No |
| Grype | Image or SBOM | No |
| Syft | Image | No |
| ZAP | URL (JSON report parsed) | Yes |

## Run

```bash
./beril run --target https://app.example --owned
./beril run --target ./repo
./beril run --target ./app.tar --only trivy,grype
./beril run --target https://app.example --dry-run
```

Active adapters need an ownership record. `--dry-run` prints the exact argument
list. `--header`, `--cookie` and `--auth-file` feed Nuclei and testssl.

## JavaScript render

Some checks only work after JavaScript runs. `--render` loads the page with
Camoufox and runs the same passive checks on the rendered DOM.

```bash
./beril scan --target https://app.example --render
```

The render is one browser pass, not a crawler. It is slower and needs the
Camoufox browser. A failed render falls back to the plain HTTP GET and records
the error.

## Auth

```bash
./beril scan --target https://app.example --header "Authorization: Bearer $TOKEN"
./beril scan --target https://app.example --cookie "sid=..."
./beril scan --target https://app.example --auth-file auth.json
```

`auth.json` holds a `headers` object. Values are not copied into the report;
only the header names are used in the run.

## Feeds and cache

KEV, EPSS and OSV have a dated seed in `data/`. A live lookup is opt-in:

```bash
python scripts/feeds.py status
python scripts/feeds.py update --online
python scripts/feeds.py lookup --cve CVE-2021-44228
python scripts/feeds.py osv --ecosystem npm --package lodash --version 4.17.20 --online
```

Network is off by default. With `--online`, a stale cache is refreshed, a failed
fetch falls back to the stale cache and then to the seed, and the error is kept
in `feeds.ERRORS` and the report. Cache files live under `data/feed_cache/`
(gitignored), are written atomically and are capped at 40 MB with a 20 second
timeout. TTL is 24 hours for KEV and 12 hours for EPSS and OSV.

## Ingest

```bash
./beril ingest --input nuclei.jsonl --format nuclei --target https://app.example
./beril ingest --input semgrep.sarif --format sarif --target ./src
```

Supported formats: `sarif`, `nuclei`, `trivy`, `gitleaks`, `osv`, `grype`,
`zap` and `generic`. Every parsed finding is checked against
`references/finding-schema.md`; a violation is printed and kept in the report
errors. An imported finding keeps its raw location and its tool name.

## Watch

```bash
./beril watch --target https://app.example --interval 3600 --iterations 3 \
  --webhook https://hooks.example/beril
```

The first pass becomes the baseline. Later passes suppress it and print only the
difference. Each pass writes JSON and Markdown under `scans/watch/`.

## CI

```bash
./beril scan --target https://staging.example --baseline scans/base.json \
  --fail-on high --sarif --out scans/ci
```

Exit 1 means a new finding at or above the threshold. The baseline count stays in
`meta.suppressed`.

## Boundary

- The adapters inherit the tool's own false positives and tuning.
- Beril does not manage tool versions or databases.
- A missing tool is a gap in the run, not a clean result.
- The scope gate covers Beril and the active adapters. A tool run manually
  outside `beril run` is your responsibility.
