# GEMINI.md

Beril is a cybersecurity intelligence and assessment skill for Gemini CLI.

## Read

- `SKILL.md`
- `agents/router.md`
- the reference for the artifact under test

## Commands

```bash
./beril scan --target <url-or-path>
./beril scan --target <binary> --deep
./beril re --target <binary> --capa --floss --rizin
./beril labs --run
./beril train --next
```

## Loop

1. Confirm target and authorization.
2. Detect the artifact.
3. Scan read-only.
4. Open the matching method card.
5. Replay minimally.
6. Report with evidence.
7. List the gaps.

## Rules

- One target, one class at a time.
- Static before dynamic.
- Confirmed vs inferred labels.
- No scope, no scan.
- A clean scan is not a certification.

Answer in the user's language. Keep commands intact.
