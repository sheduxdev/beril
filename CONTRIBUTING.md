# Contributing

## What helps

- A new source with a tested endpoint and notes on its access limits.
- A correction to a method card with a primary link and a repro.
- A tool entry with a verified install command.
- A failure mode that the Camoufox playbook does not cover.
- A scanner check with a false positive or false negative and the input that shows it.

## Before a pull request

```bash
./beril validate
```

Also run `python scripts/validate.py --links --max-links 40` when you touched `data/`.

- Add a public URL and `collected_at` to every new row.
- Keep the schema in `SKILL.md`.
- Date every snapshot.
- Replay the claim yourself. A scanner line is a lead, not proof.
- Keep secrets out. Mask them and say where they live.

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

`main` takes pull requests. The `catalog` check must pass, conversations must be resolved, and history stays linear. An admin can bypass for a hotfix, then open a follow-up if the bypass skipped review.

## Security

Report a vulnerability in Beril through a private advisory, not a public issue. See `SECURITY.md`.
