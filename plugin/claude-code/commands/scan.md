---
description: Passive web or artifact scan with Beril
allowed-tools: Bash
---

Run a passive scan against the target the user names. Do not interview when the
target is present.

```bash
./beril scan --target "$ARGUMENTS" --profile engineer --out scans/scan
```

Read the top five, keep the scope and limit block, and report only what the
evidence supports. If the user says "benim" or "my app" and wants active probes,
add `--active --owned`. Otherwise stay passive and ask one permission question.

Use `$ARGUMENTS` as the URL, IP or path. If empty, ask for the target.
