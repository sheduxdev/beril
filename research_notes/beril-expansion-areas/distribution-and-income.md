# Beril: global distribution, monetization, bug bounty policy, regional compliance, community

Scope note: coordinator changed scope to global adoption. Turkey reduced to one short note (see last section). Research used ~21 search calls, mostly search snippets, few full-page fetches. Confidence labels: [H] primary or multiple sources, [M] single secondary source, [L] aggregator or conflicting.

## 1. Distribution channels (reach and requirements)

### Takeaway
Skills ecosystem is cross-agent now (one SKILL.md works in Claude Code, Codex CLI, Copilot, Gemini CLI); the cheapest first moves are skills.sh install, Claude plugin directory submission, and PyPI. Homebrew core and Kali have notability gates a new solo repo will not pass at launch.

### Cited Findings
- Claude plugin directory: submit from a GitHub repo via developer portal claude.ai/directory/manage; older Console form unsupported; needs a claude.ai account with submit role (community form needs Team/Enterprise org with Directory permission); must follow Anthropic Software Directory Terms and Policy; validate step checks README, license, name uniqueness; `claude plugin validate ./plugin` runs locally; plugin.json fields icon, documentationUrl, supportUrl, privacyPolicyUrl, termsOfServiceUrl feed the listing [H] — [Anthropic submit docs](https://claude.com/docs/plugins/submit.md), [pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist)
- Sources conflict on whether the official marketplace `claude-plugins-official` takes form submissions; the community marketplace `claude-community` lists form-submitted plugins; impersonating names are blocked [M] — [official repo](https://github.com/anthropics/claude-plugins-official), [marketplace docs](https://code.claude.com/docs/en/plugin-marketplaces)
- Self-hosted marketplace (a GitHub repo with marketplace file) is also supported, no review needed [M] — [Claude Code docs](https://code.claude.com/docs/en/plugin-marketplaces)
- skills.sh (Vercel Labs, launched Feb 2026): npm-style installer `npx skills add/find/update/remove` from GitHub sources, install-count leaderboard aggregated across agents; core SKILL.md has no version field or lockfile (CLI adding lock/check commands) [M] — [Vercel](https://vercel.com/blog/introducing-skills), [Termdock](https://termdock.com/en/blog/cross-agent-skills-new-npm)
- Portable SKILL.md frontmatter: stick to `name` and `description`; agents each use own dotfile dirs, `.agents/skills/` read as fallback [M] — [Termdock](https://termdock.com/en/blog/cross-agent-skills-new-npm)
- Homebrew core: notability needs 30 forks/30 watchers/75 stars; self-submitted (owner or matching-domain author) needs 90/90/225 [H] — [Homebrew Acceptable Formulae](https://docs.brew.sh/Acceptable-Formulae). Own tap has no such gate (general Homebrew practice, not in these results).
- Kali: submissions via bug tracker, need a case for the tool, Debian-standard packaging, popularity/adoption weighed, tool creator willing to package helps; DoS/anonymity tools not installed by default [H] — [Kali submitting tools](https://www.kali.org/docs/tools/submitting-tools/)
- Black Hat Arsenal: separate Call for Tools from Briefings; open-source tools; submission needs description, license, changelog, install requirements, usage examples; Asia CFT 4 Sep–2 Nov 2026, notification 1 Dec 2026; Europe event 9–10 Dec 2026 [H] — [Arsenal resources](https://blackhat.com/arsenal-resources.html), [Asia](https://blackhat.com/asia/arsenal-overview.html)
- OWASP: project submission screened by coordinator, review 4–8 weeks, incubator leaders expected to ship draft release within 12 months [M, partly archived wiki pages] — [OWASP project working group](https://owasp.org/groups/project-working-group?tab=good-practices), [Project Stages](https://wiki.owasp.org/index.php/OWASP_Project_Stages)

### Inferences
- Order of effort: own repo + self-hosted marketplace, skills.sh, PyPI/pipx, own Homebrew tap, plugin directory form, then Arsenal CFT and OWASP after traction. Homebrew core, Kali, BlackArch only after stars/users exist.
- Beril already ships rules files for Cursor/Windsurf/Copilot/Gemini/AGENTS.md, which matches the cross-agent trend; keep SKILL.md frontmatter minimal for portability.
- Camoufox harvesting adds scraping-ToS risk that directory reviewers may question; document it as opt-in.

### Gaps
- No data found on actual install counts or reach of Claude directory, MCP registries, GitHub Marketplace/Actions, PyPI, AUR, BlackArch criteria, awesome-security contribution rules, DEF CON Demo Labs rules. Not searched or no result.

## 2. Monetization models of comparable tools

### Takeaway
Funded comparables are open core plus hosted cloud sold to teams. A solo developer cannot copy the VC path; realistic income is consulting/reports/training, with sponsorship as minor.

### Cited Findings
- Semgrep: open-source engine (LGPL-2.1), paid cloud platform priced per contributor; list prices vary by source ($20/$30/$40 per contributor per month) so unreliable; Opengrep fork seen as threat to monetizing the engine [M/L] — [dev.to](https://dev.to/rahulxsingh/is-semgrep-free-understanding-oss-vs-semgrep-cloud-in-2026-ge8), [Sacra](https://sacra.com/c/semgrep/), [Semgrep pricing](https://semgrep.dev/pricing)
- ProjectDiscovery (Nuclei): $25M Series A (2023) with launch of cloud platform as first commercial offering [H] — [Dark Reading](https://www.darkreading.com/cloud/projectdiscovery-announces-25m-series-a-financing-and-launch-of-cloud-platform), [TechCrunch](https://techcrunch.com/2023/08/17/projectdiscovery-raises-25m-to-launch-a-cloud-version-of-its-threat-scanning-platform/)
- Truffle Security (TruffleHog): $25M Series B Nov 2025, total over $40M, money for TruffleHog Enterprise; one source says revenue more than doubled [M] — [Intel Capital](https://www.intelcapital.com/truffle-security-raises-25-million-series-b-to-expand-nhi-security/), [SecurityWeek](https://www.securityweek.com/truffle-security-raises-25-million-for-secret-scanning-engine/)
- Aikido: free Developer plan (2 users, 10 repos); paid flat per 10 users: about $350/$700/$1,050 per month (one site says $300 for Basic) [L] — [Aikido pricing](https://www.aikido.dev/pricing?currency=eur), [G2](https://www.g2.com/products/aikido-security/pricing)
- Socket: free tier plus per-seat paid (Team about $25/dev/mo, Business about $50; sources differ, one reports a July 2026 free-cap increase unconfirmed) [L] — [Socket pricing](https://www.socket.dev/pricing)
- GitHub Sponsors: over $100M moved to maintainers by July 2026; no fee for personal sponsors, up to 6% for org sponsors; academic study says many maintainers do not earn enough to sustain projects [M] — [Help Net Security](https://www.helpnetsecurity.com/2026/07/21/open-source-github-sponsors-100-million/), [GitHub docs](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/about-github-sponsors-for-open-source-contributors), [arXiv](https://arxiv.org/abs/2202.05751)

### Inferences
- Free-tier-as-funnel is the shared pattern (Semgrep, Aikido, Socket). Beril equivalent: free local CLI, paid hosted dashboard/PDF reports/compliance mapping (CRA, SOC2, NIS2 evidence), or paid managed scans.
- Per-seat pricing mismatches a solo project; flat-fee report or per-scan packs fit better. Unverified suggestion.

### Gaps
- No evidence found for solo-developer security-tool income figures, paid-report market size, or training/course revenue. No Nuclei/TruffleHog list prices found.

## 3. Bug bounty as revenue path, AI policies

### Takeaway
Every major platform now allows AI assistance but penalizes unvalidated automated output; curl closed its bounty and maintainers ban slop. A scanner-driven pipeline only pays if every report is hand-reproduced with a PoC.

### Cited Findings
- HackerOne: AI allowed, same standards as human; automated or unverified output not accepted; Code of Conduct updated April 2026; submissions up 2.8x since Jan 2025 vs valid reports 1.9x; agentic validation checks scope/dupes; paused Internet Bug Bounty submissions April 2026 (cause not confirmed) [M/H] — [HackerOne blog](https://www.hackerone.com/blog/ai-driven-report-volume-insights-and-actions), [The Register](https://www.theregister.com/2026/02/18/hackerone_ai_policy/), [Privacy Guides](https://www.privacyguides.org/news/2026/04/17/hackerone-pauses-internet-bug-bounty/)
- Bugcrowd: unvalidated automated/AI submissions can bring 30-day suspension; rate limits for new researchers; bans for submission farming [H] — [Bugcrowd](https://www.bugcrowd.com/blog/bugcrowd-policy-changes-to-address-ai-slop-submissions/)
- Intigriti: AI use must be disclosed per Code of Conduct; triage is AI-assisted with human decision [M] — [Intigriti](https://www.intigriti.com/blog/business-insights/common-misconceptions-debugged)
- YesWeHack: no policy text found; one commentary describes credit-cost for invalid reports [L]
- curl ended its HackerOne bounty 31 Jan 2026 (announced 21 Jan); reports now via GitHub private reporting; project bans and publicly shames slop; Stenberg said he had not seen a valid AI-helped report (2025 statement) [H] — [Stenberg blog](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/), [The Register](https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/)
- Django issued AI-assisted report guidance; Seth Larson urges anti-automation and closing suspect reports; OSSF working group drafting maintainer guidance [M] — [Socket](https://socket.dev/blog/django-joins-curl-in-pushing-back-on-ai-slop-security-reports), [Help Net Security](https://www.helpnetsecurity.com/2026/05/18/problems-with-ai-assisted-vulnerability-research/)
- Apache Software Foundation stopped accepting huntr.com reports (quality, no API); huntr page notes discontinued [M] — [ASF](https://security.apache.org/huntr/)
- HackerOne reportedly cut bounty rewards May 2026 (headline only, not verified) [L] — [The Register](https://www.theregister.com/security/2026/05/21/hackerone-takes-an-axe-to-its-bug-bounty-rewards/5244458)

### Inferences
- Beril `hunt` output must stay as leads; only reproduced findings with PoC, affected version, and a suggested patch should be sent. Disclose AI use where required (Intigriti).
- Bounty income is irregular and falling for generic findings; treat as marketing proof (CVEs credited to Beril) more than revenue.

### Gaps
- No evidence on acceptance rates, YesWeHack and huntr current policy text, or average payouts.

## 4. Global regulatory and legal angle (replaces Turkey focus)

### Takeaway
EU CRA and NIS2 create demand for vulnerability handling and evidence tooling; US research legal safe harbor is narrow and policy-based; unauthorized scanning stays the main legal risk everywhere.

### Cited Findings
- EU CRA: manufacturer reporting of actively exploited vulnerabilities and severe incidents starts 11 Sep 2026; ENISA Single Reporting Platform from same date; open-source stewards' reporting duties apply from 11 Dec 2027; essential requirements from 11 Dec 2027; non-monetised FOSS outside scope (law-firm reading); one vendor says stewards cannot be fined [H/M] — [ENISA factsheet](https://www.enisa.europa.eu/sites/default/files/2026-07/ENISA_CRA_SRP_Factsheet_v1.0_0.pdf), [CSA note](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-cra-reporting-deadline-20260903-csa-sty/), [Patchstack](https://patchstack.com/articles/launching-managed-cra-article-14-reporting-for-open-source-maintainers/)
- US DOJ CFAA policy (May 2022): prosecutors should decline good-faith security research; "solely" good-faith testing; extortion excluded; does not bind state law or civil suits; EFF says insufficient [H] — [MoFo](https://www.mofo.com/resources/insights/220525-cyber-crime-charging-policy), [EFF](https://www.eff.org/deeplinks/2022/05/dojs-new-cfaa-policy-good-start-does-not-go-far-enough-protect-security)
- Kali excludes DoS-type tools from default install (dual-use sensitivity) [H] — [Kali policy](https://www.kali.org/docs/policy/penetration-testing-tools-policy/)

### Inferences
- Beril's ownership/scope gate and "never test without scope" rule is a selling point to enterprise and a legal shield; publish it as a safe-harbor-style policy.
- CRA reporting duty is a hook for EU SMB manufacturers (SBOM, deps reachability, vuln triage evidence). Verify scope with a lawyer.
- GDPR/NIS2 SMB angle plausible but unsupported by sources found here.

### Gaps
- Not found: NIS2 SME scope, GDPR specifics, SOC2 demand, SEC/CISA rules, UK Computer Misuse Act (no statutory research defence confirmed either way), APAC and LATAM regimes, harvesting/scraping ToS case law. Needs another pass before any legal claim goes in docs.

## 5. Marketing, i18n and community building

### Takeaway
Little direct evidence gathered on README conversion; community channels evidence is mostly conference/OWASP process. Findings below are limited.

### Cited Findings
- Arsenal and OWASP are the formal credibility channels (see section 1).
- Intigriti and HackerOne blogs show platforms favor disclosed, validated AI use, which supports an honest "what we did not test" positioning [M].
- skills.sh leaderboard makes install counts a visible social proof metric [M] — [Termdock](https://termdock.com/en/blog/cross-agent-skills-new-npm)

### Inferences
- Unsupported by gathered sources, treat as suggestions: demo GIF of one-command scan, honest comparison table versus Semgrep/TruffleHog/Nuclei with "where they win", benchmark on public vulnerable apps, EN-first README with community translations (ES, PT, ZH, JA, DE, FR, TR) kept as `docs/i18n/` with machine-translated drafts flagged, Discord or GitHub Discussions, awesome-list PRs, conference talks after a first CVE credit.
- Dashboard strings should be externalized early (key-based JSON) so translators do not touch code.

### Gaps
- No sources found on: README conversion studies, Discord community case studies of security tools, awesome-list acceptance rules, DEF CON Demo Labs, translation workflow tools. Not researched.

## 6. Turkey note (short)

- KVKK admin fines revalued yearly; 2025 data security (art. 12/18) range reported as 204,285–13,620,402 TL; 2026 revaluation rate reported 25.49% but figures not verified against kvkk.gov.tr [M] — [KVKK fine page](https://www.kvkk.gov.tr/Icerik/8145/6698-sayili-kisisel-verilerin-korunmasi-kanunu-kapsaminda-idari-para-cezasi-tutarlari), [Alomaliye](https://www.alomaliye.com/2025/01/10/2025-yili-6698-sayili-kisisel-verilerin-korunmasi-kanunu-kapsaminda-idari-para-cezasi-tutarlari/)
- Cybersecurity Law No. 7545 in force 19 Mar 2025; fines reported 10–100M TL; no SMB-specific rule found [M] — [EY Türkiye](https://www.ey.com/content/dam/ey-unified-site/ey-com/tr-tr/technical/ey-turkiye-yayinlar-raporlar/documents/ey-tr-digilaw-quarterly-siber-guvenlik.pdf)
- Kaspersky survey: 58% of Turkish SMBs hit by at least one incident in past year (publication date unverified) [M] — [Foreks](https://www.foreks.com/haber/detay/6a951e5fdb02cb53b9e7c3ac/FRKS/tr/kaspersky-raporu-turkiye-deki-kobi-lerin-58-i-siber-saldirilara-maruz-kaldi-31-08-26/)
- Turkish bounty platforms: BugBounter (2022: 1,500 hunters, 77M TL valuation) and Bug Hunty by D-Teknoloji; "BugBounty TR" not confirmed [M] — [Para Dergi](https://www.paradergi.com.tr/ayin-konusu/2022/03/01/odul-avcisi-sayisi-bin-500e-ulasti), [D-Teknoloji](https://www.d-teknoloji.com.tr/en/products/bughunty)
- Gap: no Turkish SMB spend figures found; TR best treated as one community translation.
