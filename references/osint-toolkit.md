# OSINT toolkit

Open source intelligence is the part of recon that uses public records and
public posts instead of packets. The output is a lead sheet with a source and a
date, not a screenshot pile. Every claim needs a second source before it enters
a report.

Use this on a scope you own or a program asset. Public does not mean free of
terms. `references/recon.md` covers the host side. This file covers people,
organizations, certificates, archives and images.

## The method

1. Write the question. "Who owns this domain" and "which hosts exist" need
   different sources.
2. Name the evidence that would answer it.
3. Collect from two independent source classes.
4. Record the URL, the date and the confidence.
5. Discard a source that only repeats another source.
6. Archive before you quote. A page can change.

| Rung | Evidence |
|---|---|
| Lead | One post or one record |
| Corroborated | Two independent sources agree |
| Confirmed | A primary record or a direct observation |
| Attributed | A named owner or document links the fact to the target |

A report needs corroborated or better. A lead is a note.

## Domain and DNS

| Job | Source | Note |
|---|---|---|
| Registration | RDAP, whois | RDAP is structured and free |
| History | SecurityTrails, ViewDNS, DNS history | Free tiers are limited |
| Passive DNS | crt.sh, Cert Spotter, HackerTarget | Certificate names are not hosts |
| DNS records | `dig`, `dnsx` | A, AAAA, MX, TXT, NS, CAA |
| Zone transfer | `dig AXFR` | Try every NS |
| Wildcard | random label resolve | A wildcard invalidates brute force |
| Email policy | SPF, DMARC, DKIM selectors | `dig TXT` |
| Reputation | VirusTotal, URLhaus, Google Safe Browsing | A block is not a verdict |

Tools.

```bash
dig +short A example.com
dig +short MX example.com
dig +short TXT example.com
dig AXFR example.com @ns1.example.com
whois example.com
curl -s https://rdap.org/domain/example.com
```

## Certificates and ASN

Certificate transparency is the best free hostname source. It also exposes
internal names and old hosts.

| Job | Source |
|---|---|
| Certificate names | crt.sh, Cert Spotter, Censys |
| Certificate details | `openssl s_client`, crt.sh |
| ASN and prefix | `whois -h whois.radb.net`, bgp.tools, RIPEstat |
| BGP history | RIPEstat, BGPlay, BGPstream |
| RPKI state | `routinator`, Cloudflare RPKI portal |
| Reverse IP | HackerTarget, Shodan, Censys |
| Favicon hash | Shodan `http.favicon.hash` |

Censys and Shodan need an account. A free query budget is enough for a small
scope. Do not scan the whole internet from your laptop.

## Search engines and dorks

A dork is a query with a field. The engine does the crawl.

| Source | Field examples |
|---|---|
| Google | `site:`, `filetype:`, `inurl:`, `intitle:` |
| Bing | `site:`, `filetype:`, `ip:` |
| GitHub | `path:`, `filename:`, `org:`, `language:` |
| GitLab | `filename:`, `extension:`, `group:` |
| Shodan | `http.title:`, `http.favicon.hash:`, `ssl:` |
| Censys | `services.http.response.headers:` |
| FOFA | `body=`, `cert=`, `domain=` |
| ZoomEye | `app:`, `title:` |

High value dorks.

```text
site:example.com filetype:pdf
site:example.com inurl:admin
site:example.com ext:env OR ext:sql OR ext:bak
site:github.com "example.com" password
site:github.com org:example filename:.env
```

A dork hit is a URL. Open it and check that it is live and in scope.

## Code and secret exposure

| Job | Source |
|---|---|
| Public repos | GitHub, GitLab, Gitea, Sourcehut |
| Search | GitHub code search, grep.app, Sourcegraph |
| Secret scan | gitleaks, trufflehog, GitHub secret scanning |
| History | `git log -p`, `git filter-repo` |
| Package metadata | npm, PyPI, Maven, NuGet |
| CI config | workflow files, GitLab CI, Jenkinsfile |
| Dork for config | `filename:.env`, `filename:docker-compose.yml` |

A key in a public repo is a finding only after a read only verification and a
check of the exposed rights. Revoke first, then clean history.

## People and organizations

| Job | Source |
|---|---|
| Corporate registry | National company register, OpenCorporates |
| Ownership | Registry filings, annual reports, tender records |
| Officers | Registry, LinkedIn, press releases |
| Email format | Public emails, `theHarvester`, Hunter |
| Breach exposure | HIBP, DeHashed, LeakCheck |
| Social | LinkedIn, X, Mastodon, GitHub profile |
| Conference talks | YouTube, conference schedule, Papers |
| Job posts | Company careers, LinkedIn jobs |

Email format inference.

```text
first.last@, firstlast@, f.last@, first@
```

Collect five real addresses first. A format without a real sample is a guess.

## Archives

| Job | Source |
|---|---|
| Page history | Wayback Machine, archive.today |
| Dead link | Wayback, Common Crawl |
| Deleted post | Archive, search cache |
| Document metadata | `exiftool`, `pdfinfo` |
| Screenshot | A local capture with a timestamp |

Archive the page before quoting. A live URL can change under the report.

## Images and geolocation

| Job | Method |
|---|---|
| Reverse image | Google Lens, Yandex, Bing, TinEye |
| EXIF | `exiftool image.jpg` |
| Metadata strip | Check for GPS and device |
| Landmark | Sign text, skyline, road marks, plate style |
| Shadow | Sun angle and time of day |
| Weather | Historical weather for the claimed date |
| Map match | Street View, Mapillary, OpenStreetMap |

A location needs two independent cues. A single landmark is a lead.

## Corporate and infrastructure pivots

| Pivot | Why |
|---|---|
| ASN to prefixes | Finds hosting the org owns |
| Certificate org field | Finds related certificates |
| Favicon hash | Finds the same app on other hosts |
| Analytics ID | Finds sites with the same tag |
| MX and SPF include | Finds the mail provider |
| GitHub org | Finds repos and CI identities |
| Trademark and app store | Finds product names and package ids |
| Job post | Names the stack and the provider |

## Turkish sources

| Source | Use |
|---|---|
| USOM | Advisories and block lists |
| BTK | Regulator notices |
| Ticaret Sicili Gazetesi | Company notices |
| Resmî Gazete | Regulation and tenders |
| YÖK Akademik | Academic profiles |
| TÜBİTAK | Projects and calls |

Turkish company data is split across the trade registry and the official
gazette. Search the exact company title, not the brand.

## Verification

- Two source classes, not two pages on the same site.
- Primary record over an aggregator.
- Date every fact.
- Archive every quote.
- Check the scope before a host request.
- Label inference and keep it out of the fact column.
- A dead source stays in the note with the archive link.

## Tool table

| Tool | Job | Install |
|---|---|---|
| `dig`, `whois` | DNS and registration | System package |
| `amass` | Asset mapping | `go install` |
| `subfinder` | Passive hosts | `go install` |
| `dnsx` | DNS resolution | `go install` |
| `httpx` | HTTP probe | `go install` |
| `theHarvester` | Email and host | `pipx` |
| `gitleaks` | Secret scan | Release binary |
| `trufflehog` | Secret scan plus verify | Release binary |
| `exiftool` | Metadata | System package |
| `waybackurls` | Archive URLs | `go install` |
| `gau` | Known URLs | `go install` |
| `shodan` | Host search | `pipx` |
| `censys` | Certificate and host | `pipx` |
| `maltego` | Graph pivot | Desktop |
| `spiderfoot` | Automated OSINT | `pipx` |

Do not install all of them. Pick one per column and learn its noise.

## Legal and terms

Public data is still governed. Robots.txt, terms of service, database rights
and personal data rules apply. A login wall changes the terms. An API key is a
contract. A breach dump is not a public record.

- Keep a per source note on the terms and the login state.
- Minimize personal data. A dossier does not need a home address.
- Name the retention and the deletion owner.
- For a commercial deliverable, check the database licence.
- Turkey, KVKK applies to personal data even when the source is public.
- EU, GDPR applies when the subject is in the EU.

This is a working summary, not legal advice.

## Output

```markdown
## Lead
- Question:
- Fact:
- Source 1:
- Source 2:
- Archive:
- Date:
- Confidence: lead / corroborated / confirmed
- Scope note:
```

A lead without two sources stays a lead. That is the discipline.
