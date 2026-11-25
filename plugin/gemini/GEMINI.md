# Beril

Passive-first security assessment for Gemini CLI. Read the repository
`SKILL.md` and `AGENTS.md` first.

## Loop

1. If the target is in the sentence, run the matching command.
2. Passive first: `./beril scan --target <target>`
3. Read the top five and the scope block.
4. `./beril verify --new <host>` for active work.
5. Report with the right profile.

"Kır" or "açık bul" means scan, then one manual class. "Harita" or "recon"
means `./beril recon --target <domain>`. Behavior: `agents/front-desk.md`.

```bash
./beril scan --target <url-or-path>
./beril recon --target <domain>
./beril hunt --target <repo> --sandbox
./beril secrets --target <dir> --history
./beril infra --target <dir>
./beril bgp --prefix <cidr>
```

A scanner hit is a lead. Replay it. Mask secrets. No scope, no scan.
