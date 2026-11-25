---
name: beril
description: Run a passive-first security assessment, domain recon, authorized active probes, secret and dependency checks, local hunt, or a BGP posture lookup. Use when the user says "break this", "find a bug", "scan this", "kır", "açık bul", "recon" or "harita", asks to check an app they own, check an artifact, hunt a repo, review IaC or MCP config, or triage routing.
---

# Beril

Use the repository CLI. Read `SKILL.md` for the full loop, `AGENTS.md` for the
hard rules and `agents/front-desk.md` for the conversational behavior.

If the target is in the sentence, the first step is a command, not an interview.
"Kır" or "açık bul" means passive scan, then one manual class. Passive needs no
gate. Active needs one ownership signal.

## First move

1. If the target is clear, run the matching command.
2. Otherwise ask one question: the target.
3. Passive first: `./beril scan --target <target> --out scans/scan`.
4. Report the top five with scope and limits.

Map a domain before choosing a host:

```bash
./beril recon --target example.com
```

## Active

```bash
./beril verify --new <host>
./beril verify --verify <host>
./beril scan --target https://<host> --active --profile bugbounty
```

An explicit "benim", "my app" or "our site" allows `--owned` without a record.

## Other lines

- `./beril hunt --target <repo> --sandbox`: local bug hunt.
- `./beril secrets --target <dir> --history`: revoke-first secret pass.
- `./beril mcp --target .`: MCP config linter.
- `./beril infra --target <dir>`: IaC and K8s review.
- `./beril image --target <image>`: image scan through installed tools.
- `./beril bgp --prefix <cidr>`: passive BGP and RPKI.

Never call a scanner hit a vulnerability. Replay it. Mask secrets. Stop at the
agreed proof. Answer in the user's language.
