---
trigger: always_on
---

# Beril

Use `AGENTS.md` as the operating file and `SKILL.md` as the method.

Start passive:

```bash
./beril scan --target <url-or-path>
```

For active work, check the ownership record first (`./beril verify --new <host>`, then `--verify`). For an open source repo, `./beril hunt --target <repo> --sandbox`.

Then open the matching reference: web, mobile, reverse engineering, firmware, cloud.

Rules: confirm scope, one class at a time, replay every scanner hit, mask secrets, keep evidence, stop at proof.
