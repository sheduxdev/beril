# Beril for Codex

Load `AGENTS.md` at the repository root first. It carries the hard rules.

## Default loop

1. Confirm the target and the authorization.
2. Passive scan: `./beril scan --target <target> --out scans/scan`.
3. Read the top five and the scope block.
4. Replay one finding by hand.
5. Report with the matching profile.

## Commands

```bash
./beril scan --target <url-or-path>
./beril verify --new <host>
./beril scan --target <url> --active --profile bugbounty
./beril hunt --target <repo> --sandbox
./beril secrets --target <dir> --history
./beril infra --target <dir>
./beril image --target <image>
./beril bgp --prefix <cidr>
./beril report --input <json> --profile smb
```

Rules: passive before payloads, evidence for every claim, secrets masked, stop
at the proof. Never scan a host without scope.
