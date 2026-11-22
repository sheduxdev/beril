# CLAUDE.md

Beril is a cybersecurity intelligence and assessment skill. Claude Code loads this file automatically.

## Start here

- `SKILL.md`: the operating loop, source board, and quality gates.
- `agents/router.md`: intake questions and routing.
- `references/`: the deep material for each artifact.

## Commands

```bash
./install.sh
./install.sh --tools --re
./beril scan --target <url-or-path>
./beril scan --target <binary> --deep
./beril re --target <binary> --capa --floss --rizin
./beril train --week 1
./beril labs --run web
./beril validate
```

## Workflow

1. Ask for the target, authorization, read-only or active, and the proof needed.
2. Detect the artifact type.
3. Run the read-only scan.
4. Read the top findings and the matching card in `references/techniques.md`.
5. Confirm by hand with a minimal request or input.
6. Report with `references/dossier-template.md`.
7. State what you did not test.

## Rules

- Static before dynamic.
- Read-only before payloads.
- A scanner hit is a lead.
- Label confirmed vs inferred.
- Keep the evidence path.
- Stop at the agreed proof.
- Never test a host without scope.

## Break-my-app runbook

`docs/break-my-app.md` has the intake, per-artifact steps, report block, and stop conditions.

## Task recipes

- Web app: scan, then choose auth, injection, IDOR, or logic. One class per pass.
- APK: scan, read the manifest, review exported components, then Frida in a lab.
- EXE/ELF: scan `--deep`, map imports and mitigations, open Ghidra or rizin, confirm in a debugger.
- Source: scan `--tools`, trace one source to one sink, write the fix and a test.
- Firmware: unblob, map the rootfs, check the update path and the management daemon.
- Report: evidence first, impact second, CVSS last.

## Output

Use the finding block in `agents/router.md`. Answer in the user's language.
