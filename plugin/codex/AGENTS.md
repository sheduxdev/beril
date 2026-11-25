# Beril for Codex

Load `AGENTS.md` at the repository root first. It carries the hard rules.

## Default loop

1. If the target is in the sentence, run the matching command. Do not interview.
2. Passive scan: `./beril scan --target <target> --out scans/scan`.
3. Read the top five and the scope block.
4. Replay one finding by hand.
5. Report with the matching profile.

"Kır" or "açık bul" means scan, then one manual class. "Harita" or "recon"
means `./beril recon --target <domain>` first. Behavior:
`agents/front-desk.md`.

## Commands

```bash
./beril scan --target <url-or-path>
./beril recon --target <domain>
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
