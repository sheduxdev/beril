---
description: Render a Beril report for a chosen reader
allowed-tools: Bash
---

Render an existing report. Pick the profile for the reader:

- `engineer` for the fixer
- `bugbounty` for triage
- `smb` for a one-page business summary
- `maintainer` for open source disclosure
- `sarif` for CI

```bash
./beril report --input "$ARGUMENTS" --profile engineer --out report.md
```

Do not mix profiles in one file. Keep the limits section.
