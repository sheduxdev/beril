---
name: beril
description: Run a passive-first security assessment, authorized active probes, secret and dependency checks, local hunt, or a BGP posture lookup. Use when the user asks to scan an app they own, check an artifact, hunt a repo, review IaC or MCP config, or triage routing.
---

# Beril

Use the repository CLI. Read `SKILL.md` for the full loop and `AGENTS.md` for
the hard rules.

## First move

1. Ask for the target and the authorization if missing.
2. Passive first: `./beril scan --target <target> --out scans/scan`.
3. Report the top five with scope and limits.

## Active

```bash
./beril verify --new <host>
./beril verify --verify <host>
./beril scan --target https://<host> --active --profile bugbounty
```

## Other lines

- `./beril hunt --target <repo> --sandbox`: local bug hunt.
- `./beril secrets --target <dir> --history`: revoke-first secret pass.
- `./beril mcp --target .`: MCP config linter.
- `./beril infra --target <dir>`: IaC and K8s review.
- `./beril image --target <image>`: image scan through installed tools.
- `./beril bgp --prefix <cidr>`: passive BGP and RPKI.

Never call a scanner hit a vulnerability. Replay it. Mask secrets. Stop at the
agreed proof.
