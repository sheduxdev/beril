![Beril, green eyes and pistachio](assets/beril.webp)

# Beril

A local-first cybersecurity intelligence skill for agents and people. Beril reads the security sites that block plain HTTP clients, keeps every lead with a date and a public URL, and turns the result into a dossier with a reading queue, a tool shelf and method cards. The same repository carries ten practice labs, a 25-week training plan, a read-only scan pass for apps you own and a static triage pass for local artifacts.

[![version](https://img.shields.io/github/v/tag/sheduxdev/beril?sort=semver&label=version&color=2f6f4e)](https://github.com/sheduxdev/beril/tags)
![license](https://img.shields.io/badge/license-MIT-2f6f4e)
![python](https://img.shields.io/badge/python-3.10%2B-2f6f4e)
[![validate](https://github.com/sheduxdev/beril/actions/workflows/validate.yml/badge.svg)](https://github.com/sheduxdev/beril/actions/workflows/validate.yml)
[![stars](https://img.shields.io/github/stars/sheduxdev/beril?style=flat&color=2f6f4e)](https://github.com/sheduxdev/beril/stargazers)

Current release: **1.3.0**. Snapshot date: **2026-11-22**.

Beril was built from 44 public security skill repositories and a live collection pass over forums, disclosed reports, researcher blogs and GitHub tool shelves. Every catalog row links to its origin. The snapshot is a sample with a date, not a census.

## What it is

| Layer | What it does |
|---|---|
| Skill | `SKILL.md` gives an agent the research loop, entity schemas, browser rules and quality gates. |
| Router files | `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, Cursor, Windsurf, Cline, Copilot and Aider files point an agent at the skill without pasting it five times. |
| CLI | `./beril` wraps harvest, extract, dossier, validate, scan, reverse-engineering triage, labs, training and the dashboard. |
| Catalogs | Dated JSONL for threads, experts, tools, methods and the GitHub atlas. |
| Dossier | A Markdown brief with ranked leads, coverage, a tool shelf and the gaps left for the next pass. |
| Labs | Ten local targets with tasks, smoke tests and answer keys. |
| Dashboard | A loopback-only workspace for jobs, spend, scans, labs and every catalog. |

## What it does

| Job | Behavior | Entry point |
|---|---|---|
| Collect public leads | Camoufox reads RSS, JSON, shadow DOM and challenge pages. Responses are cached by URL hash. | `./beril harvest forums`, `experts`, `tools`, `methods`, `all` |
| Extract structure | Records headings, intro, code block count and table count so a method can be separated from a news item. | `./beril extract` |
| Build a dossier | Merges the catalogs into a ranked brief with links and explicit gaps. | `./beril dossier` |
| Map the tool shelf | Sweeps GitHub topics for security repositories with stars, language, license and last push. | `./beril github` |
| Scan your web app | Read-only checks for six headers, eleven exposed paths, TLS, cookies, password forms and fingerprints. | `./beril scan --target https://your-app.example` |
| Scan an artifact | Static review of an APK, IPA, PE, ELF, archive or source tree. Manifests, hardening, secrets, dangerous sinks and archive paths. | `./beril scan --target ./build/app.apk` |
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
| It does not exploit anything | The scan finds missing headers, exposed paths and static sinks. It does not log in, inject payloads, fuzz parameters or confirm exploitability. |
| The web scan is shallow by design | Six headers, eleven paths, TLS metadata, cookie flags and basic fingerprints. A clean result means the short list passed. |
| It is not an authenticated scanner | Private pages, dashboards and API routes behind a login are out of reach unless the path is public. |
| Artifact scans are static | Samples are read, not executed. Packed, encrypted or heavily obfuscated files can hide most behavior. |
| There is no sandbox | A local binary is parsed and hashed. Deep passes call external tools on the host. |
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
./beril scan --target https://your-app.example
```

The scan writes `scans/<target>.md` and `.json`. Read the Markdown file, start with the top severity, and confirm the exposure before reporting it.

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

Python 3.10 or newer is required. The Camoufox browser needs about 300 MB. On headless Linux, install `xvfb` for the headful fallback.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
camoufox fetch
./beril validate
./beril dossier
```

`requirements.txt` includes the scanners and parsers. `requirements-re.txt` adds the reverse-engineering Python packages and is installed by `./install.sh --re`.

## Scan coverage

### Web, read-only

| Group | Checks |
|---|---|
| Headers | `strict-transport-security`, `content-security-policy`, `x-content-type-options`, `x-frame-options`, `referrer-policy`, `permissions-policy` |
| Paths | `/.git/HEAD`, `/.env`, `/.svn/entries`, `/backup.zip`, `/server-status`, `/phpinfo.php`, `/actuator/health`, `/openapi.json`, `/swagger-ui/`, `/graphql`, `/.well-known/security.txt` |
| Transport | TLS version, issuer, subject, expiry, SAN list |
| Cookies | `Secure`, `HttpOnly`, `SameSite` flags and scope |
| Page | Status, title, password form over plain HTTP, framework fingerprints |

The scanner sends `GET` requests with a Beril user agent and reads at most 400 KB per response. It does not read `robots.txt` for you: check that file and the program scope yourself.

### Artifacts, static

| Type | Checks |
|---|---|
| APK | Manifest, exported components, permissions, deep links, hardcoded secrets, dangerous API calls, backup and debuggable flags, native libs |
| IPA | `Info.plist`, URL schemes, ATS exceptions, embedded frameworks, secrets and entitlement clues |
| PE | Headers, sections, imports, signing clues, mitigation flags, embedded strings and overlay |
| ELF | Architecture, bits, RELRO, NX, PIE, canaries, imports, strings and hardening gaps |
| Source | Secret patterns, dangerous sinks by language, dependency manifests, Docker and CI review |
| Archive | Zip and tar traversal, nested artifacts, file type mix |

`--tools` adds semgrep, gitleaks and trivy when they are installed. `--deep` routes a binary through the optional triage passes.

## Commands

| Command | What it does |
|---|---|
| `./beril scan --target <url-or-path>` | Read-only web or artifact scan |
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
| Methods | 156 | How do they do it? |

The tool count is 88 curated tools plus 570 reverse-engineering tools. Star counts, bounty totals and thread counts are dated snapshots. `references/source-catalog.md` lists every endpoint, refresh cadence and known gap.

Refresh the GitHub atlas with an authenticated token:

```bash
GITHUB_TOKEN=$(gh auth token) ./scripts/github_sweep.py --out data/github_atlas.jsonl
# or
make github
```

## Dashboard

![dashboard](assets/dashboard.png)

```bash
./beril dashboard
```

`127.0.0.1:8788`. Dark only, no framework, no build step, loopback only. Tracks spend, jobs, tokens, budget, labs, scans and every catalog. Ten labs run from the UI. Scans run read-only. `/` focuses search. See `docs/dashboard.md`.

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

## Safety

Beril only reads. The web scan sends plain `GET` requests. It does not log in, fuzz or exploit. The artifact scan does not execute a sample. The dashboard binds loopback and has no login.

Scan a host only when you own it or have scope for it. Testing a technique from the catalog still requires authorization. A method card is not a license.

## Repository layout

```text
beril/
├── SKILL.md                 # agent-facing skill
├── AGENTS.md                # generic agent entry
├── scripts/                 # harvest, scan, RE triage, dossier, labs, dashboard
├── references/              # method cards, tooling, RE, curriculum, source catalog
├── agents/                  # role prompts
├── labs/                    # ten local targets
├── docs/                    # runbooks and walkthroughs
├── data/                    # dated JSONL snapshot
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

Keep the schema, date your snapshot and run `./beril validate` before opening a pull request.

## Versioning

Beril uses semantic versioning. The current release is `1.3.0`, which adds the dark dashboard, the GitHub security atlas and a 570-entry reverse-engineering plugin index. The previous tag is `v1.2.0`.

Tags and release notes: https://github.com/sheduxdev/beril/tags

## The name

Beril is a person, not an acronym. She has green eyes and likes pistachios, so the banner does too. The rest of the repository is evidence.

## License

MIT for the code and original prose. The linked sources and cloned repositories keep their own licenses. See `LICENSE`.

The banner is in `assets/beril.webp`, with a PNG fallback in `assets/beril.png`. The GitHub social preview is `assets/social-preview.jpg`.

## Türkçe

Beril, ajanlar ve insanlar için yerel çalışan bir siber güvenlik araştırma becerisidir. Camoufox ile forumları, açıklanmış raporları, araştırmacıları ve araçları toplar. Bulduğunu tarih ve genel bağlantıyla saklar. Sonunda okunabilir bir dosya üretir.

Aynı depoda on yerel lab, 25 haftalık eğitim planı, sahip olduğun uygulamalar için salt okunur tarama ve yerel dosyalar için statik inceleme var.

```bash
git clone https://github.com/sheduxdev/beril.git
cd beril
./install.sh
./beril scan --target https://uygulaman.example
```

Tarama yalnızca okur. Giriş yapmaz, payload göndermez, örnek çalıştırmaz. Temiz sonuç, kısa listenin geçtiği anlamına gelir.

Kurulum, tarama ve raporlama için `docs/one-click.md` dosyasına bak. Araştırma döngüsü `SKILL.md` içinde. Kaynak listesi `references/source-catalog.md`, metot kartları `references/techniques.md`, eğitim planı `references/curriculum.md` ve veri anlık görüntüsü `data/` altında.
