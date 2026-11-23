# Secret scanning and revocation

Beril finds secrets, masks them and gives the revocation order. It stays off
the network by default. Live verification is a separate flag.

## Why revoke first

The cost of a leaked key is not the leak. It is the two years that follow. In
2022, 64% of verified keys were still not revoked in 2026. Cleaning git history
does not kill a live key, it only reduces the number of copies.

Correct order:

1. Revoke or rotate the key at the provider.
2. Issue a replacement with a narrow scope.
3. Deploy it to the running system.
4. Remove the old value from history and config.
5. Check usage logs and billing.

## Command

```bash
./beril secrets --target ./repo --history --out scans/secrets
```

`--history` reads added lines in git history. `--verify` sends each key to the
provider read endpoint.

## Patterns

Covered providers: AWS, GitHub, GitLab, Google, OpenAI, Anthropic, DeepSeek,
Hugging Face, Stripe, Slack, Supabase, PostgreSQL, MongoDB, Redis, MySQL,
private keys, JWTs and generic secret names.

A generic pattern never goes above `low` confidence. A provider pattern starts
high and context can lower it.

## Context filters

| Signal | Effect |
|---|---|
| Path contains `test`, `example`, `fixture` or `docs` | Confidence drops |
| Value contains `xxxx`, `changeme`, `${VAR}` or `your_key` | Confidence drops, severity falls to info |
| Entropy below 2.6 | Confidence drops one step |
| Value shorter than 8 characters | Dropped |

The filters reduce false positives without removing them. Every hit needs a
human.

## Masking

The value is never written in full:

```text
AKIA...MNOP
```

The first four and last four characters are enough. Shorter values are masked
more aggressively. The JSON output has no full value either.

## Live verification

```bash
./beril secrets --target ./repo --verify
```

Only providers with an HTTP check are tried, and only read endpoints: GitHub
`/user`, GitLab `/api/v4/user`, OpenAI `/v1/models`, Anthropic `/v1/models`,
Google model list, Slack `auth.test`, Supabase REST root, Stripe balance.

Results:

- `2xx`: verified, high confidence.
- `401/403`: the provider rejected it, so the key may be revoked.
- Network error: unknown, confidence unchanged.

Database and private key verification stays local. MongoDB and PostgreSQL need
a separate connection attempt.

## Revocation guide

Every finding carries the provider console link in `fix`. AWS:
`console.aws.amazon.com/iam`. GitHub: `github.com/settings/tokens`. The list is
in `data/secret_providers.json` and can be edited.

## Git history

The scan reads added lines from the last 300 commits. On a large repo, lower the
commit count or add a path filter.

Two ways to clean history:

1. Simple: revoke the key, change the file, make a new commit. Leaving the old
   value in history is fine.
2. Full: remove it with `git filter-repo`, force push, refresh every clone. For
   a revoked key this is often unnecessary.

## Limits

- Encrypted archives and keys inside binaries get limited coverage.
- Cloud secret stores (Vault, SSM, Secrets Manager) are not scanned.
- There is no `.env` decryption or KMS integration.
- The generic pattern stays noisy. Take `low` confidence seriously.

## Beril's own secret handling

Beril writes no key to disk. It writes only masked lines to output files. During
`--verify`, the value lives in memory and in the provider request.
