![Beril, green eyes and pistachio](assets/beril.webp)

# Beril

A local-first cybersecurity skill for agents and people, with two working lines. The defense line scans an app, repository, artifact, MCP config or Minecraft plugin you own and returns a ranked fix list. The attack line hunts bugs in open source behind an ownership gate, a networkless sandbox and maintainer reports. Both lines share one finding model: severity, confidence, evidence, impact, fix and a plain statement of what was not tested.

Beril also reads the security sites that block plain HTTP clients, keeps every lead with a date and a public URL, and turns the result into a dossier with a reading queue, a tool shelf and method cards. The repository carries ten practice labs and a 25-week training plan.

[![version](https://img.shields.io/github/v/tag/sheduxdev/beril?sort=semver&label=version&color=2f6f4e)](https://github.com/sheduxdev/beril/tags)
![license](https://img.shields.io/badge/license-MIT-2f6f4e)
![python](https://img.shields.io/badge/python-3.11%2B-2f6f4e)
[![validate](https://github.com/sheduxdev/beril/actions/workflows/validate.yml/badge.svg)](https://github.com/sheduxdev/beril/actions/workflows/validate.yml)
[![stars](https://img.shields.io/github/stars/sheduxdev/beril?style=flat&color=2f6f4e)](https://github.com/sheduxdev/beril/stargazers)

Current release: **1.4.0**. Snapshot date: **2026-11-23**.

Documentation: **https://sheduxdev.github.io/beril/**. The source pages live in `wiki/`, `docs/`, `references/` and `knowledge/`. Build the site locally with `python3 scripts/build_docs.py`.

Beril was built from 44 public security skill repositories and a live collection pass over forums, disclosed reports, researcher blogs and GitHub tool shelves. Every catalog row links to its origin. The snapshot is a sample with a date, not a census.

## What it is

| Layer | What it does |
|---|---|
| Skill | `SKILL.md` gives an agent the loop, output contract, browser rules and quality gates. |
| Router files | `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, Cursor, Windsurf, Cline, Copilot and Aider files point an agent at the skill without pasting it five times. |
| CLI | `./beril` wraps harvest, dossier, scan, secrets, MCP, JAR, vibe, deps, SBOM, hunt, report, RE triage, labs, training and the dashboard. |
| Finding model | One schema and five renderers: engineer, bugbounty, SMB, maintainer, CRA. JSON and SARIF are machine outputs. |
| Gates | Ownership record before active probes, scope file, request budget, rate limit, masked secrets, static-only artifacts. |
| Catalogs | Dated JSONL for threads, experts, tools, methods and the GitHub atlas. |
| Labs | Ten local targets with tasks, smoke tests and answer keys. |
| Tests | 65 regression tests with local fixtures, a planted-secret repo and golden renderer output. |
| Dashboard | A loopback-only posture and workspace view with jobs, spend, scans, labs and every catalog. |

## What it does

| Job | Behavior | Entry point |
|---|---|---|
| Collect public leads | Camoufox reads RSS, JSON, shadow DOM and challenge pages. Responses are cached by URL hash. | `./beril harvest forums`, `experts`, `tools`, `methods`, `all` |
| Extract structure | Records headings, intro, code block count and table count so a method can be separated from a news item. | `./beril extract` |
| Build a dossier | Merges the catalogs into a ranked brief with links and explicit gaps. | `./beril dossier` |
| Map the tool shelf | Sweeps GitHub topics for security repositories with stars, language, license and last push. | `./beril github` |
| Scan your web app | Passive checks for headers, CSP, cookies, CORS, 35 exposed paths, TLS, SPF/DKIM/DMARC, 8 common ports and fingerprints. Request budget and robots.txt respect. | `./beril scan --target https://your-app.example` |
| Prioritize known bugs | KEV, EPSS and CVSS joined to dependency findings, with import reachability as a first filter. | `./beril deps --target ./repo --reachability` |
| Scan secrets | Provider patterns, context filters, git history and masked output. Revocation link per hit, revoke-first order. Optional live check. | `./beril secrets --target ./repo --history` |
| Audit MCP configs | Unpinned packages, plaintext keys, broad filesystem access, privileged containers, plain HTTP, tool-description instructions. | `./beril mcp --target .` |
| Triage a plugin | JAR manifest, IOC files, class strings, external URLs, Base64, obfuscation and hash. | `./beril jar --target ./plugins` |
| Review a vibe-coded app | Missing RLS, service_role in the client, NEXT_PUBLIC secrets, unsafe HTML, open CORS, open Firebase rules. | `./beril vibe --target ./app` |
| Active probes | One quote, one marker, one redirect, one traversal per parameter, OPTIONS and TRACE. Ownership gated. | `./beril scan --target https://your-app.example --active` |
| Hunt a repo | Fingerprint, OSV, source rules, git history, fan-in, optional networkless sandbox with sanitizers. | `./beril hunt --target ./repo --sandbox` |
| Render a report | Four reader profiles plus JSON and schema-checked SARIF from the same evidence. | `./beril report --input scans/app.json --profile smb` |
| Run specialist tools | Installed Nuclei, Semgrep, Trivy, Gitleaks, OSV, Grype and testssl, merged into one schema. | `./beril run --target <url-or-dir>` |
| Ingest another tool | SARIF, Nuclei, Trivy, Gitleaks, OSV, Grype or ZAP output into a Beril report. | `./beril ingest --input out.sarif --format sarif` |
| Watch a target | Interval scan, baseline diff, JSON and webhook. | `./beril watch --target https://app.example` |
| Review infrastructure | Terraform, Kubernetes, Docker and CloudFormation rules. | `./beril infra --target ./terraform` |
| Scan an image | Trivy, Grype and Syft when installed. | `./beril image --target app:tag` |
| Audit saved configs | sshd, nftables, DNS, nginx and HAProxy checks. | `./beril netcheck --target ./configs` |
| Produce an SBOM | CycloneDX 1.5 with purl, license and hash where a component is vendored, plus SPDX 2.3, OpenVEX and a license table. | `./beril sbom --target ./repo --spdx sbom.spdx.json --vex sbom.vex.json` |
| Scan an artifact | Static review of an APK, IPA, PE, ELF, JAR, archive or source tree. Manifests, hardening, secrets, dangerous sinks and archive paths. | `./beril scan --target ./build/app.apk` |
| Triage a binary deeper | Optional capa, FLOSS, rizin, YARA and Ghidra passes. Missing tools are skipped and named in the output. | `./beril re --target ./sample --capa --floss --rizin` |
| Train | A 25-week curriculum with drills, checkpoints and grading rubrics. | `./beril train --week 1` |
| Run a lab | Ten local labs: web, binary, fuzz, RE, mobile, firmware, cloud, AD, LLM and detection. | `./beril labs --run web` |
| Track work | Append-only job ledger with actor, model, tokens and cost. | `./beril job log` |
| Watch the whole base | Local dashboard for spend, jobs, scans, labs and catalogs. | `./beril dashboard` |

## What you can do with it

- Prepare for a bounty program by pulling the current tools and methods for its stack, with links you can check.
- Build a reading queue before an engagement and sort it by code density instead of headline.
- Compare researchers by what they publish, not by follower count.
- Open a page that returns 403 or an empty JavaScript shell to `curl` and still get the text.
- Run a first read-only pass over an app you own before a manual review.
- Inspect an APK, IPA, EXE or ELF without running it.
- Turn a lab result into a durable method note with `./beril reflect`.
- Give Claude, Codex, Gemini, Cursor, Copilot, Windsurf, Cline or Aider a source-backed security workflow.

## What it cannot do

| Limit | Detail |
|---|---|
| It does not weaponize | Active probes are four minimal GET patterns. No POST body, upload, SSRF callback or race. No working exploit is generated. |
| The active set is narrow | A quote, a marker, a redirect, a traversal, OPTIONS and TRACE per parameter. Depth needs a human. |
| No login automation | Sessions work through `--header`, `--cookie` or `--auth-file`. Beril does not fill login forms or refresh tokens. |
| Artifact scans are static | Samples are read, not executed. Packed, encrypted or heavily obfuscated files can hide most behavior. |
| The hunt sandbox is a container | Network off, read-only mount, dropped capabilities and resource caps, but the host kernel is shared. Use a VM for hostile samples. |
| Reachability is a grep | An unused package can still be pulled in transitively, so it is reported low, not removed. |
| Version matching is a hint | The offline CMS and OSV seeds are small. Use the adapters, `--online` or the real advisory database for currency. |
| Live secret checks leave the host | `--verify` sends the key to the provider read endpoint. It is off by default. |
| Camoufox has a ceiling | CAPTCHAs, hard login walls and aggressive fingerprint checks can still win. No paid CAPTCHA service is used by default. |
| It does not rotate proxies by default | One identity per session. A fresh IP may be needed after repeated challenges. |
| The catalogs are snapshots | Stars, report totals and thread counts move. The date travels with every number. |
| It cannot judge a technique | `extract.py` records structure, not truth. You read the top notes and replay the request. |
| Deep tooling is external | Ghidra, Binary Ninja, IDA, rizin, capa, FLOSS, AFL++, unblob, EMBA, MobSF and YARA need their own install and, in some cases, a license. |
| Mobile runtime work needs a device | Frida hooks need an emulator or phone, a matching Frida server and a debuggable target. |
| Linux is the tested platform | Windows and macOS artifact paths exist, but the optional toolchain is documented for Linux. |
| The dashboard is single-user | Loopback only, no login, no database server. Do not expose it without a proxy and auth. |
| No backend and no telemetry | Catalogs are files. Jobs and spending stay local. Nothing is uploaded. |
| No private data | Public pages only. Report bodies that need a login are stored as public metadata and summaries. |
| No automatic submission | Beril writes Markdown and JSON. Posting to a program, a ticket or a chat is manual. |

## Quickstart

```bash
git clone https://github.com/sheduxdev/beril.git
cd beril
./install.sh
./beril scan --target https://your-app.example --profile engineer
```

The scan writes `scans/<target>.md` and `.json`. Read the Markdown file, start with the top five, and confirm the exposure before reporting it. A one-page SMB report is one flag away:

```bash
./beril scan --target https://your-app.example --profile smb --out scans/app-smb
```

Active probes and the hunt line:

```bash
./beril verify --new your-app.example
# publish the token, then
./beril verify --verify your-app.example
./beril scan --target https://your-app.example --active --profile bugbounty

./beril hunt --target ./some-open-source-repo --sandbox --report HUNT.md
```

Read `docs/defending.md` and `docs/attacking.md` before the first real target. The ownership flow is in `docs/verification.md`.

For research instead of a scan:

```bash
./beril harvest forums --sources 0x00sec,htb,reddit,hackerone --limit 20
./beril harvest experts --sources curated,hackerone,portswigger --limit 40
./beril harvest tools --sources canonical --limit 60
./beril harvest methods --limit 20
./beril extract --input data/methods.jsonl --out data/method_details.jsonl --limit 25
./beril dossier
./beril validate
```

Then open `examples/dossier.md`.

### Manual install

Python 3.11.5 or newer is required. The Camoufox browser needs about 300 MB. On headless Linux, install `xvfb` for the headful fallback.

With uv:

```bash
uv sync --extra dev
uv run camoufox fetch
uv run pytest
uv run python scripts/validate.py
```

With venv and pip:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
camoufox fetch
./beril validate
./beril dossier
```

`pyproject.toml` is the dependency source of truth. `requirements.txt` and `requirements-re.txt` stay as compatibility mirrors for pip and `./install.sh --re`. The dev extras add ruff, pyright and pytest.

Tested detector numbers, including the poor ones, are in `docs/benchmarks.md`.

Other install paths: `pipx install .`, a wheel, a pinned container image and a composite GitHub Action. `docs/deployment.md` has the commands, the offline defaults and the writable-directory note for containers.

## Scan coverage

### Web, passive

| Group | Checks |
|---|---|
| Headers | HSTS and max-age, CSP presence and weak directives, XCTO, frame, referrer, permissions, COOP, CORP, banner leaks |
| Cookies | `Secure`, `HttpOnly`, `SameSite`, per cookie |
| CORS | `*` plus credentials, origin reflection, `null` |
| Paths | 35 paths: `.git`, `.env` and variants, VCS metadata, backups, SQL dumps, server-status, phpinfo, `.DS_Store`, manifests, Actuator, Swagger/OpenAPI, GraphQL, phpMyAdmin, Adminer, WordPress/Joomla/Drupal admin and login, security.txt, robots.txt, sitemap |
| Transport | TLS version, issuer, subject, expiry, SAN list, HTTP to HTTPS |
| Mail | SPF presence and policy, DMARC presence and policy, common DKIM selectors |
| Network | 3306, 5432, 27017, 6379, 9200, 11211, 2375, 8080 with banner |
| Page | Status, title, generator and framework hints, SQL error signatures, debug traces, directory listing, password form over HTTP, source map hints |
| Soft 404 | Two random paths calibrate the baseline so a friendly 404 is not a finding |

The scanner sends `GET` requests with a Beril user agent, reads at most 400 KB per response, honors robots.txt, defaults to 2 requests per second and 250 requests, and backs off on 429/503.

### Web, active (ownership gated)

Per discovered parameter: one quote for SQL error signatures, one `<beril9f7z>` marker for reflection, one protocol relative URL on redirect parameters, one `../../etc/passwd` on file parameters. Plus OPTIONS and TRACE. No writes.

### Artifacts, static

| Type | Checks |
|---|---|
| APK | Manifest, exported components, permissions, deep links, hardcoded secrets, dangerous API calls, backup and debuggable flags, native libs |
| IPA | `Info.plist`, URL schemes, ATS exceptions, embedded frameworks, secrets and entitlement clues |
| PE | Headers, sections, imports, signing clues, mitigation flags, embedded strings, secrets |
| ELF | Architecture, bits, RELRO, NX, PIE, canaries, imports, strings, SUID, secrets |
| JAR | `plugin.yml`, IOC files, class strings, external URLs, Base64, nesting, obfuscation, hash |
| Source | Secret patterns and history, 25 source rules, dangerous sinks, dependency and OSV match, Docker and CI review, fan-in |
| Archive | Zip and tar traversal, links, nested artifacts, text secrets |

`--tools` adds semgrep and gitleaks when they are installed. `--deep` routes a binary through the optional triage passes. `--vibe`, `--mcp` and `--sbom` add the matching passes.

## Commands

| Command | What it does |
|---|---|
| `./beril scan --target <url-or-path>` | Passive web or static artifact scan |
| `./beril scan ... --fail-on high` | Exit 1 when a finding is at or above the threshold |
| `./beril scan ... --baseline old.json` | Suppress findings already in the baseline |
| `./beril scan ... --suppress .berilignore` | Apply reviewed ignores with a reason and expiry |
| `./beril mcp --target .` | MCP config plus skill, agent and plugin manifest checks |
| `./beril scan ... --render` | Run passive checks on a JavaScript-rendered page |
| `./beril scan --target <url> --active` | Minimal active probes, ownership gated |
| `./beril scan --target <url> --profile smb` | One-page SMB report with KVKK note |
| `./beril verify --new <host>` | Issue an ownership token and show the three publish paths |
| `./beril secrets --target <dir> --history` | Masked secret scan including git history |
| `./beril mcp --target <dir>` | MCP configuration linter |
| `./beril jar --target <jar-or-dir>` | Minecraft plugin and JAR triage |
| `./beril vibe --target <dir>` | Supabase RLS and client secret checks |
| `./beril deps --target <dir> --reachability` | Dependency inventory and OSV match |
| `./beril sbom --target <dir> --out <file>` | CycloneDX SBOM, optional SPDX and OpenVEX, license table |
| `./beril bgp --prefix <cidr>` | Passive BGP, RIS and RPKI posture lookup |
| `./beril run --target <url-or-dir>` | Run installed Nuclei, Semgrep, Trivy, Gitleaks, OSV, Grype, testssl, ZAP |
| `./beril ingest --input <file> --format <fmt>` | Merge SARIF, Nuclei, Trivy, Gitleaks, OSV, Grype or ZAP output |
| `./beril watch --target <url>` | Continuous scan, baseline diff and webhook |
| `./beril infra --target <dir>` | Terraform, K8s, Docker and CloudFormation review |
| `./beril image --target <image>` | Trivy, Grype and Syft image pass |
| `./beril netcheck --target <dir>` | Exported sshd, nftables, DNS and proxy config audit |
| `./beril feeds --online` | Refresh or inspect the KEV, EPSS and OSV cache |
| `./beril benchmark` | Precision and recall on the labeled offline corpora |
| `./beril health --target <dir>` | Open source maintenance scorecard with reasons |
| `./beril evidence --target <dir>` | Claim, source, status and hash dossier |
| `./beril incidents list` | Published incident cases with a rule and a lab |
| `./beril hunt --target <repo> --sandbox` | Local bug hunt with sanitizers |
| `./beril report --input <json> --profile <p>` | Render engineer, bugbounty, SMB, maintainer, CRA, JSON or SARIF |
| `./beril guard --text <file>` | Prompt injection risk for harvested text |
| `./beril scan --target <path> --deep` | Scan plus capa, FLOSS and rizin |
| `./beril re --target <binary> --capa --floss --rizin` | Explicit binary triage |
| `./beril harvest <layer>` | Collect threads, experts, tools or methods |
| `./beril extract` | Turn URLs into structure notes |
| `./beril dossier` | Rebuild `examples/dossier.md` |
| `./beril validate` | Schema, link and prose checks |
| `./beril train --status` | Curriculum progress |
| `./beril labs --run [name]` | Run one lab or all smoke tests |
| `./beril reflect` | Save a lab finding as a method note |
| `./beril github` | Refresh the GitHub atlas |
| `./beril dashboard` | Start the local dashboard |
| `./beril job list` | Read the job and cost ledger |

`python scripts/validate.py --links --max-links 40` also checks links. Run it before a pull request.

## Catalogs

| Layer | Rows | Question it answers |
|---|---:|---|
| Threads and reports | 556 | What is being found now? |
| Experts | 94 | Who knows this best? |
| Tools | 658 | What should I run? |
| GitHub atlas | 2,064 | What exists to build or study? |
| Methods | 191 | How do they do it? |

The tool count is 88 curated tools plus 570 reverse-engineering tools. Star counts, bounty totals and thread counts are dated snapshots. `references/source-catalog.md` lists every endpoint, refresh cadence and known gap.

Refresh the GitHub atlas with an authenticated token:

```bash
GITHUB_TOKEN=$(gh auth token) ./scripts/github_sweep.py --out data/github_atlas.jsonl
# or
make github
```

## Memory

Beril recalls before it researches. `knowledge/` holds 272 testable cards; `knowledge/INDEX.md` is the entry point. A fresh high or medium card closes a decision for 180 or 90 days. Stale cards are refreshed, missing ones are researched and added.

```bash
./beril recall "idor owner check" --decide
./beril remember add --title "..." --claim "..." --test "..." --proof "..." --failure "..." --tags web,idor
```

What Beril does not know sits in `knowledge/GAPS.md`, ranked. `./beril gaps --next` shows the next high gap. See `docs/memory.md`.

## Dashboard

![dashboard](assets/dashboard.png)

```bash
./beril dashboard
```

`127.0.0.1:8788`. Orbit, Apple HIG and Material 3 design rules, light and dark by system, responsive down to a phone, no framework, no build step, loopback only. Tracks spend, jobs, tokens, budget, labs, scans and every catalog. Ten labs run from the UI. Scans run read-only. `/` filters, `Ctrl K` jumps to any page. See `docs/dashboard.md`.

## Use with any agent

Every major coding agent has an entry file: `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `OPENAI.md`, `.cursor/rules/beril.mdc`, `.windsurf/rules/beril.md`, `.clinerules/beril.md`, `.github/copilot-instructions.md`, `.aider.conf.yml` and `llms.txt`.

Install the routers into another project:

```bash
./scripts/install_agent_files.py --target ~/code/myapp --agents claude,cursor,copilot
```

The files stay short on purpose. They route to `SKILL.md` and the matching reference. See `docs/agents.md`.

## Research loop

1. **Scope.** One sentence, one target class, one time window.
2. **Collect.** Camoufox reads RSS, JSON, shadow DOM and challenge pages. Every response is cached by URL hash.
3. **Extract.** Headings, intro, code block count and table count separate a method from a news item.
4. **Verify.** A method card needs a precondition, a minimal request, an observable proof and a failure mode.
5. **Write.** The dossier links every claim. Observations and inferences sit in separate sentences.
6. **Refresh.** Weekly for reports and threads, monthly for tools, quarterly for standards.

Read `SKILL.md` for the full loop and the quality gates. `references/camoufox-playbook.md` has the browser settings, challenge ladder, site recipes and failure modes.

## Training and labs

```bash
./beril train --status
./beril train --week 1
./beril labs --run
```

The curriculum runs from the shell to ROP, heap, AD, firmware and AI security. Ten labs are local and runnable. Each has a README, tasks, a smoke test and an answer key.

| Lab | Topic |
|---|---|
| `web` | IDOR, XSS, SQLi, traversal, SSRF, weak auth |
| `binary` | stack, format string, UAF, integer, mitigations |
| `fuzz` | libFuzzer harness and crash triage |
| `re` | stripped binary, static reconstruction |
| `mobile` | exported components, deep link, JS bridge |
| `firmware` | extraction, CGI injection, update signing |
| `cloud` | Terraform, pod, Dockerfile review |
| `ad` | ACL paths, Kerberoast, ADCS ESC1 |
| `llm` | prompt injection, RAG leak, exfil |
| `detection` | Sigma rule and log triage |

`./beril reflect` turns a lab result into a note with a root cause and a fix. Progress lives in `training/` and does not enter git. Start at `docs/training.md` and `references/curriculum.md`.

The network defense track is separate from the 25-week curriculum:

- `references/network-visibility.md`: flow, packet, DNS, IDS, eBPF and honeypot telemetry, with what each source misses.
- `references/network-protection.md`: segmentation, egress, management plane, DDoS, WAF, DNS, TLS and recovery, with a test per control.
- `references/network-checklist.md`: 50 controls and evidence lines for a quarterly pass.
- `references/bgp-security.md`: hijack, route leak, RPKI, filtering and BMP, with tests.
- `references/network-toolkit.md`: tools by question, limits and safety.
- `references/network-curriculum.md`: an eight-week lab track.
- `docs/network-runbook.md`: incident scope and containment order.
- `docs/automation.md`: adapters, auth headers, ingest, watch and CI.
- `docs/suppression.md`: baseline and reviewed ignore file.
- `docs/mcp-supply-chain.md`: MCP, skill and plugin manifest checks.
- `docs/project-health.md`: supplier and repository health signals.
- `references/evidence-dossier.md`: journalism and OSINT claim format.
- `references/incident-library.md`: incident cases, source policy and drills.
- `docs/bgp-runbook.md`: hijack confirmation and mitigation.
- `references/gap-map.md`: what Beril still lacks and what to train next.
- `references/competitive-gap-analysis.md`: score against ZAP, Nuclei, Semgrep, Trivy, TruffleHog, Prowler, Wazuh, Strix and others.
- `references/research-log-2026-11-23.md`: what was read and what stays unverified.

## Reverse engineering

```bash
./install.sh --re
./beril scan --target ./sample --deep
./beril re --target ./sample --capa --floss --rizin
./scripts/ghidra_headless.sh ./sample out.json
./scripts/patch_diff.sh ghidriff old.bin new.bin
```

`--deep` runs every installed optional pass and keeps the static result. Ghidra needs `GHIDRA_HOME`. Binary Ninja needs a license and `install_api.py`. The reference set covers Ghidra, GhidRust, Ghidrust, Binary Ninja, IDA, rizin, x64dbg, WinDbg, GDB, Frida, angr, capa, FLOSS, AFL++, CASR, unblob, EMBA and MobSF.

- `references/reverse-engineering.md`
- `references/vulnerability-research.md`
- `references/fuzzing.md`
- `references/exploit-development.md`
- `references/mobile-reverse.md`
- `references/firmware-iot.md`
- `references/ghidra-ecosystem.md`
- `references/rust-reverse.md`
- `references/re-plugin-index.md`

## Evidence rules

- Every row has a public URL and a collection timestamp.
- A technique claim needs one grade A source or two independent grade B sources.
- Star counts and report totals are snapshots. The date travels with the number.
- No private reports, credentials, tokens or personal data.
- A dead link is noted, not hidden.
- A method card names a precondition, a minimal request, a proof and a failure mode.
- Prose follows the humanizer rules: no em dashes, no forced triads, no inflated significance.

A finding needs a reproducible artifact: a request and response, a crash input, a diff or a file path. A scanner line alone is not a finding.

## Example output

`examples/dossier.md` is generated from the snapshot. It shows coverage, high-signal threads, expert reading, a tool shelf, a method index and the gaps left for the next pass. `examples/scan-example.md` and `examples/scan-artifact-example.md` show the scan report shape.

## CI gate

A scan can fail a pipeline and a known finding can stay quiet:

```bash
# First run writes the baseline
./beril scan --target https://staging.example --out scans/staging
# Later runs fail only on new high or critical findings
./beril scan --target https://staging.example --baseline scans/staging.json --fail-on high --sarif
```

The baseline matches by finding id and by check plus subject. The count is written in
`meta.suppressed`, so a report still says how much it hid. The same flags work on
`bgp`. Exit code 0 means no finding at or above the threshold, 1 means one exists.

## Tests and quality gates

```bash
./install.sh --dev
ruff check scripts tests
ruff format --check scripts tests
pyright
python -m pytest -q
./beril validate
```

The suite has 189 tests. It covers the finding model, dedupe, priority, renderers, SARIF schema checks, secret masking and placeholders, the ownership gate, scope matching, the active probes, MCP rules and supply checks, RLS rules, JAR triage, dependency reachability, archive traversal, feed cache and fallback, SBOM with SPDX and OpenVEX, the BGP lookup, adapters, ingest, infra, netcheck, watch, plugins, suppression, the incident library, AST rules, project health, the evidence dossier, packaging and the prompt guard. Web tests run against a local fixture only. Ruff and pyright are pinned to the versions CI uses.

## Safety model

| Control | Behavior |
|---|---|
| Passive default | Nothing runs active without a record |
| Ownership | DNS TXT, well-known file or meta tag, stored with an expiry |
| Scope | Host, wildcard or path allowlist; out of scope means no request |
| Budget | 250 requests, 2 requests per second, backoff on 429/503 |
| Non-destructive | GET only, four tiny patterns, no write |
| Secrets | Masked in every output, no full key on disk |
| Static artifacts | Files read, never executed |
| Hunt sandbox | Network off, read-only source, dropped caps, resource caps |
| Prompt injection | Harvested text wrapped as data, risk scored |
| Local first | No telemetry, no backend, dashboard loopback |

Scan a host only when you own it or have scope for it. Testing a technique from the catalog still requires authorization. A method card is not a license. A clean scan is not a certification.

## Repository layout

```text
beril/
├── SKILL.md                 # agent-facing skill
├── AGENTS.md                # generic agent entry
├── scripts/                 # scan, secrets, MCP, JAR, vibe, deps, hunt, report, RE, dossier
├── tests/                   # regression suite and local fixtures
├── references/              # method cards, finding schema, maintainer template, RE
├── agents/                  # role prompts
├── labs/                    # ten local targets
├── docs/                    # attacking, defending, verification, report format
├── data/                    # catalogs plus KEV, EPSS, rule and IOC seeds
├── assets/                  # banner and dashboard preview
├── examples/                # generated dossier and sample scans
├── install.sh
└── beril                    # command wrapper
```

## Research base

The build downloaded 44 public repositories and found 22,976 `SKILL.md` files across 21 of them. The total was about 3.1 GB of shallow clones. Several repositories vendor the same skills, so the unique count is lower.

The upstream corpus includes broad libraries such as `mukul975/anthropic-cybersecurity-skills` and `ComeOnOliver/skillshub`, focused packs such as `uphiago/recon-skills` and `Security-Talent/bugskill-ai`, agent systems such as `KeygraphHQ/shannon` and `vxcontrol/pentagi`, and reference data such as `swisskyrepo/PayloadsAllTheThings` and `danielmiessler/SecLists`.

`references/source-catalog.md` has the full list, per-repository counts and roles.

## Companion projects

- [Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter): 83 bounty skills, triage gates and report patterns. Notes: `references/claude-bughunter.md`.
- [ARTEX](https://github.com/BaaRai/ARTEX): autonomous multi-agent pentest runner with evidence graphs. Notes: `references/artex.md`.

Beril supplies the knowledge, scan and evidence layer. The companions supply execution and class-specific hunt patterns.

## Sponsors

Beril is free, MIT licensed and maintained in public. Sponsorship pays for browser runs, CI minutes and lab hardware. Sponsors are listed here as they join.

[![Sponsor Beril](https://img.shields.io/badge/Sponsor-%40sheduxdev-2f6f4e?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/sheduxdev)

## Contributors

- Deniz USTA ([@sheduxdev](https://github.com/sheduxdev)): author and maintainer.
- Everyone who has landed a commit: [contribution graph](https://github.com/sheduxdev/beril/graphs/contributors).
- The maintainers of the 44 upstream repositories, credited in `references/source-catalog.md`.

Useful contributions:

- a new source with a tested endpoint and a note on its access limits;
- a correction to a method card with a primary link;
- a tool entry with a verified install command;
- a failure mode that the playbook does not cover.

Keep the schema, date your snapshot and run `./beril validate` before opening a pull request. The full checklist is in `CONTRIBUTING.md`. Report a vulnerability in Beril through `SECURITY.md`.

## Versioning

Beril uses semantic versioning. The current release is `1.4.0`, which adds the two-line model: ownership gated active probes, the unified finding and report schema, secret scanning with revocation order, KEV/EPSS priority, MCP and JAR triage, the Supabase/RLS pass, the hunt sandbox, SARIF, and the regression suite.

Tags and release notes: https://github.com/sheduxdev/beril/tags

## The name

Beril is a person, not an acronym. She has green eyes and likes pistachios, so the banner does too. The rest of the repository is evidence.

## License

MIT for the code and original prose. The linked sources and cloned repositories keep their own licenses. See `LICENSE`.

The banner is in `assets/beril.webp`, with a PNG fallback in `assets/beril.png`. The GitHub social preview is `assets/social-preview.jpg`.

## Turkey and KVKK

Beril keeps a one-page profile for small businesses in Turkey. The `smb`
profile renders a traffic light, at most five actions and a KVKK note for a
non-technical reader.

```bash
./beril scan --target https://your-app.example --profile smb --out scans/summary
```

KVKK requires a breach notification within 72 hours. If a finding can expose
personal data, the summary points to that duty and to the article 12 duty of
care.

The legal frame in `docs/legal.md` covers TCK 243, TCK 244 and Cybersecurity
Law 7545. It is not legal advice.
