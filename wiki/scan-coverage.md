# Scan coverage

What each pass checks, and the limits it runs under.

## Web, passive

| Group | Checks |
|---|---|
| Headers | HSTS and max-age, CSP presence and weak directives, X-Content-Type-Options, frame, referrer, permissions, COOP, CORP, banner leaks |
| Cookies | `Secure`, `HttpOnly`, `SameSite`, per cookie |
| CORS | `*` plus credentials, origin reflection, `null` |
| Paths | 35 paths: `.git`, `.env` and variants, VCS metadata, backups, SQL dumps, server-status, phpinfo, `.DS_Store`, manifests, Actuator, Swagger and OpenAPI, GraphQL, phpMyAdmin, Adminer, WordPress, Joomla and Drupal admin and login, security.txt, robots.txt, sitemap |
| Transport | TLS version, issuer, subject, expiry, SAN list, HTTP to HTTPS |
| Mail | SPF presence and policy, DMARC presence and policy, common DKIM selectors |
| Network | Ports 3306, 5432, 27017, 6379, 9200, 11211, 2375 and 8080 with banner |
| Page | Status, title, generator and framework hints, SQL error signatures, debug traces, directory listing, password form over HTTP, source map hints |
| Soft 404 | Two random paths calibrate the baseline so a friendly 404 is not a finding |

### Request limits

| Limit | Value |
|---|---|
| Method | `GET` with a Beril user agent |
| Response size | 400 KB at most |
| `robots.txt` | Honored |
| Rate | 2 requests per second |
| Budget | 250 requests |
| Backoff | On 429 and 503 |

## Web, active

Ownership gated. Per discovered parameter:

| Probe | Looks for |
|---|---|
| One quote | SQL error signatures |
| One `<beril9f7z>` marker | Reflection |
| One protocol-relative URL on redirect parameters | Open redirect |
| One `../../etc/passwd` on file parameters | Path traversal |
| `OPTIONS` and `TRACE` | Method exposure |

No writes. No POST body, upload, SSRF callback or race. No working exploit is generated.

## Artifacts, static

Files are read, never executed.

| Type | Checks |
|---|---|
| APK | Manifest, exported components, permissions, deep links, hardcoded secrets, dangerous API calls, backup and debuggable flags, native libraries |
| IPA | `Info.plist`, URL schemes, ATS exceptions, embedded frameworks, secrets and entitlement clues |
| PE | Headers, sections, imports, signing clues, mitigation flags, embedded strings, secrets |
| ELF | Architecture, bits, RELRO, NX, PIE, canaries, imports, strings, SUID, secrets |
| JAR | `plugin.yml`, IOC files, class strings, external URLs, Base64, nesting, obfuscation, hash |
| Source | Secret patterns and history, 25 source rules, dangerous sinks, dependency and OSV match, Docker and CI review, fan-in |
| Archive | Zip and tar traversal, links, nested artifacts, text secrets |

## Other passes

| Pass | Covers |
|---|---|
| Secrets | Provider patterns, context filters, git history, masked output, a revocation link per hit. `--verify` sends the key to the provider and is off by default |
| MCP | Unpinned packages, plaintext keys, broad filesystem access, privileged containers, plain HTTP, instructions inside tool descriptions |
| Vibe | Missing RLS, `service_role` in the client, `NEXT_PUBLIC` secrets, unsafe HTML, open CORS, open Firebase rules |
| Dependencies | KEV, EPSS and CVSS joined to findings, with import reachability as a first filter |
| Infrastructure | Terraform, Kubernetes, Docker and CloudFormation rules |
| Network configs | sshd, nftables, DNS, nginx and HAProxy |

## What the scores mean

The priority score is severity times confidence, with verified and KEV boosts. It orders the work. It is not CVSS. A clean scan covers a short checklist: logged-in flows, business logic and authorization stay manual.

Detector precision and recall, including the weak spots, are in [Benchmarks](../docs/benchmarks.md).
