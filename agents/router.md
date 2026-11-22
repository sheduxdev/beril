# Beril agent router

Read this before a task. It maps a request to the right layer and keeps the agent from scanning blind.

## Intake

Ask only what you cannot infer:

1. What is the target: URL, APK, IPA, EXE, ELF, archive, source directory, or firmware?
2. Do you own it, or is it in a bounty scope? Get the exact host or path.
3. Is read-only enough, or may I send payloads?
4. What proof do you need: note, report, PoC, or a fix?

If the user says "break it and report", default to read-only first, then a narrow active test on the same target. Stop at the first reproducible proof.

## Break-my-app runbook

`docs/break-my-app.md` has the intake, per-artifact steps, report block, and stop conditions.

## Route

| Request | First command | Then |
|---|---|---|
| "Scan my web app" | `./beril scan --target <url>` | `references/techniques.md`, manual request pair |
| "Check my APK" | `./beril scan --target <apk> --deep` | `references/mobile-reverse.md` |
| "Look at this EXE/ELF" | `./beril scan --target <bin> --deep` | `references/reverse-engineering.md` |
| "Review my source" | `./beril scan --target <dir> --tools` | `references/vulnerability-research.md` |
| "Extract this firmware" | `./beril scan --target <image> --deep` | `references/firmware-iot.md` |
| "Find a bug, prove it" | scan, then the matching method card | `references/exploit-development.md` |
| "Write the report" | existing evidence | `references/dossier-template.md`, `references/scoring.md` |
| "Teach me" | `./beril train --status` | `references/curriculum.md` |
| "Run the labs" | `./beril labs --run` | `labs/README.md` |

## Rules

- One target at a time. One vulnerability class at a time.
- Static before dynamic. Read-only before payloads.
- Do not run a binary until you know what it would do.
- Every claim gets a request, a crash, a diff, or a file path.
- A scanner hit is a lead. Replay it by hand.
- Separate confirmed behavior from inference with explicit labels.
- Stop when the agreed proof exists.

## Output

```markdown
## Finding
- Asset:
- Precondition:
- Request or input:
- Result:
- Impact:
- Root cause:
- Fix:
- Confidence: confirmed / inferred
- Evidence path:
```

If no finding, list what you ruled out and the next test.

## When to stop and ask

- The target is ambiguous or shared hosting.
- A test needs a write, a restart, or a paid API.
- The scan needs credentials you do not have.
- An artifact is packed, encrypted, or split and needs another part.
- A finding could break production and the user has not approved a window.
