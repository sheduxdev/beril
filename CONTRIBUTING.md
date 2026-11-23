# Contributing

## What helps

- A new source with a tested endpoint and notes on its access limits.
- A correction to a method card with a primary link and a repro.
- A tool entry with a verified install command.
- A failure mode that the Camoufox playbook does not cover.
- A scanner check with a false positive or false negative and the input that shows it.

## Before a pull request

```bash
./install.sh --dev
ruff check scripts tests
ruff format --check scripts tests
pyright
python -m pytest -q
./beril validate
python -m compileall -q scripts
```

Also run `python scripts/validate.py --links --max-links 40` when you touched `data/`.

- Add a public URL and `collected_at` to every new row.
- Keep the catalog schema in `SKILL.md` and the finding schema in `references/finding-schema.md`.
- Date every snapshot.
- Replay the claim yourself. A scanner line is a lead, not proof.
- Keep secrets out. Mask them and say where they live.
- A new check needs a fixture and a test, positive and negative.
- A new active probe needs a budget cost and a false-positive note.
- Renderer changes need a golden test for every profile they touch.

## Python

- Type hints on every function.
- Google style docstrings on public functions.
- Specific exception types. No bare `except`.
- Validate inputs at the function boundary.
- Keep functions small and pure when possible.
- pytest only. Tests live in `tests/` and every new check needs a positive and a negative case.
- ruff for lint and format, pyright for types. Both run in CI with pinned versions.

## Prose

The house rules come from the humanizer skill:

- no em dashes or en dashes;
- sentence case headings, no decorative emoji;
- straight quotes;
- no forced triad;
- separate observation from inference.

## Commits

Small commits with a scope: `docs:`, `data:`, `fix:`, `feat:`, `ci:`. One topic per commit. Do not mix a data refresh with a code change.

## Review

`main` takes pull requests. The `test` job must pass (pytest, schema, prose and compile), conversations must be resolved, and history stays linear. An admin can bypass for a hotfix, then open a follow-up if the bypass skipped review.

## Security

Report a vulnerability in Beril through a private advisory, not a public issue. See `SECURITY.md`.
