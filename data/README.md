# Data snapshot

JSONL files collected on 2026-11-22 with Camoufox, plus scanner seed data on 2026-11-23. The catalog schema is documented in `SKILL.md` and `references/source-catalog.md`. The finding schema is in `references/finding-schema.md`.

| File | Rows | Contents |
|---|---:|---|
| `threads.jsonl` | 556 | Forum threads, disclosed reports, article leads |
| `experts.jsonl` | 94 | Named researchers, handles, and public works |
| `canonical_tools.jsonl` | 88 | Curated tools with install commands |
| `methods.jsonl` | 191 | Method and research URLs |
| `method_details.jsonl` | 73 | Headings, intros, code density |
| `thread_details.jsonl` | 38 | Extracted thread and report notes |
| `sources.json` | 1 | Counts, dates, and provenance |
| `re_tools.jsonl` | 570 | Reverse-engineering and exploitation tool shelf |
| `github_atlas.jsonl` | 2064 | Security repositories by topic and stars |
| `jobs.jsonl` | 19 | Job ledger: actor, model, tokens, cost |
| `llm_prices.json` | 7 | Per-million token prices |
| `budget.json` | 1 | Monthly spend budget |
| `curriculum.json` | 25 | Training weeks, drills, labs and checkpoints |
| `learned_methods.jsonl` | 1 | Notes produced by the reflection loop |
| `upstream_repos.json` | 43 | Downloaded upstream repositories and skill counts |

Scanner seed data, all offline by default:

| File | Contents |
|---|---|
| `kev.json` | CISA KEV seed subset, refresh with `scripts/priority.py --update` |
| `epss.json` | FIRST EPSS seed for the KEV set |
| `secret_providers.json` | Revocation and read-only verification endpoints |
| `source_rules.json` | Static CWE rules with fix and false-positive notes |
| `mcp_rules.json` | MCP permission and instruction patterns |
| `jar_iocs.json` | Minecraft malware file and string indicators |
| `cms_vulns.json` | Small CMS version and path seed |
| `osv_seed.json` | Offline OSV sample, `--online` uses the real API |

`feed_cache/` is not committed. It holds timestamped copies of KEV, EPSS and OSV
responses, is written atomically and is invalidated by TTL (24 hours for KEV, 12
for EPSS and OSV). `scripts/feeds.py status` shows freshness; `update --online`
refreshes KEV.

## Schema

Every row carries `type`, `source`, `collected_at`, and a public URL.

- `thread`: `title`, `author`, `date`, `tags`, `summary`, `metrics`
- `expert`: `name`, `handle`, `profile`, `focus`, `works`
- `tool`: `category`, `repo`, `name`, `description`, `stars`, `language`, `install`, `flags`
- `method`: `title`, `headings`, `intro`, `code_blocks`, `tables`

## Caveats

Star counts and report totals are snapshots. HackerOne report bodies may be private, so only public metadata and summaries are stored. Reddit post text can include comment text; trim before quoting.

Refresh with the scripts in `../scripts/` and update `sources.json` afterward.
