# GitHub Copilot instructions

Beril is a security assessment skill. Read `AGENTS.md` and `SKILL.md` before suggesting code or tests.

## Workflow

1. Confirm the target and the authorization.
2. Use a read-only scan first: `./beril scan --target <path-or-url>`.
3. Match the artifact to `references/`.
4. Replay findings with a minimal input.
5. Add a regression test when fixing.

## Rules

- Prefer standard library and existing project dependencies.
- Keep PoCs small and reproducible.
- Do not add a secret to source. Use a placeholder and note rotation.
- Separate confirmed behavior from inference.
- Stop at the proof the user asked for.
