# Project health check

`beril health` reads a local clone and reports maintenance, release, test,
process and dependency signals as a scorecard with reasons. It reuses the
dependency inventory and the licence reader; there is no new engine.

```bash
./beril health --target ./repo
./beril health --target ./repo --json --out scans/health
```

## Dimensions

| Dimension | Signals |
|---|---|
| Maintenance | Commits and authors in the last year, top author share |
| Release | Tags in the last year, signed tags |
| Tests | Test directory or runner config, CI workflow |
| Process | `SECURITY.md`, licence file |
| Dependencies | Component count, lockfile |
| Docs | README size, docs directory |

The overall number is the mean. It orders a portfolio review; it is not
comparable across ecosystems.

## Findings

Each missing signal is a finding with a fix. A single active author is flagged
only after enough commits to show a pattern. A large dependency count is low
severity by itself.

## Limits

- No forge API: issue age, pull request queue and reviewer spread are out.
- Commit count favours squash-heavy workflows.
- A tests directory can be empty or skipped in CI.
- Documentation volume is not documentation quality.
- The check reads the default branch only.

For a supplier or acquisition decision, read the findings and the limits
together. A high score with no recent commit is still a stale project.
