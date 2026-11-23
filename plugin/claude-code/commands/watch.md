---
description: Continuous watch with baseline diff and webhook
allowed-tools: Bash
---

Start with a baseline, then watch. The first pass becomes the baseline.

```bash
./beril watch --target "$ARGUMENTS" --interval 3600 --iterations 3 --out-dir scans/watch
```

Each pass writes JSON and Markdown and prints only the difference. Add
`--webhook` when a chat or automation endpoint exists. Passive by default.
