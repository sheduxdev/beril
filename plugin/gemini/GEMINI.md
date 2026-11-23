# Beril

Passive-first security assessment for Gemini CLI. Read the repository
`SKILL.md` and `AGENTS.md` first.

## Loop

1. Confirm target and authorization.
2. `./beril scan --target <target>`
3. Read the top five and the scope block.
4. `./beril verify --new <host>` for active work.
5. Report with the right profile.

```bash
./beril scan --target <url-or-path>
./beril hunt --target <repo> --sandbox
./beril secrets --target <dir> --history
./beril infra --target <dir>
./beril bgp --prefix <cidr>
```

A scanner hit is a lead. Replay it. Mask secrets. No scope, no scan.
