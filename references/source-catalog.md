# Source catalog

This file records what Beril reads and what was downloaded to build it. It is the provenance page. If a number in the dossier is challenged, start here.

Snapshot date: 2026-11-23.

## Network defense sources

Used for the network visibility, protection and runbook notes. Government and
standards sources outrank vendor explainers. Product docs are used for fields
and behavior, not for risk claims.

| Source | Endpoint | Format | Refresh | Notes |
|---|---|---|---|---|
| CISA CPGs | `https://www.cisa.gov/cybersecurity-performance-goals-cpgs` | HTML | quarterly | Cross-sector controls |
| CISA microsegmentation | `https://www.cisa.gov/sites/default/files/2025-07/ZT-Microsegmentation-Guidance-Part-One_508c.pdf` | PDF | yearly | Zero trust, phased |
| CISA communications hardening | `https://www.cisa.gov/resources-tools/resources/enhanced-visibility-and-hardening-guidance-communications-infrastructure` | HTML and PDF | yearly | Flow and config monitoring |
| NIST SP 800-94 | `https://csrc.nist.gov/pubs/sp/800/94/final` | HTML | on revision | IDPS classes and tuning |
| NIST SP 800-61r3 | `https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r3.pdf` | PDF | on revision | Incident response |
| MITRE ATT&CK T1071.004 | `https://attack.mitre.org/techniques/T1071/004/` | HTML | quarterly | DNS C2 and analytics |
| MITRE D3FEND | `https://d3fend.mitre.org/technique/d3f:NetworkIsolation/` | HTML | quarterly | Isolation taxonomy |
| SANS flow paper | `https://www.giac.org/paper/gcih/1241/shedding-light-security-incidents-network-flows/102204` | HTML | static | Flow use and limits |
| SANS capture paper | `https://symantec-enterprise-blogs.security.com/sites/default/files/2021-05/White%20Paper%20%28SANS%29%20-%20Packets%20or%20it%20didn%27t%20happen.pdf` | PDF | static | Metadata and retention tiers |
| Zeek docs | `https://docs.zeek.org/en/current/script-reference/log-files.html` | HTML | on release | Log fields |
| Suricata docs | `https://docs.suricata.io/en/latest/output/eve/eve-json-output.html` | HTML | on release | EVE fields |
| Sigma docs | `https://sigmahq.io/docs/basics/rules.html` | HTML | on release | Rule structure |
| Tetragon docs | `https://tetragon.io/docs/` | HTML | on release | eBPF telemetry |
| Cowrie | `https://github.com/cowrie/cowrie` | HTML | on release | SSH honeypot |
| Cloudflare DDoS | `https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/` | HTML | static | Attack layers and mitigations |
| Cloudflare ECH | `https://blog.cloudflare.com/encrypted-client-hello/` | HTML | static | ECH and SNI |
| RFC 8484 | `https://www.rfc-editor.org/rfc/rfc8484.html` | HTML | static | DoH |
| NIST SP 800-189 | `https://csrc.nist.gov/pubs/sp/800/189/final` | HTML and PDF | on revision | BGP security and DDoS |
| RFC 7454 | `https://www.rfc-editor.org/rfc/rfc7454.html` | HTML | static | BGP operations and security |
| RFC 6811 | `https://www.rfc-editor.org/rfc/rfc6811.html` | HTML | static | Origin validation |
| RFC 6480 | `https://www.rfc-editor.org/rfc/rfc6480.html` | HTML | static | RPKI architecture |
| RFC 7854 | `https://www.rfc-editor.org/rfc/rfc7854.html` | HTML | static | BGP Monitoring Protocol |
| RFC 7999 | `https://www.rfc-editor.org/rfc/rfc7999.html` | HTML | static | BLACKHOLE community |
| MANRS actions | `https://manrs.org/netops/actions/` | HTML | yearly | Routing security actions |
| MANRS Observatory | `https://observatory.manrs.org/` | HTML | live | Routing readiness |
| Hurricane Electric BGP Toolkit | `https://bgp.he.net/` | HTML | live | Prefix and ASN lookup |
| bgp.tools | `https://bgp.tools/` | HTML | live | Prefix, ASN and RPKI lookup |
| Routinator | `https://github.com/NLnetLabs/routinator` | HTML | on release | Local RPKI validator |
| ARTEMIS | `https://github.com/FORTH-ICS-INSPIRE/artemis` | HTML | on release | Hijack and leak detection |

## Competitive references

Used only for the comparison in `competitive-gap-analysis.md`. Product docs are
used for capabilities, not for independent benchmark claims.

| Tool | Endpoint | Refresh | Note |
|---|---|---|---|
| OWASP ZAP baseline | `https://www.zaproxy.org/docs/docker/baseline-scan/` | on release | Passive spider, rule config, CI exit codes |
| Nuclei | `https://docs.projectdiscovery.io/opensource/nuclei/overview` | on release | Template scanner, 6,500+ templates |
| Semgrep | `https://semgrep.dev/docs/getting-started/quickstart` | on release | SAST rule registry |
| Trivy | `https://trivy.dev/latest/docs/` | on release | Images, IaC, secrets, licences |
| OSV-Scanner | `https://github.com/google/osv-scanner` | on release | SCA, containers, call analysis |
| Gitleaks | `https://github.com/gitleaks/gitleaks` | on release | Secret scan, baseline, SARIF |
| TruffleHog | `https://github.com/trufflesecurity/trufflehog` | on release | 800+ detectors, live verification |
| Syft | `https://github.com/anchore/syft` | on release | SBOM in CycloneDX and SPDX |
| Prowler | `https://docs.prowler.com/` | on release | Multi cloud and K8s posture |
| Wazuh | `https://documentation.wazuh.com/current/index.html` | on release | SIEM, XDR, FIM, SCA |
| Strix | `https://github.com/usestrix/strix` | on release | Agentic pentest, PoC, autofix |

## Live sources

| Source | Endpoint | Format | Refresh | Notes |
|---|---|---|---|---|
| 0x00sec | `https://0x00sec.org/rss/` | RSS | weekly | Tag feeds at `/tag/{tag}/rss/` |
| 0x00sec deep dives | `https://0x00sec.org/deep-dive-series/` | HTML | monthly | Long-form series |
| Hack The Box Forum | `https://forum.hackthebox.com/latest.json` | JSON | weekly | Discourse |
| HTB top | `https://forum.hackthebox.com/top.json?t=year` | JSON | weekly | Sort by views or replies |
| Reddit | `https://sh.reddit.com/r/{sub}/top/?t=year` | HTML, shadow DOM | weekly | Warm the subreddit first |
| HackerOne Hacktivity | `https://hackerone.com/hacktivity/overview?...` | HTML grid | weekly | Public metadata only |
| Intigriti blog | `https://www.intigriti.com/researchers/blog` | HTML and RSS | weekly | RSS at `/researchers/blog/feed` |
| PortSwigger Research | `https://portswigger.net/research` | HTML and RSS | weekly | Author pages for people |
| PortSwigger Academy | `https://portswigger.net/web-security` | HTML | monthly | Labs and topic hubs |
| ProjectDiscovery blog | `https://projectdiscovery.io/blog` | HTML | weekly | Authors at `/blog/authors` |
| YesWeHack blog | `https://www.yeswehack.com/blog` | HTML | monthly | Sections under `/blog/*` |
| Assetnote / Searchlight | `https://www.slcyber.io/research` | HTML | monthly | Old blog redirects here |
| HackerOne blog | `https://www.hackerone.com/blog` | HTML | monthly | Program and researcher posts |
| GitHub topics | `https://github.com/topics/{topic}` | HTML | monthly | Stars are a snapshot |
| GitHub repo | `https://github.com/{owner}/{repo}` | HTML | monthly | `stargazerCount` in the page |
| GitHub raw README | `https://raw.githubusercontent.com/{owner}/{repo}/HEAD/README.md` | text | monthly | Install commands and flags |
| DEF CON media | `https://media.defcon.org/` | directory index | yearly | Talk archives |
| Hacker News | `https://hn.algolia.com/api/v1/search` | JSON | on demand | Lead generator |
| watchTowr Labs | `https://labs.watchtowr.com/rss/` | RSS | weekly | Appliance research |
| Horizon3 | `https://horizon3.ai/feed/` | RSS | weekly | CVE analysis |
| Trail of Bits | `https://blog.trailofbits.com/feed/` | RSS | weekly | Audits and tooling |
| Project Zero | `https://googleprojectzero.blogspot.com/feeds/posts/default?alt=rss` | Atom | weekly | Deep research |
| Bugtraq | `https://seclists.org/bugtraq/` | HTML | monthly | Historical advisories |
| infosec.exchange | `https://infosec.exchange/api/v1/timelines/public` | JSON | daily | Researcher posts |
| Lobsters | `https://lobste.rs/hottest.json` | JSON | on demand | Lead generator |
| NVD | `https://nvd.nist.gov/` | HTML and API | on demand | CVE enrichment |
| MITRE ATT&CK | `https://attack.mitre.org/` | HTML | quarterly | Technique IDs |
| CWE | `https://cwe.mitre.org/` | HTML | quarterly | Weakness IDs |
| OWASP WSTG | `https://owasp.org/www-project-web-security-testing-guide/latest/` | HTML | quarterly | Test cases |
| OWASP MASTG | `https://mas.owasp.org/MASTG/` | HTML | quarterly | Mobile tests |
| HackTricks | `https://book.hacktricks.wiki/` | HTML | quarterly | Command reference |
| PayloadsAllTheThings | `https://github.com/swisskyrepo/PayloadsAllTheThings` | Markdown | quarterly | Payload lists |
| Bugcrowd VRT | `https://bugcrowd.com/vulnerability-rating-taxonomy` | HTML | quarterly | Severity language |
| Exploit-DB | `https://www.exploit-db.com/` | HTML | monthly | Public exploit code |
| Packet Storm | `https://packetstormsecurity.com/` | HTML | monthly | Advisories and tools |
| Vulners | `https://vulners.com/` | HTML and API | on demand | Aggregator |
| Full Disclosure | `https://seclists.org/fulldisclosure/` | HTML | weekly | Raw advisories |
| Phrack | `http://phrack.org/` | HTML | yearly | Long-form exploitation |
| infosec.exchange | `https://infosec.exchange/` | Mastodon | daily | Researcher chatter |
| Black Hat archives | `https://www.blackhat.com/html/archives.html` | HTML | yearly | Slides and papers |
| OWASP events | `https://owasp.org/events/` | HTML | monthly | Conference index |

## Endpoint notes

### HackerOne query strings

```text
disclosed:true
disclosed:true&severity:critical
disclosed:true&program:shopify
disclosed:true&weakness:SSRF
```

The grid uses `pageIndex` for pagination and `sortField=latest_disclosable_activity_at`. The report body may be private even when the title and metadata are public.

### Reddit

`sh.reddit.com` renders `shreddit-post` web components. The useful attributes are on the element, not in the light DOM. Use Playwright to read the host, or parse the attributes from the HTML source.

### GitHub

The repo page embeds `"stargazerCount":12345`. The topic card embeds `Star 12.3k` in text. Prefer the precise number from the repo page.

### 0x00sec

RSS may arrive as a download. Fetch it from page context with `fetch()` after warming `https://0x00sec.org/`. The author field in the feed is usually the editorial account.

## Upstream skill corpus

The build downloaded 44 public repositories into `sources/` with shallow clones. The list and per-repo skill counts are in `data/upstream_repos.json`. The total was about 3.1 GB, and 22,976 `SKILL.md` files were found across 21 of them. Several repos vendor copies of the same skills, so the unique count is lower.

### Repositories with skill files

| Repository | SKILL.md | Use |
|---|---:|---|
| `ComeOnOliver/skillshub` | 12,423 | Large skill hub with vendored packs; search by name |
| `CyberStrikeus/CyberStrike` | 7,667 | Agent platform with a large bundled skill tree |
| `xalgorix/xalgorix` | 865 | 22-phase autonomous pentest methodology |
| `mukul975/anthropic-cybersecurity-skills` | 818 | Broad cybersecurity skill library, framework mapped |
| `H-mmer/pentest-agents` | 306 | Pentest agent roles and task skills |
| `Security-Talent/bugskill-ai` | 162 | Focused bug classes, each with a test procedure |
| `penligent/AIPentest_Skills` | 159 | API review, workflow, verification |
| `uphiago/recon-skills` | 137 | External recon, web, API, auth, reporting |
| `trailofbits/skills` | 99 | Audit, fuzzing, cryptography, supply chain |
| `trilwu/secskills` | 94 | Offensive and defensive skill pack |
| `elementalsouls/Claude-BugHunter` | 83 | Bug bounty skill bundle with disclosed report patterns |
| `BaaRai/ARTEX` | 0 | Autonomous agent platform with planner, workers and evidence |
| `NVIDIA/SkillSpector` | 34 | Skill quality and security review |
| `SubhiSec/claude-ai-cyber-security-skills` | 30 | Compact cyber skill set |
| `awarexone/Agentic-Bug-Hunter` | 26 | Full bug bounty workflow and vuln classes |
| `Masriyan/Claude-Code-CyberSecurity-Skill` | 22 | Claude Code security workflow |
| `samugit83/redamon` | 20 | Recon and automation skills |
| `GreyDGL/PentestGPT` | 17 | Autonomous pentest workflow |
| `crazyMarky/pentest-skills` | 11 | Recon, fingerprint, exploit, report |
| `Autumn-27/ScopeSentry` | 1 | Asset scope management |
| `KeygraphHQ/shannon` | 1 | Autonomous web and API pentest |
| `The-Art-of-Hacking/h4cker` | 1 | Large security corpus and references |

### Tool, data, and reference repositories

| Repository | Role |
|---|---|
| `0xSteph/pentest-ai-agents` | Agent definitions for pentest tasks |
| `0xsteph/pentest-ai` | Agent framework and prompts |
| `0xmaximus/Galaxy-Bugbounty-Checklist` | Checklist for bounty programs |
| `Armur-Ai/Pentest-Swarm-AI` | Multi-agent pentest orchestration |
| `Astrosp/Awesome-OSINT-List` | OSINT source list |
| `CISOfy/lynis` | Host security audit |
| `GhostTroops/scan4all` | Asset and vulnerability scanner |
| `Hack-with-Github/Awesome-Hacking` | Broad hacking resource index |
| `arkadiyt/bounty-targets-data` | Program scope data |
| `danieldurnea/FBI-tools` | OSINT and forensics tools |
| `dwisiswant0/awesome-oneliner-bugbounty` | One-liner bounty commands |
| `kpcyrd/sn0int` | OSINT framework |
| `lintsinghua/DeepAudit` | AI code audit |
| `nahamsec/Resources-for-Beginner-Bug-Bounty-Hunters` | Beginner resource list |
| `reddelexc/hackerone-reports` | Disclosed report collection |
| `six2dez/reconftw` | Recon automation framework |
| `skerkour/black-hat-rust` | Offensive Rust examples |
| `sundowndev/hacker-roadmap` | Learning roadmap |
| `swisskyrepo/PayloadsAllTheThings` | Payload and bypass reference |
| `vxcontrol/pentagi` | Autonomous pentest agents |
| `yogeshojha/rengine` | Recon and vulnerability management |
| `zan8in/afrog` | Vulnerability scanner |

Bug bounty material came from `elementalsouls/Claude-BugHunter`. Autonomous execution architecture came from `BaaRai/ARTEX`.

GhidRust material came from `DMaroo/GhidRust` and `oofz/Ghidrust`. Plugin inventory came from GitHub topic and search results, then folded into `data/re_tools.jsonl`.

Reverse-engineering material came from `0xSteph/pentest-ai-agents` (RE agent), `mukul975/anthropic-cybersecurity-skills` (Ghidra, jadx, Frida), `SnailSploit/Claude-Red` (exploit development, crash analysis, shellcode), `CyberStrikeus/CyberStrike` (Ghidra bridge and REA docs), `trailofbits/skills` (audit and fuzzing), and `skerkour/black-hat-rust`.

The upstream repos keep their own licenses. Check the license before copying text or code into a report or a product.

## Snapshot contents

The `data/` directory in this skill contains:

| File | Rows | What it holds |
|---|---:|---|
| `threads.jsonl` | 556 | Forums, reports, and article leads |
| `experts.jsonl` | 94 | Named researchers, handles, and works |
| `canonical_tools.jsonl` | 87 | Curated tool shelf with install lines |
| `methods.jsonl` | 156 | Method and research URLs |
| `method_details.jsonl` | 73 | Headings, intros, code density |
| `thread_details.jsonl` | 38 | Thread and report extracts |
| `re_tools.jsonl` | 570 | Reverse-engineering and exploitation tool shelf |
| `github_atlas.jsonl` | 2064 | Security repository atlas |
| `jobs.jsonl` | 10 | Job and cost ledger |
| `curriculum.json` | 25 | Training plan with drills and checkpoints |
| `learned_methods.jsonl` | 1 | Reflection notes from labs |

The snapshot is a sample, not a complete map. HackerOne alone publishes thousands of reports. The selection favors recent, public, and method-rich material.

HackForums contributes 42 rows from its public homepage and section feeds. A section pass is implemented in `harvest.py`, but Cloudflare clearance is intermittent. The data was collected with headful Camoufox under Xvfb and a persistent profile. If the challenge returns, use a new profile and a new IP, then retry.

## Refresh schedule

| Cadence | Sources |
|---|---|
| Weekly | HackerOne Hacktivity, Reddit top, 0x00sec RSS, PortSwigger research, ProjectDiscovery blog |
| Monthly | GitHub topics, tool stars, Intigriti, YesWeHack, HackerOne blog |
| Quarterly | OWASP, MITRE, CWE, HackTricks, PayloadsAllTheThings, upstream skill corpus |
| Yearly | Conference archives, DEF CON media, Phrack |

Write the date in the commit message every time you refresh. A catalog without a date is a rumor.

## Licensing and attribution

The live sources are quoted briefly and linked. The upstream repos were cloned for research. If you republish a large section from any of them, include the license and attribution required by that repository. The `data/` snapshot contains titles, links, short summaries, and metadata, which is enough to find the original.
