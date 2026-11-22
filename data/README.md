# Data snapshot

JSONL files collected on 2026-11-22 with Camoufox. The schema is documented in `SKILL.md` and `references/source-catalog.md`.

| File | Rows | Contents |
|---|---:|---|
| `threads.jsonl` | 447 | Forum threads, disclosed reports, article leads |
| `experts.jsonl` | 94 | Named researchers, handles, and public works |
| `canonical_tools.jsonl` | 87 | Curated tools with install commands |
| `methods.jsonl` | 85 | Method and research URLs |
| `method_details.jsonl` | 42 | Headings, intros, code density |
| `thread_details.jsonl` | 38 | Extracted thread and report notes |
| `sources.json` | 1 | Counts, dates, and provenance |
| `re_tools.jsonl` | 570 | Reverse-engineering and exploitation tool shelf |
| `github_atlas.jsonl` | 2064 | Security repositories by topic and stars |
| `curriculum.json` | 25 | Training weeks, drills, labs and checkpoints |
| `learned_methods.jsonl` | 1 | Notes produced by the reflection loop |
| `upstream_repos.json` | 43 | Downloaded upstream repositories and skill counts |

## Schema

Every row carries `type`, `source`, `collected_at`, and a public URL.

- `thread`: `title`, `author`, `date`, `tags`, `summary`, `metrics`
- `expert`: `name`, `handle`, `profile`, `focus`, `works`
- `tool`: `category`, `repo`, `name`, `description`, `stars`, `language`, `install`, `flags`
- `method`: `title`, `headings`, `intro`, `code_blocks`, `tables`

## Caveats

Star counts and report totals are snapshots. HackerOne report bodies may be private, so only public metadata and summaries are stored. Reddit post text can include comment text; trim before quoting.

Refresh with the scripts in `../scripts/` and update `sources.json` afterward.
