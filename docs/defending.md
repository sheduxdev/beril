# Defense line: companies, small business and developers

This line helps you fix your own system. The output is ordered: highest impact
first, then the fix, then the evidence. The aim is few findings and real work.

## Order

1. Passive web hygiene.
2. Secrets and revocation.
3. Dependencies and known bugs.
4. AI apps and MCP configuration.
5. Game servers and JAR files.
6. Active verification.

## 1. Passive web hygiene

```bash
./beril scan --target https://company.example --profile smb
```

The report fits one page, with a traffic light and at most five items under "do
today". A KVKK note reminds the reader of the 72 hour rule.

Priority:

| Finding | Why first |
|---|---|
| Exposed `.env`, backup, SQL dump | Direct secret and data access |
| Exposed admin panel | Password guessing and panel takeover |
| Exposed database port | Authentication sits outside |
| Missing DMARC and SPF | Fake payment and CEO fraud |
| Missing CSP and HSTS, weak cookie flags | XSS and session theft get worse |

On the same machine or LAN, use the private address:

```bash
./beril scan --target http://10.0.0.20 --profile engineer
```

## 2. Secrets

Search the local repository and its history first:

```bash
./beril secrets --target ./repo --history --out scans/secrets
```

The rule is simple: **revoke first, clean history second.** Cleaning history
does not kill a live key. Each finding carries the provider console and the
revocation order. Values are masked, so the report has no full key.

Use `--verify` only with explicit consent, because the key leaves the host.
Verification uses read-only endpoints.

## 3. Dependencies

```bash
./beril deps --target ./repo --reachability
./beril sbom --target ./repo --out sbom.cdx.json --spdx sbom.spdx.json --vex sbom.vex.json --licenses licenses.md
```

Reachability is a grep, not a call graph. A package marked "not-found" can still
be pulled in transitively, so it stays in the report at low confidence instead
of being deleted.

Priority combines KEV, EPSS and reachability. A KEV package goes first even when
the upgrade breaks things.

## 4. AI apps and agent configuration

Supabase, Lovable, v0 and similar tools produce many apps with a table missing
RLS. The anon key is public by design. The policy is the protection.

```bash
./beril vibe --target ./app
```

The checks:

- A migration with `create table` and no `enable row level security`, or no
  `create policy`.
- `service_role` in a client directory.
- A secret behind a `NEXT_PUBLIC_*` or `VITE_*` prefix.
- `dangerouslySetInnerHTML` with no sanitizer.
- Open CORS and an open Firebase rule.
- An API route with no auth hint.

The MCP client config is a separate command:

```bash
./beril mcp --target .
```

It flags unpinned `npx -y`, plain tokens, root directory access, privileged
containers and instructions inside tool descriptions. The description an agent
reads is an attack surface.

## 5. Game servers

```bash
./beril jar --target ./plugins
./beril jar --target ./FreeRank.jar
./beril scan --target ./server --jar
```

The scan reports IOC files, a `plugin.yml` mismatch, external URLs, Base64,
reflection and process calls. Nothing runs.

When something looks bad:

1. Stop the server and quarantine the jar.
2. Revoke the plugin author account tokens.
3. Rotate `ops.json`, `server.properties`, SSH keys and panel passwords.
4. Restore a clean backup and compare jar hashes.
5. Review `online-mode`, RCON and the forwarding secret.

## 6. Active verification

A passive report says "this path is open". An active pass says "this parameter
returns an error".

```bash
./beril verify --new company.example
./beril scan --target https://company.example --active --owned
```

The active pass writes nothing. Production needs no window, yet run it during
work hours at low speed. The defaults are 2 requests per second and 250
requests.

## 7. CI gate

Keep a baseline and fail only on new risk:

```bash
./beril scan --target https://staging.example --out scans/staging
./beril scan --target https://staging.example --baseline scans/staging.json --fail-on high --sarif
```

`--fail-on` accepts `info`, `low`, `medium`, `high` and `critical`. The baseline
matches by finding id and by check plus subject. The suppressed count stays in
`meta.suppressed`.

## 8. After a fix

1. Make the change that closes the finding.
2. Run the same command again.
3. Confirm the finding is gone and no new one appeared.
4. Add a regression test (a header, config or policy test).
5. Keep the evidence and the date.

## 9. Limits

Beril never says "you are secure". It covers the check list it ran. Authenticated
flows, business logic and the authorization model stay manual. Get an outside
review at least once a year.
