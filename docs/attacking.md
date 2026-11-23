# Attack line: bug bounty and authorized testing

Beril has two lines. The defense line scans a system you own. The attack line
looks for bugs inside an authorized scope, proves the smallest case and writes
the report. Both lines use the same finding model, the same report format and
the same honesty rules.

## 0. The gate

Active work differs from a passive GET. Beril enforces that difference in code.

```bash
# 1) issue a token
./beril verify --new app.example

# 2a) DNS TXT: _beril.app.example = "beril-..."
# 2b) file: https://app.example/.well-known/beril-verify.txt
# 2c) meta: <meta name="beril-verify" content="beril-...">

# 3) verify
./beril verify --verify app.example

# 4) scan active
./beril scan --target https://app.example --active
```

The record lives in `.beril/authorizations/<host>.json` for 30 days. The tool
exits before the first payload when no record exists. The program rule (for
example "GET only") comes before Beril's gate.

A scope file is the second gate:

```text
# scope.txt
app.example
*.app.example
api.example/admin/*
```

```bash
./beril scan --target https://app.example --active --scope scope.txt
```

Hosts and paths outside the list stay untouched. A redirect away from scope
shows up as a warning in the report.

## 1. Passive discovery

Start quiet:

```bash
./beril scan --target https://app.example --profile engineer
```

The output holds headers, CSP, cookies, CORS, exposed files, TLS, DNS mail
records, ports and fingerprints. Each finding carries a request line and a
short response.

Then widen by hand:

- List subdomains and API hosts in scope.
- Read login, signup, reset, invite and payment flows.
- Create two accounts. Request the same object as both users.
- Read robots.txt, sitemap, old docs and JS bundles.
- Pull the endpoint list from source maps when they exist.

## 2. Active pass

Beril's active set is deliberately small: one quote, one reflection marker, one
redirect, one traversal, OPTIONS and TRACE. No writes, no fuzzing.

```bash
./beril scan --target https://app.example --active --profile bugbounty --sarif
```

How to read a probe:

- A quote that returns a database error signature is a medium confidence SQLi
  candidate. Confirm with a boolean pair or a timing check.
- A marker returned without encoding is reflection, not XSS. Check the context
  (attribute, script, URL) and the CSP before reporting.
- A `Location` header to an attacker host is an open redirect candidate. The
  impact depends on whether an OAuth flow carries a token through it.
- A `/etc/passwd` body is a proven file read. Try the app config and secret
  files for the real impact.
- An `Allow` header with write methods needs one PUT or DELETE to prove the write
  path. Clean up after it.

Stop at the first reproducible proof. Spreading one class over every endpoint
makes a report nobody finishes.

## 3. Known bugs

If Nuclei is installed, run it through the adapter so the scope and the report stay
in one place:

```bash
./beril run --target https://app.example --only nuclei --owned
```

Its template hits import as medium confidence. Replay before reporting.

Version matching in the passive scan is a hint. For dependencies and CVEs:

```bash
./beril deps --target ./repo --online --reachability
```

KEV and EPSS set the order. A KEV entry beats a higher CVSS score that nobody
exploits. A low EPSS score still gets patched, because KEV already proves
exploitation.

## 4. Verification and evidence

Every finding sits at one of three levels:

| Level | Meaning | In the report |
|---|---|---|
| Candidate | Pattern or a single response | Yes, low confidence |
| Reproduced | Same behavior on two clean requests | Yes |
| Verified | Impact shown, human confirmed | Yes, high confidence |

The evidence pack:

1. Full request (method, path, headers, body).
2. Response (status, relevant headers, body excerpt).
3. Baseline request and the diff.
4. Environment (browser, account role, time).
5. Reproduction step.

A screenshot alone is weak. A `curl` pair is stronger.

## 5. Report

```bash
./beril report --input scans/app.json --profile bugbounty --out report.md
```

The profile asks for CVSS, CWE, a request pair, impact and a fix. Map the fields
to a program template when it has one. Never skip these three statements:

- What was tested.
- What was not tested.
- Why it could be a false positive.

## 6. Limits

The active line does not cover:

- POST bodies, file upload, SSRF callbacks, authenticated IDOR.
- Timing injection and fuzzing.
- Business logic and race conditions.
- WAF evasion and rate limit pressure.

Those stay manual. `references/bug-method-matrix.md` has a test card per class.

## 7. Daily flow

1. Read the program scope and write `scope.txt`.
2. Get the ownership record or pass `--owned`.
3. Passive scan, then manual discovery.
4. Pick one class, try it on one endpoint.
5. Collect the proof and place it at a level.
6. Write the report and send it.
7. Clean up anything you created.
