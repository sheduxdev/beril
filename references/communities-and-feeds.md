# Communities and feeds

Where defenders and researchers publish and discuss. Complements `references/forums.md` (which has tested fetch endpoints) with a broader, lower-maintenance list. Read for method and disclosed detail. A blog post is a lead, not a fact until confirmed by a CVE, advisory, vendor fix or a reproducible lab.

Snapshot 2026-11-26.

## Disclosure and writeups

| Source | Endpoint | Take |
|---|---|---|
| HackerOne Hacktivity | `https://hackerone.com/hacktivity` | Disclosed reports and fixes |
| Bugcrowd blog | `https://www.bugcrowd.com/blog/` | Methodology, program notes |
| Intigriti blog | `https://www.intigriti.com/researchers/blog` | Web bug writeups |
| PentesterLand writeups | `https://pentester.land/writeups/` | Aggregated bounty writeups |
| GitHub Security Advisories | `https://github.com/advisories` | Package advisories |
| Exploit-DB | `https://www.exploit-db.com/` | PoC archive, study only on your own lab |

## Research blogs

| Source | Endpoint | Take |
|---|---|---|
| PortSwigger Research | `https://portswigger.net/research` | New web primitives |
| Google Project Zero | `https://googleprojectzero.blogspot.com/` | Deep root-cause analyses |
| watchTowr Labs | `https://labs.watchtowr.com/` | Edge-device patch diffing |
| Assetnote | `https://www.assetnote.io/resources/research` | Appliance RCE research |
| Trail of Bits | `https://blog.trailofbits.com/` | Audits, tooling, crypto |
| Orange Tsai | `https://blog.orange.tw/` | Request smuggling, logic chains |
| Microsoft MSRC | `https://msrc.microsoft.com/blog/` | Vendor-side analysis |
| Rapid7 | `https://www.rapid7.com/blog/` | Vuln analysis, Metasploit notes |

## Blue team and detection

| Source | Endpoint | Take |
|---|---|---|
| SANS Internet Storm Center | `https://isc.sans.edu/diaries.html` | Daily defender diaries |
| SigmaHQ | `https://github.com/SigmaHQ/sigma` | Detection rules |
| Florian Roth / Nextron | `https://www.nextron-systems.com/blog/` | Detection engineering |
| The DFIR Report | `https://thedfirreport.com/` | Full intrusion timelines |
| Red Canary blog | `https://redcanary.com/blog/` | Threat detection |
| MITRE ATT&CK blog | `https://medium.com/mitre-attack` | Technique updates |
| Awesome Detection Engineering | `https://github.com/infosecB/awesome-detection-engineering` | Curated list |

## Communities (login or human in the loop)

| Source | Endpoint | Take |
|---|---|---|
| r/netsec | `https://old.reddit.com/r/netsec/` | Curated writeups |
| r/blueteamsec | `https://old.reddit.com/r/blueteamsec/` | Defender links |
| r/AskNetsec | `https://old.reddit.com/r/AskNetsec/` | Practitioner Q&A |
| 0x00sec | `https://0x00sec.org/` | Low-level, RE, red team |
| TryHackMe Discord/forum | `https://tryhackme.com/` | Learning community |
| Hack The Box forum | `https://forum.hackthebox.com/` | Machine and cert discussion |
| OWASP Slack | `https://owasp.org/slack/invite` | Project and appsec chat |

## Standards bodies and CERTs

| Source | Endpoint | Take |
|---|---|---|
| CISA | `https://www.cisa.gov/news-events/cybersecurity-advisories` | US advisories, KEV |
| NCSC UK | `https://www.ncsc.gov.uk/section/advice-guidance/all-topics` | Guidance |
| ENISA | `https://www.enisa.europa.eu/publications` | EU threat landscape |
| USOM (Türkiye) | `https://www.usom.gov.tr/` | Turkish national CERT alerts |
| FIRST | `https://www.first.org/` | CVSS, EPSS, CSIRT community |
| OWASP | `https://owasp.org/projects/` | Projects, cheat sheets, WSTG |

## Turkish-language

| Source | Endpoint | Take |
|---|---|---|
| USOM | `https://www.usom.gov.tr/` | Alerts and takedown lists |
| BTK / TR-CERT | `https://www.btk.gov.tr/` | Regulator and CERT notices |
| Mehmet Dursun İnce | `https://mdisec.com/` | Turkish offensive-security writeups |
| Canyoupwn.me archive | `https://canyoupwn.me/` | Turkish CTF and method notes |

Maintenance note. This list favors stability over tested endpoints. Before wiring any of these into a harvest job, confirm the feed URL and read `references/forums.md` for the sources that already have tested endpoints and parsing notes.
