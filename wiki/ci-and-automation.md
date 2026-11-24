# CI and automation

## Fail a pipeline on new findings

```bash
# First run writes the baseline
./beril scan --target https://staging.example --out scans/staging
# Later runs fail only on new high or critical findings
./beril scan --target https://staging.example --baseline scans/staging.json --fail-on high --sarif
```

The baseline matches by finding id and by check plus subject. The count is written to `meta.suppressed`, so a report still says how much it hid. Exit code 0 means no finding at or above the threshold. Exit code 1 means one exists. The same flags work on `bgp`.

## Reviewed ignores

A `.berilignore` file holds ignores with a reason and an expiry:

```bash
./beril scan --target ./repo --suppress .berilignore
```

An expired ignore stops hiding its finding. See [Suppression](../docs/suppression.md).

## Machine formats

| Output | Use |
|---|---|
| JSON | The finding schema. Re-render with `./beril report` |
| SARIF 2.1.0 | Code scanning UIs. Checked against the schema |
| CycloneDX 1.5 | SBOM with purl, license and hash where vendored |
| SPDX 2.3 and OpenVEX | Supply chain exchange |

## Other tools in the loop

```bash
./beril run --target <url-or-dir>                       # installed scanners, one schema
./beril ingest --input out.sarif --format sarif         # bring another tool's output in
./beril watch --target https://app.example              # interval scan, baseline diff, webhook
```

`run` drives Nuclei, Semgrep, Trivy, Gitleaks, OSV, Grype, testssl and ZAP when they are installed. `ingest` accepts SARIF, Nuclei, Trivy, Gitleaks, OSV, Grype or ZAP output. Missing tools are skipped and named in the output. See [Automation](../docs/automation.md).

## Install paths

| Path | Command |
|---|---|
| Script | `./install.sh` |
| pipx | `pipx install .` |
| Wheel | Build with the project tooling and install the wheel |
| Container | A pinned image. Mind the writable-directory note |
| GitHub Action | The composite `action.yml` in the repository root |

The commands and the offline defaults are in [Deployment](../docs/deployment.md).

## Quality gates for contributors

```bash
./install.sh --dev
ruff check scripts tests
ruff format --check scripts tests
pyright
python -m pytest -q
./beril validate
python scripts/validate.py --links --max-links 40
```

Web tests run against a local fixture only. Ruff and pyright are pinned to the versions CI uses. Read [Contributing](../CONTRIBUTING.md) before a pull request.
