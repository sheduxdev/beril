# AGENTS.md

Beril is a cybersecurity intelligence and assessment skill. This file is the entry point for any coding agent.

## Read first

1. `SKILL.md` for the loop and the quality gates.
2. `agents/router.md` for intake and routing.
3. The matching reference for the artifact.

## Commands

```bash
./install.sh                 # base install
./install.sh --tools --re    # optional recon and RE tools
./beril scan --target <url-or-path>
./beril scan --target <binary> --deep
./beril re --target <binary> --capa --floss --rizin
./beril train --status
./beril labs --run
./beril validate
```

## Default workflow

1. Intake. Target, authorization, read-only or active, proof needed.
2. Detect. URL, local artifact, source tree, or firmware.
3. Scan. Use the read-only pass first.
4. Read. Open the top findings and the matching method cards.
5. Verify. Replay with a minimal request or input.
6. Report. Use `references/dossier-template.md`.
7. Clean up. Say what was not tested.

## Hard rules

- Do not scan a host without confirming the user owns it or has scope.
- Do not run untrusted binaries on the host without a snapshot or VM.
- Do not dump a whole database or brute force without a reason.
- Do not execute a packed sample just to "see what happens".
- Do not claim a vulnerability from a scanner signature alone.
- Do not paste secrets into the report. Mask them and say where they live.
- Keep every command and output path.

## Break-my-app runbook

`docs/break-my-app.md` has the intake, per-artifact steps, report block, and stop conditions.

## Common requests

| User says | Do |
|---|---|
| "Web appimde açık ara" | URL scan, then one manual class at a time |
| "APK'mı incele" | APK scan, manifest review, hook template |
| "Bu EXE/ELF'i kır" | deep scan, Ghidra or rizin, debugger |
| "Kaynak kodum var" | source scan with `--tools`, trace one sink |
| "Firmware" | unblob, rootfs map, update path |
| "Rapor yaz" | evidence first, then the report template |
| "Öğret" | `./beril train`, one week at a time |

## Evidence

A finding needs a reproducible artifact: request and response, crash input, a diff, or a file path. A screenshot alone is weak. A scanner line alone is not a finding.

## Language

Answer in the user's language. Keep commands and paths in their original form.
