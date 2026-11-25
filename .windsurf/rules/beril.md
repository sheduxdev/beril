---
trigger: always_on
---

# Beril

Use `AGENTS.md` as the operating file and `SKILL.md` as the method.

If the user names a target, act. "Kır" or "açık bul" means scan, then one manual class. Behavior: `agents/front-desk.md`.

Start passive:

```bash
./beril scan --target <url-or-path>
./beril recon --target <domain>
```

For active work, check the ownership record first (`./beril verify --new <host>`, then `--verify`). For an open source repo, `./beril hunt --target <repo> --sandbox`.

Then open the matching reference: web, mobile, reverse engineering, firmware, cloud.

Rules: confirm scope, one class at a time, replay every scanner hit, mask secrets, keep evidence, stop at proof.
