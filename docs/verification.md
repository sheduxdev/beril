# Ownership verification

Active work needs proof that the target is yours. Beril accepts three methods
and stores the record for 30 days. Expiry closes the gate again.

## Issue a token

```bash
./beril verify --new app.example
```

The output prints a token and three publish paths. A token is single use and
bound to one host.

## Method 1: DNS TXT

```text
_beril.app.example.  TXT  "beril-<32 hex>"
```

This is the strongest method. It works when you control DNS for the domain and
does not collide with a subdomain delegation.

## Method 2: file

```text
https://app.example/.well-known/beril-verify.txt
```

The file content is the token alone. Useful when you can write to the web root.
`/.well-known/` is a standard path and does not collide with security.txt.

## Method 3: meta tag

```html
<meta name="beril-verify" content="beril-<32 hex>">
```

Fast when you can edit the home page. Only the home page is read.

## Verify

```bash
./beril verify --verify app.example
```

The three paths run in order and the match uses a constant time compare. The
successful method goes into the record. On failure the record stays
`unverified` and active scanning stays closed.

## Record

```text
.beril/authorizations/app.example.json
```

Fields: host, method, token, evidence, verification time, expiry. The directory
is gitignored. The token is public, so it is not a secret.

## Declaration

When DNS and files are out of reach:

```bash
./beril scan --target https://app.example --active --owned
```

An `ack` record is written and the report says "user declaration". A declaration
is a reminder, not legal proof.

## Scope file

Verification covers the host. A scope file narrows the paths:

```text
app.example
*.app.example
api.example/v2/*
10.0.0.0/24
```

- `*.example.com` includes the root.
- `host/path/*` covers that prefix only.
- CIDR applies to IP targets.
- The tool refuses a target outside the list.

## Leaving scope

Two cases exist:

1. An HTTP redirect goes to another host. Beril writes a warning and keeps
   scanning. The report shows `redirected_to`.
2. The scope file excludes the target. The tool sends no request.

There is no subdomain discovery. Run each in-scope host separately.

## Without verification

Passive scanning always runs. Even a passive scan is a GET against a public
page. The legal grey area depends on the country and the site. `docs/legal.md`
says so.

## What it does not prove

- An ownership record does not override the program rule.
- The record does not show that the target is production.
- An expired token closes the gate again.
- An `ack` can be given for someone else's host. A wrong declaration is the
  user's responsibility.
