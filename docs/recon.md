# Recon

`beril recon` maps a root domain before the app scan. It answers four questions
with DNS lookups and plain GETs:

1. Which hostnames exist?
2. Which ones answer, and with what title, server and stack?
3. Which CNAMEs point at a service that hands out a claimable page?
4. Which public IPs outside the CDN ranges look like the origin?

```bash
./beril recon --target example.com
./beril recon --target example.com --owned --out scans/example
./beril recon --target example.com --no-bruteforce --max-requests 120
```

| Flag | Effect |
|---|---|
| `--owned` | Store an ownership acknowledgement |
| `--scope <file>` | Drop discovered hosts outside the scope |
| `--sources crtsh,certspotter` | Run only the named sources |
| `--no-bruteforce` | No DNS wordlist |
| `--no-auth` | Skip the login and reset probe |
| `--max-hosts 50` | Cap probed hosts |
| `--max-requests 150` | Cap total requests |
| `--rate 2` | Requests per second |

Only GET is used. Nothing is fuzzed or written. The gate is still useful: with
`--owned` the acknowledgement is stored, and `--scope scope.txt` drops hosts
outside the engagement.

## Sources

| Source | Request | Notes |
|---|---|---|
| crt.sh | `GET /?q=%.domain&output=json` | Certificate transparency, free, can be slow |
| Cert Spotter | `GET api.certspotter.com/v1/issuances` | Certificate transparency, free tier |
| HackerTarget | `GET api.hackertarget.com/hostsearch` | Passive DNS, free tier |
| DNS Dumpster | `POST dnsdumpster.com` with the CSRF token | Passive DNS, HTML parse |
| Wordlist | A, AAAA resolution for `data/recon.json` words | Local DNS only |

Run one source with `--sources crtsh`, or a comma list with
`--sources crtsh,certspotter`. `--no-bruteforce` keeps the pass fully passive.

Wildcard DNS is checked first. When a random label resolves, hosts from the
brute-force list that share the wildcard address are kept but rank lower. A
wildcard finding is recorded.

## Host probe

Each resolved host gets HTTPS and then HTTP on `/`. The probe records status,
title, `Server`, `X-Powered-By` and response headers. Technology fingerprints in
`data/recon.json` match against those headers, cookies, meta tags and body
markers. A match is a lead, never proof.

The score follows the ARTEX idea of ranking by role, not by status alone:
admin, database, backup and internal names score highest, then development,
API, config and auth, then mail, monitoring, file and VPN. `401` adds 25, `403`
adds 20, `200` adds 10, a `5xx` adds 15. The score decides what to read first.

## Takeover check

A CNAME is compared with the service list. A finding needs the CNAME suffix and
a page marker. Without a marker but with a `404`, the finding is `inferred` and
confidence drops to medium. Confirm the resource at the provider before
reporting it.

## Origin candidates

MX hosts, CT names, subdomain A records and IP disclosure headers are scored.
Private and CDN addresses are filtered. An address found by one method gets its
method weight. Multiple methods add a bonus, and an open web port adds 10. Only
the top three enter the findings, at `info`, and only when the apex itself sits
behind a CDN. Firewalling the origin to CDN ranges is the fix, not hiding it.

## Auth surface and emails

The apex is probed once for the login and reset paths in `data/recon.json`.
Links from the home page with `login`, `auth`, `reset` or `forgot` are added,
capped at 40 paths. A page counts when it returns `200`, `401` or `403` and has a
password field or auth keyword.

Addresses published on the home page are collected for the report. They feed
phishing and spray lists.

## Output

`scans/recon-<domain>.json` is the source of truth. The Markdown view has the
host table, candidates, auth surface, emails and findings.

Read it in this order:

1. Takeover candidates. Confirm and report.
2. Critical and high score hosts. Send the app scan at the best one.
3. Origin candidates. Check whether the origin answers directly.
4. Auth pages. Note the MFA and rate limit posture.
5. The rest of the inventory.

Then run `./beril scan --target https://chosen-host` for headers, paths, TLS and
mail policy. Recon does not replace that pass.

## Limits

- Certificate transparency misses hosts without a certificate.
- Passive sources are third parties. They can be stale or rate limited.
- A 200 with a parked page is still a live host.
- A CNAME match can be a live service, not a takeover.
- Origin scoring is inference. Shared hosting creates noise.
- No zone transfer, DNSSEC, cache snooping or port sweep.
- JavaScript-only hosts show an empty title.
- The request budget is global. A large inventory is cut at `--max-hosts` (120 by default).

Refresh the seed lists in `data/recon.json` when a service changes its takeover
page. Cloud CIDRs move. A stale range only lowers precision.
