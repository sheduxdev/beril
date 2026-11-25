---
description: Local bug hunt with a networkless sandbox
allowed-tools: Bash
---

Run the hunt against a local clone. Keep only reproduced findings. Start now if
the path is present, then read `docs/bug-hunt.md` before sending.

```bash
./beril hunt --target "$ARGUMENTS" --sandbox --timebox 300 --report HUNT.md
```

Read `docs/bug-hunt.md` before sending. A candidate without a reproduction stays
local. Use `references/maintainer-report.md` for the disclosure.
