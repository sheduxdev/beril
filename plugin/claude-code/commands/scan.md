---
description: Passive web or artifact scan with Beril
allowed-tools: Bash
---

Run a passive scan against the target the user names. Confirm ownership first.

```bash
./beril scan --target "$ARGUMENTS" --profile engineer --out scans/scan
```

Read the top five, keep the scope and limit block, and report only what the
evidence supports. If the user wants active probes, stop and ask for ownership.

Use `$ARGUMENTS` as the URL, IP or path. If empty, ask for the target.
