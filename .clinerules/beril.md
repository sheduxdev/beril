# Beril

Read `AGENTS.md` first.

If the user names a target, act. "Kır" or "açık bul" means scan, then one manual class. Behavior: `agents/front-desk.md`.

Workflow: intake, detect, passive scan, matching method card, minimal replay, report. Active work needs an ownership record.

Never scan without scope. Never run an unknown binary without a snapshot or sandbox. A scanner hit is a lead, not a finding. Mask secrets and revoke before cleaning git history.

Commands:

```bash
./beril scan --target <url-or-path>
./beril recon --target <domain>
./beril verify --new <host>
./beril scan --target <web> --active
./beril hunt --target <repo> --sandbox
```
