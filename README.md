# Beril

![Beril banner](assets/banner.svg)

A cybersecurity intelligence skill that reads the web with Camoufox, keeps what it finds as evidence-linked catalogs, and turns the result into a dossier a human can act on.

Beril was built from 43 public security skill repositories and a live collection pass over forums, disclosed reports, researcher blogs, and GitHub tool shelves.

## Why it exists

Most security reading lists are stale, unsourced, or a wall of links. Beril fixes three problems:

- **Access.** Security sites block plain HTTP clients. Camoufox gets through challenges without pretending to be a stealth service.
- **Structure.** Threads, experts, tools, and methods are stored in one schema with dates and URLs, so a claim can be traced.
- **Use.** The output is a short dossier with a reading queue, a tool shelf, and method cards that name a precondition and a proof.

## What's inside

```text
beril/
├── SKILL.md                     # the agent-facing skill
├── scripts/
│   ├── camo.py                  # Camoufox session, cache, parsing helpers
│   ├── harvest.py               # forums, experts, tools, methods
│   ├── extract.py               # headings, intros, code density
│   ├── build_dossier.py         # JSONL -> Markdown brief
│   └── validate.py              # schema, links, prose checks
├── references/
│   ├── camoufox-playbook.md     # challenge ladder and site recipes
│   ├── forums.md                # community catalog
│   ├── experts.md               # researcher profiles and methods
│   ├── tooling.md               # phase map and commands
│   ├── techniques.md            # 25 method cards
│   ├── source-catalog.md        # provenance and upstream repos
│   ├── dossier-template.md      # output structure
│   └── scoring.md               # ranking rules
├── agents/                      # parallel research prompts
├── data/                        # snapshot catalogs
├── examples/dossier.md          # generated sample brief
└── requirements.txt
```

## Quick start

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
| Threads and reports | 269 | What is being found now? |
| Experts | 94 | Who knows this best? |
| Tools | 87 | What should I run? |
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
