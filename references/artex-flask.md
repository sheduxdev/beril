# ARTEX (Flask recon app, IlyassCODEX)

Repo: https://github.com/IlyassCODEX/ARTEX
Author: IlyassCODEX (`CODEX(ILYASS.GH)`)
Created: 2025-07-16. One commit on 2025-07-24.
Stars: 432, forks: 249 at review time.
License: none. No `LICENSE` file, so the code is all rights reserved. Beril
reimplements the methods and keeps the public data lists as facts.

This is not the Go autonomous platform. For that one, read `references/artex.md`.

The app is a Flask wrapper around nine Python modules. A form collects a domain
and five toggles. A background thread runs the modules, writes into a dict, and
a 1,692 line results template renders tabs. There is an AI analyst with a Groq
key and a rule-based fallback. It is a demo product, not a hardened scanner.

## Pipeline

| Step | Module | Technique |
|---|---|---|
| 1 | `subdomains.py` | crt.sh JSON, HackerTarget hostsearch, DNS Dumpster with CSRF, 17 word DNS brute force, CNAME takeover check |
| 2 | `enumeration.py` | Login and reset path guesses, home page link crawl, password field detection, Office365, Google, Okta and Auth0 URL guesses, email regex and pattern inference |
| 3 | `port_scanner.py` | `python-nmap` `-sT --open -T4`, fallback threaded socket connect |
| 4 | `dns_scan.py` | A, AAAA, MX, NS, TXT, CNAME, SOA, SPF, DMARC, PTR, optional AXFR and cache snooping |
| 5 | `real_ip_discovery.py` | Subdomain A, DNS data, CT names, IP headers, MX hosts, confidence score |
| 6 | `ssl_scanner.py` | Certificate parse, protocol and cipher probes, HSTS, OCSP, CT, CRL, DNSSEC, vulnerability inference |
| 7 | `tech_detector.py` | Wappalyzer over one response |
| 8 | `FastAnalyst.py` | Rule-based host scoring, risk score, recommendations |
| 9 | `AI_analyst.py` | Groq `llama3-70b-8192`, owner and hunter prompts, rule fallback |

## Data worth keeping

### Risky ports

| Port | Service | Claimed risk | Real note |
|---:|---|---|---|
| 21 | FTP | high | Anonymous login and plaintext |
| 22 | SSH | high | Brute force, weak keys. Open SSH is not a bug |
| 445 | SMB | critical | EternalBlue class, null sessions |
| 1433 | MSSQL | high | Brute force, `xp_cmdshell` |
| 3306 | MySQL | medium | Direct database access |
| 3389 | RDP | high | BlueKeep class, brute force |
| 5432 | PostgreSQL | medium | Direct database access |
| 5984 | CouchDB | medium | Admin party mode |
| 6379 | Redis | high | No auth, module load |
| 9200 | Elasticsearch | medium | Unauthenticated data |
| 27017 | MongoDB | high | No auth by default |
| 8080 | HTTP alt | medium | Secondary app |

Beril `data/recon.json` extends this with 23, 25, 111, 2375, 2376, 5900, 6443,
7001, 8500, 9042, 10250, 11211, 15672 and keeps a severity per port.

### Exposed files

45 paths. The useful additions over a basic list are `.htpasswd`, `.git/config`,
`.bzr/branch/branch.conf`, `wp-config.php`, `config.yaml`, `config.yml`,
`config.json`, `database.sql`, `backup.sql`, `admin/.env`, `admin/.git/HEAD`,
`admin/.htpasswd`, `storage/.env`, `api/.env`, and four log paths. Beril
`web_checks.PATHS` now carries them with markers and fixes.

### Auth paths

15 login paths and 11 reset paths, including `/wp-login.php`,
`/account/login`, `/auth/login`, `/member/login`, `/portal/login`,
`/wp-login.php?action=lostpassword` and `/account/recovery`. Detection is a
password input, an auth keyword or the path itself. This is a wordlist, not a
crawler.

### Subdomain takeover

Only four services: GitHub Pages, S3, Heroku and Shopify. The check requires a
CNAME match and a page marker on a 404. Beril `data/recon.json` carries 28
services from the public takeover list and also accepts a marker without a 404.

### CDN ranges

Cloudflare, Akamai, Fastly and CloudFront v4 ranges. The Cloudflare list is also
fetched from `cloudflare.com/ips-v4` with a hardcoded fallback. Beril adds Azure
Front Door, GCP frontend, Imperva and Sucuri ranges, and filters private space.

### IP disclosure headers

`X-Real-IP`, `X-Original-URL`, `X-Forwarded-For`, `X-Cluster-Client-IP`,
`X-Forwarded`, `Forwarded-For`, `Forwarded`, `Client-IP`, `X-Client-IP`, `Via`.
Beril adds `X-Host`, `X-Server-IP`, `True-Client-IP` and `CF-Connecting-IP`.

### Origin scoring

Mail server 10, HTTP header 8, DNS record 6, certificate transparency 4,
subdomain 3, plus 5 per extra method and 10 when a web port answers. Minimum
score 8. The weights are reasonable. The implementation leaks the apex address
into the candidate set.

### Host scoring

Keyword points: `phpmyadmin` 75, `adminer` 70, `cpanel` 70, `administrator` 65,
`intranet` 65, `whm` 65, `admin` 60, `internal` 60, `backup` 55, `database` 55,
`private` 55, `mysql` 50, `db` 50, `configuration` 50, `dev` 45, `development`
45, `staging` 45, `graphql` 45, `config` 45. Status adds 401 25, 403 20, 5xx 15,
200 10, HTTPS 5. Thresholds: 60 critical, 40 high, 25 medium.

### Technology fingerprints

A small header DB for servers, languages, frameworks, CMS and WAF, plus a cloud
and CDN map. Most of the actual detection is delegated to Wappalyzer. Beril kept
the header, cookie, meta and body idea and a 38 entry list, without the
Wappalyzer dependency.

## Report shape

Cover, table of contents, executive summary, subdomain table, port table,
technology table, email table, security analysis, AI owner view, AI hunter view,
appendix, PDF or JSON. The owner view asks for a summary, key findings,
protection recommendations and immediate actions. The hunter view asks for
promising targets, attack vectors, research areas and high value finding
classes. Beril already has profiles; the dual view is a product idea rather than
a new technique.

## What Beril took

- `scripts/recon.py`: passive source collection, wildcard check, host probe,
  fingerprint, takeover, origin score, auth surface, emails, inventory.
- `data/recon.json`: ports, paths, auth words, takeover markers, CDN ranges,
  headers, tech, wordlist, categories and score weights.
- `web_checks.py`: 25 extra exposed paths, 16 extra ports, an HSTS subdomain
  check.
- `agents/front-desk.md`: the owner and hunter split turned into a direct
  conversational entry, with a profile per reader.
- Knowledge cards for origin discovery, takeover and fingerprinting.
- `docs/recon.md` as the user guide.

## Bugs and weak spots in the source

Do not copy these blindly.

- `subdomains.py` strips `*.` after validating the name, so wildcard names pass
  validation and then collapse into the apex.
- `_check_subdomain` stores a bool in the DNS cache, while `_validate_subdomains`
  expects a dict. The cache branch is dead.
- `time.sleep(self.rate_limit_delay)` runs inside every worker, so 50 workers
  still sleep one second each before a request.
- Every request uses `verify=False` and hides the warning.
- DNS Dumpster scraping breaks when the CSRF field or markup changes.
- `dns_scan.cache_snooping` compares three unrelated timings. A cached answer is
  not proven.
- `ssl_scanner._check_protocols` maps TLS 1.3 to `PROTOCOL_TLS` and treats a
  successful connection as support for every version. `SSLv3` is reported
  through `SSLv23`, which cannot negotiate SSLv3 on modern Python.
- The `heartbleed` check is `scan_data.get('protocol') == 'TLSv1.1'`, a field the
  scan does not set. It is almost always false.
- Cipher enumeration calls `ssl._SSLMethod.PROTOCOL_TLS.get_ciphers()`, but the
  enum member has no such method, so the cipher block always raises and is
  swallowed. A single cipher is also set per connection, which cannot work for
  TLS 1.3 suites.
- `_process_certificate_info` calls `ssl._ssl._test_decode_cert(cert_dict)` with
  a dict, but the private helper wants a file path. The trust result is wrong.
- `_check_crl_revocation` collects CRL URLs and never fetches one.
- `_get_tls_fingerprint` returns a stub, not JA3.
- `real_ip_discovery._check_certificate_transparency` resolves every CT name,
  not the apex, which is correct inside the comprehension, but it submits one
  thread per name with a 50 certificate cap and no dedupe.
- `port_scanner.batch_scan` iterates the futures dict, not `as_completed`, so a
  slow first target blocks result collection.
- `_basic_port_check` caps a range at port 51, unrelated to the requested end.
- The AI prompt trusts scanner strings. A hostname or title with a newline and
  instruction text reaches the model unframed.
- `scan_results` and `scan_status` are process dicts. A restart loses every scan.
- The Groq key is assigned in `__init__` and overwrites the constructor argument.

## Gaps

- No zone transfer unless aggressive mode is on, and no real DNSSEC validation.
- No rate limit between subdomain HTTP probes, no budget, no robots.txt.
- No soft 404 baseline. A parked wildcard turns into hundreds of live hosts.
- No IPv6 handling in the socket fallback.
- No dedupe across sources before probing.
- No tests in the repo.

## Sources

- Repository tree at commit `a6d9650`, read on 2026-11-25.
- `README.md`, `app.py`, `core/*`, `modules/*`, `utils/*`, `templates/*`.
- GitHub API metadata for stars, dates and license.
