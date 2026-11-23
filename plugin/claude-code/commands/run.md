---
description: Run installed specialist tools through Beril
allowed-tools: Bash
---

Show what is installed, then run only the adapters that exist.

```bash
./beril run --list
./beril run --target "$ARGUMENTS" --owned --out scans/run
```

Active adapters (Nuclei, testssl) need ownership. Missing tools are listed, not
simulated. See `references/competitive-gap-analysis.md` for the split.
