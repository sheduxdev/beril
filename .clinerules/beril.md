# Beril

Read `AGENTS.md` first.

Workflow: intake, detect, read-only scan, matching method card, minimal replay, report.

Never scan without scope. Never run an unknown binary without a snapshot. A scanner hit is a lead, not a finding.

Commands:

```bash
./beril scan --target <url-or-path>
./beril scan --target <binary> --deep
```
