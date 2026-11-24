# Command reference

Every command is `./beril <command>`. The wrapper dispatches to the scripts in `scripts/`. Flags below are the ones the project documents.

## Scan and verify

| Command | What it does |
|---|---|
| `./beril scan --target <url-or-path>` | Passive web or static artifact scan |
| `./beril scan ... --profile <p>` | Choose the report reader: `engineer`, `bugbounty`, `smb`, `maintainer`, `cra` |
| `./beril scan ... --out <path>` | Choose the output base name |
| `./beril scan ... --render` | Run passive checks on a JavaScript-rendered page |
| `./beril scan ... --active` | Minimal active probes. Ownership gated |
| `./beril scan ... --deep` | Route a binary through capa, FLOSS and rizin when installed |
| `./beril scan ... --tools` | Add Semgrep and Gitleaks when installed |
| `./beril scan ... --vibe`, `--mcp`, `--sbom` | Add the matching pass |
| `./beril scan ... --header`, `--cookie`, `--auth-file` | Scan a logged-in session. Beril does not fill login forms |
| `./beril verify --new <host>` | Issue an ownership token and show the three publish paths |
| `./beril verify --verify <host>` | Check the published token |

## Defend

| Command | What it does |
|---|---|
| `./beril secrets --target <dir> --history` | Masked secret scan including git history. Revoke first, then clean |
| `./beril mcp --target <dir>` | MCP configuration, skill, agent and plugin manifest checks |
| `./beril jar --target <jar-or-dir>` | Minecraft plugin and JAR triage |
| `./beril vibe --target <dir>` | Supabase RLS, client secrets and other vibe-coded app checks |
| `./beril deps --target <dir> --reachability` | Dependency inventory with OSV, KEV and EPSS |
| `./beril sbom --target <dir> --out <file>` | CycloneDX SBOM, optional SPDX and OpenVEX, license table |
| `./beril infra --target <dir>` | Terraform, Kubernetes, Docker and CloudFormation review |
| `./beril image --target <image>` | Trivy, Grype and Syft image pass |
| `./beril netcheck --target <dir>` | Exported sshd, nftables, DNS, nginx and HAProxy config audit |
| `./beril bgp --prefix <cidr>` | Passive BGP, RIS and RPKI posture lookup |
| `./beril health --target <dir>` | Open source maintenance scorecard with reasons |
| `./beril evidence --target <dir>` | Claim, source, status and hash dossier |

## Hunt and reverse engineer

| Command | What it does |
|---|---|
| `./beril hunt --target <repo> --sandbox` | Local bug hunt with sanitizers in a networkless container |
| `./beril re --target <binary> --capa --floss --rizin` | Explicit binary triage |
| `./beril guard --text <file>` | Prompt injection risk score for harvested text |
| `./beril incidents list` | Published incident cases with a rule and a lab |

## Reports, automation and CI

| Command | What it does |
|---|---|
| `./beril report --input <json> --profile <p>` | Render engineer, bugbounty, SMB, maintainer, CRA, JSON or SARIF |
| `./beril scan ... --fail-on high` | Exit 1 when a finding is at or above the threshold |
| `./beril scan ... --baseline old.json` | Hide findings already in the baseline |
| `./beril scan ... --suppress .berilignore` | Apply reviewed ignores with a reason and an expiry |
| `./beril scan ... --sarif` | Also write SARIF |
| `./beril run --target <url-or-dir>` | Run installed Nuclei, Semgrep, Trivy, Gitleaks, OSV, Grype, testssl and ZAP, merged into one schema |
| `./beril ingest --input <file> --format <fmt>` | Merge SARIF, Nuclei, Trivy, Gitleaks, OSV, Grype or ZAP output |
| `./beril watch --target <url>` | Interval scan, baseline diff, JSON and webhook |
| `./beril feeds --online` | Refresh or inspect the KEV, EPSS and OSV cache |
| `./beril benchmark` | Precision and recall on the labeled offline corpora |

## Research and memory

| Command | What it does |
|---|---|
| `./beril harvest <layer>` | Collect `forums`, `experts`, `tools`, `methods` or `all` |
| `./beril extract` | Turn URLs into structure notes |
| `./beril dossier` | Rebuild `examples/dossier.md` |
| `./beril github` | Refresh the GitHub atlas |
| `./beril recall "<query>" --decide` | Return `USE`, `REFRESH` or `RESEARCH` for a topic |
| `./beril remember add` | Add a memory card after a new lesson |
| `./beril gaps --next` | Show the next high-priority knowledge gap |
| `./beril validate` | Schema, link and prose checks |

## Training and workspace

| Command | What it does |
|---|---|
| `./beril train --status` | Curriculum progress |
| `./beril train --week <n>` | Show a week |
| `./beril labs --run [name]` | Run one lab or every smoke test |
| `./beril reflect` | Save a lab finding as a method note |
| `./beril job log`, `./beril job list` | Write or read the job and cost ledger |
| `./beril dashboard` | Start the local dashboard on `127.0.0.1:8788`. `--port` changes it, `--no-open` skips the browser |

## Exit codes

`0` means no finding at or above the threshold. `1` means at least one exists. The same flags work on `bgp`.
