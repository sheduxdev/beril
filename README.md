# Beril

![Beril, green eyes and pistachio](assets/beril.webp)

A cybersecurity intelligence skill that reads the web with Camoufox, keeps what it finds as evidence-linked catalogs, and turns the result into a dossier a human can act on. The palette is pistachio green and the eyes are green, because the project is named after someone who likes both.

Beril was built from 43 public security skill repositories and a live collection pass over forums, disclosed reports, researcher blogs, and GitHub tool shelves.

## Why it exists

Two problems get in the way. Security sites block plain HTTP clients, and the reading lists people keep are stale or unsourced. Beril uses Camoufox for the first, stores every item with a date and URL for the second, and turns the result into a short dossier with a reading queue, a tool shelf, and method cards that name a precondition and a proof.

## What's inside

```text
beril/
├── SKILL.md                     # the agent-facing skill
├── AGENTS.md                    # generic agent entry
├── CLAUDE.md                    # Claude Code entry
├── GEMINI.md                    # Gemini CLI entry
├── llms.txt                     # LLM index
├── scripts/
│   ├── camo.py                  # Camoufox session, cache, parsing helpers
│   ├── harvest.py               # forums, experts, tools, methods
│   ├── extract.py               # headings, intros, code density
│   ├── scan.py                  # URL or artifact router
│   ├── scan_app.py              # read-only web scan
│   ├── scan_artifact.py         # APK, IPA, PE, ELF, archive, source scan
│   ├── re_triage.py             # capa, FLOSS, rizin, Ghidra passes
│   ├── ghidra_dump.py           # Ghidra postscript
│   ├── ghidra_headless.sh       # Ghidra wrapper
│   ├── rizin_triage.sh          # rizin JSON triage
│   ├── patch_diff.sh            # Ghidra/BinDiff/git diff helper
│   ├── frida_hook.js            # mobile hook template
│   ├── afl_harness.c            # fuzzing harness template
│   ├── train.py                 # curriculum coach and progress
│   ├── labs.py                  # lab runner
│   ├── build_dossier.py         # JSONL -> Markdown brief
│   └── validate.py              # schema, links, prose checks
├── install.sh                   # one-click setup
├── beril                        # command wrapper
├── docs/one-click.md            # install and scan without the terminal
├── docs/scan-artifacts.md       # APK, binary and source review
├── docs/reverse-engineering.md  # deep binary workflow
├── docs/training.md             # how to train with Beril
├── docs/agents.md               # agent file matrix and installer
├── docs/break-my-app.md         # request-to-report runbook
├── references/
│   ├── camoufox-playbook.md     # challenge ladder and site recipes
│   ├── forums.md                # community catalog
│   ├── experts.md               # researcher profiles and methods
│   ├── tooling.md               # phase map and commands
│   ├── techniques.md            # 25 method cards
│   ├── reverse-engineering.md   # Ghidra, Binary Ninja, IDA, debuggers
│   ├── vulnerability-research.md # bug classes, triage, exploitability
│   ├── fuzzing.md               # harnesses, AFL++, sanitisers, CI
│   ├── exploit-development.md   # ROP, heap, UAF, mitigations
│   ├── mobile-reverse.md        # Android and iOS
│   ├── firmware-iot.md          # extraction, emulation, hardware
│   ├── curriculum.md            # 25-week training plan
│   ├── exercises.md             # 68 drills by domain
│   ├── source-catalog.md        # provenance and upstream repos
│   ├── dossier-template.md      # output structure
│   └── scoring.md               # ranking rules
├── agents/                      # research, RE, crash, fuzzing, firmware, mentor prompts
├── labs/                        # web, binary, fuzz, RE, mobile, firmware, cloud
├── assets/                      # banner and social preview
├── data/                        # snapshot catalogs
├── examples/dossier.md          # generated sample brief
├── examples/scan-example.md     # sample web scan
├── examples/scan-artifact-example.md  # sample source scan
└── requirements.txt
```

## One-click scan

```bash
git clone https://github.com/sheduxdev/beril.git
cd beril
./install.sh
./beril scan --target https://your-app.example
```

The scan is read-only and works on a URL, APK, IPA, PE/EXE/DLL, ELF binary, archive, or source tree. For web targets it checks headers, TLS, cookies, a short list of exposed paths, and fingerprints. For artifacts it reads the manifest or binary, finds secrets and dangerous sinks, and checks hardening flags. Open the Markdown report in `scans/`. See `docs/one-click.md` and `docs/scan-artifacts.md` for the walkthrough and the limits.

```bash
./beril scan --target ./build/app.apk
./beril scan --target ./source --tools
./beril scan --target ./release/app.exe
```

Optional known-CVE pass, if nuclei is installed:

```bash
nuclei -u https://your-app.example -severity medium,high,critical \
  -tags cve,exposure,misconfig -o scans/nuclei.txt
```

## Use with any agent

Every major coding agent has an entry file: `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.cursor/rules/beril.mdc`, `.windsurf/rules/beril.md`, `.clinerules/beril.md`, `.github/copilot-instructions.md`, `.aider.conf.yml`, and `llms.txt`.

Install the routers into another project:

```bash
./scripts/install_agent_files.py --target ~/code/myapp --agents claude,cursor,copilot
```

The files route to `SKILL.md` and the matching reference. They stay short on purpose. See `docs/agents.md`.

## Training

A 25-week curriculum with local labs, drills, checkpoints, and grading rubrics. It runs from the shell to ROP, heap, AD, firmware, and AI security.

```bash
./beril train --status
./beril train --week 1
./beril labs --run web
```

Seven labs are local and runnable: web, binary, fuzz, RE, mobile, firmware, cloud. Each has tasks, a smoke test, and an answer key. Start at `docs/training.md` and `references/curriculum.md`.

## Reverse engineering and exploit development

```bash
./install.sh --re
./beril scan --target ./sample --deep
./beril re --target ./sample --capa --floss --rizin
./scripts/ghidra_headless.sh ./sample out.json
./scripts/patch_diff.sh ghidriff old.bin new.bin
```

`--deep` runs every installed optional pass and keeps the static result. `re` is the same with explicit tool flags. Ghidra needs `GHIDRA_HOME`; Binary Ninja needs a license and `install_api.py`.

The reference set covers Ghidra, Binary Ninja, IDA, rizin, x64dbg, WinDbg, GDB, Frida, angr, capa, FLOSS, AFL++, CASR, unblob, EMBA, MobSF, and the workflows around them:

- `references/reverse-engineering.md`
- `references/vulnerability-research.md`
- `references/fuzzing.md`
- `references/exploit-development.md`
- `references/mobile-reverse.md`
- `references/firmware-iot.md`

## Manual quick start

```bash
git clone https://github.com/sheduxdev/beril.git
cd beril

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
camoufox fetch

python scripts/validate.py
python scripts/build_dossier.py --data data --out examples/dossier.md
```

Then refresh one layer:

```bash
python scripts/harvest.py forums --sources 0x00sec,htb,reddit,hackerone --limit 20
python scripts/harvest.py experts --sources curated,hackerone,portswigger --limit 40
python scripts/harvest.py tools --sources canonical --limit 60
python scripts/harvest.py methods --limit 20
```

Or use the short targets:

```bash
make validate
make dossier
make forums
```

Read `SKILL.md` for the full loop and the quality gates.

## Research loop

1. **Scope.** One sentence, one target class, one time window.
2. **Collect.** Camoufox reads RSS, JSON, shadow DOM, and challenge pages. Every response is cached by URL hash.
3. **Extract.** Headings, intro, code block count, and table count separate a method from a news item.
4. **Verify.** A method card needs a precondition, a minimal request, an observable proof, and a failure mode.
5. **Write.** The dossier links every claim. Observations and inferences sit in separate sentences.
6. **Refresh.** Weekly for reports and threads, monthly for tools, quarterly for standards.

## The four catalogs

| Layer | Snapshot | What it answers |
|---|---:|---|
| Threads and reports | 311 | What is being found now? |
| Experts | 94 | Who knows this best? |
| Tools | 139 | What should I run? |
| Methods | 85 | How do they do it? |

The snapshot is a sample, not a census. See `references/source-catalog.md` for endpoints, dates, and gaps.

## Camoufox

Beril uses Camoufox because ordinary HTTP clients fail on the sources that matter. The playbook covers:

- fingerprint consistency across locale, timezone, OS, and proxy;
- headless to headful escalation under Xvfb;
- persistent profiles for challenge clearance;
- Discourse JSON, Ghost RSS, Reddit shadow DOM, HackerOne's disclosure grid, GitHub stars and READMEs;
- caching, evidence snapshots, rate limits, and the failure modes that look like empty pages.

Start with `references/camoufox-playbook.md`.

## Research base

The build downloaded 43 public repositories and found 22,976 `SKILL.md` files across 21 of them. The upstream corpus includes:

- broad libraries: `mukul975/anthropic-cybersecurity-skills`, `ComeOnOliver/skillshub`;
- focused packs: `uphiago/recon-skills`, `Security-Talent/bugskill-ai`, `penligent/AIPentest_Skills`;
- agent systems: `KeygraphHQ/shannon`, `usestrix/strix`, `vxcontrol/pentagi`, `xalgorix/xalgorix`;
- reference data: `swisskyrepo/PayloadsAllTheThings`, `danielmiessler/SecLists`, `arkadiyt/bounty-targets-data`.

The full list, counts, and roles are in `references/source-catalog.md`.

## Evidence rules

- Every row has a public URL and a collection timestamp.
- A technique claim needs one grade A source or two independent grade B sources.
- Star counts and report totals are snapshots. The date travels with the number.
- No private reports, credentials, tokens, or personal data.
- A dead link is noted, not hidden.
- Prose follows the humanizer rules: no em dashes, no forced triads, no inflated significance.

## Example output

`examples/dossier.md` is generated from the snapshot. It shows coverage, high-signal threads, expert reading, a tool shelf, a method index, and the gaps left for the next pass.

## Requirements

- Python 3.10 or newer
- `camoufox[geoip]`, `beautifulsoup4`, `lxml`
- About 300 MB for the Camoufox browser
- `xvfb` for the headful fallback on Linux

## The name

Beril is a person, not an acronym. She has green eyes and likes pistachios, so the banner does too. The rest of the repository is evidence.

The banner is in `assets/beril.webp` (PNG fallback in `assets/beril.png`). The GitHub social preview is `assets/social-preview.jpg`.

## License

MIT for the code and original prose. The linked sources and cloned repositories keep their own licenses. See `LICENSE`.

## Contributing

Useful contributions:

- a new source with a tested endpoint and a note on its access limits;
- a correction to a method card with a primary link;
- a tool entry with a verified install command;
- a failure mode that the playbook does not cover.

Please keep the schema, date your snapshot, and run `python scripts/validate.py` before opening a pull request.

## Türkçe

Beril, Camoufox ile siber güvenlik forumlarını, açıklanmış raporları, araştırmacıları ve araçları toplayan bir araştırma becerisidir. Bulduğunu kaynak bağlantısı ve tarihle saklar, sonunda okunabilir bir dosya üretir.

Kurulum:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
camoufox fetch
```

Kullanım için `SKILL.md` dosyasına, kaynak listesi için `references/forums.md` dosyasına bak. Metot kartları `references/techniques.md` içinde. Veri anlık görüntüsü `data/` altında.
