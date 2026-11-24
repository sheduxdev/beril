# How Beril works

Beril is a local-first skill for agents and people. It has two working lines that share one finding model.

## Two lines

| Line | Job | Gate |
|---|---|---|
| Defense | Scan an app, repository, artifact, MCP config or Minecraft plugin you own and return a ranked fix list | Passive by default |
| Attack | Hunt bugs in open source and write maintainer reports | Ownership record, scope file, networkless sandbox |

A research layer sits beside both. It reads the security sites that block plain HTTP clients, keeps every lead with a date and a public URL, and turns the result into a dossier.

## One finding model

Every check, from either line, produces a finding with the same fields:

| Field | Meaning |
|---|---|
| Severity | How bad it is if real |
| Confidence | How sure the check is. It never goes up without new evidence |
| Evidence | The request and response, file path, hash or diff that shows it |
| Impact | What an attacker gains |
| Fix | The smallest change that removes it |
| Not tested | A plain statement of what the pass did not cover |

Five renderers turn the same evidence into engineer, bugbounty, SMB, maintainer and CRA reports. JSON and SARIF are the machine outputs. See [Report format](../docs/report-format.md) and the [finding schema](../references/finding-schema.md).

## The pipeline

1. **Detect.** `scan` looks at the target and picks a path: web URL, APK, IPA, PE, ELF, JAR, archive or source tree.
2. **Gate.** Passive checks run. Active checks need an ownership record and a scope entry. Out of scope means no request.
3. **Check.** The matching passes run. Examples: headers, cookies, CORS, 35 exposed paths, TLS and mail records for a web target; manifests, hardening flags, secrets and dangerous sinks for an artifact.
4. **Merge.** Findings are deduplicated and scored. The score is severity times confidence, with verified and KEV boosts. It orders work and is not CVSS.
5. **Suppress.** A baseline or a reviewed ignore file hides known findings. The count is written to `meta.suppressed`, so a report says how much it hid.
6. **Render.** The chosen profile writes Markdown, JSON or SARIF.

## Layers

| Layer | What it is |
|---|---|
| Skill | `SKILL.md` gives an agent the loop, output contract, browser rules and quality gates |
| Router files | `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, Cursor, Windsurf, Cline, Copilot and Aider files point an agent at the skill |
| CLI | `./beril` wraps every pass |
| Gates | Ownership record, scope file, request budget, rate limit, masked secrets, static-only artifacts |
| Catalogs | Dated JSONL for threads, experts, tools, methods and the GitHub atlas |
| Memory | Small cards in `knowledge/` that an agent reads before it searches |
| Labs | Ten local targets with tasks, smoke tests and answer keys |
| Dashboard | A loopback-only workspace view for jobs, spend, scans, labs and catalogs |

## Where things live

```text
beril/
├── SKILL.md                 agent-facing skill
├── AGENTS.md                generic agent entry
├── scripts/                 scan, secrets, MCP, JAR, vibe, deps, hunt, report, RE, dossier
├── tests/                   regression suite and local fixtures
├── references/              method cards, finding schema, maintainer template, RE
├── agents/                  role prompts
├── labs/                    ten local targets
├── docs/                    attacking, defending, verification, report format
├── knowledge/               durable memory cards
├── data/                    catalogs plus KEV, EPSS, rule and IOC seeds
├── assets/                  banner and dashboard preview
├── examples/                generated dossier and sample scans
├── install.sh
└── beril                    command wrapper
```

## State

Nothing here uses a database server. State is files:

| Path | Holds | In git |
|---|---|---|
| `scans/` | Scan reports | No |
| `training/` | Progress and journal | No |
| `data/*.jsonl` | Catalogs, each row with a URL and a timestamp | Yes |
| `data/jobs.jsonl` | Append-only job ledger with actor, model, tokens and cost | Yes |
| `knowledge/` | Memory cards | Yes |

## The research loop

1. **Scope.** One sentence, one target class, one time window.
2. **Collect.** Camoufox reads RSS, JSON, shadow DOM and challenge pages. Responses are cached by URL hash.
3. **Extract.** Headings, intro, code block count and table count separate a method from a news item.
4. **Verify.** A method card needs a precondition, a minimal request, an observable proof and a failure mode.
5. **Write.** The dossier links every claim. Observations and inferences sit in separate sentences.
6. **Refresh.** Weekly for reports and threads, monthly for tools, quarterly for standards.

Before a new search, ask memory first: `./beril recall "class or target" --decide`. See [Memory](../docs/memory.md).

## Evidence rules

- Every row has a public URL and a collection timestamp.
- A technique claim needs one grade A source or two independent grade B sources.
- Star counts and report totals are snapshots. The date travels with the number.
- No private reports, credentials, tokens or personal data.
- A dead link is noted, not hidden.
- A finding needs a reproducible artifact: a request and response, a crash input, a diff or a file path. A scanner line alone is not a finding.
