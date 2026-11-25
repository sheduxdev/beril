# Beril, security market expansion and competitor landscape (November 2026)

Note. Sources are mostly search summaries. Vendor pages were not fetched directly. Price confidence is LOW and every figure needs verification. The Beril README and SKILL.md were not read for this pass, the capability list in the assignment was used.

## 1. Competitors by area, product, price and openness

### Takeaway
AppSec, SCA and secret scanning are crowded and mature. Free open source cores exist (gitleaks, TruffleHog, Trivy, Grype, Nuclei) and the commercial side prices per user or by quote. Agent, MCP and AI pentest work attracted money fast in 2026.

### Cited findings
- Snyk has a free tier (200 OSS tests per month) and Team at about $25 per developer per month (third party blog, low confidence). [dev.to](https://dev.to/rahulxsingh/is-snyk-worth-the-cost-complete-pricing-breakdown-for-2026-39m1)
- Semgrep has a free tier. Paid rates conflict across sources ($30 vs $35 per contributor per month). [stackpick](https://stackpick.net/blog/best-snyk-alternatives-2026/), [safeguard.sh](https://safeguard.sh/resources/blog/appsec-and-sca-pricing-compared-what-drives-cost-and-where-the-free-options-stop)
- Aikido has a free Developer plan and flat paid tiers. It acquired Root for $70M, date unverified. [aikido.dev](https://aikido.dev/blog/snyk-vs-semgrep), [bankinfosecurity](https://www.bankinfosecurity.com/latest-news/application-security-c-482/p-1)
- Endor Labs prices by quote (contributor per year). It acquired Autonomous Plane on 13 Feb 2026. Total funding conflicts between $188M and $208M. [sacra](https://sacra.com/research/endor-labs-vs-snyk/), [cbinsights](https://www.cbinsights.com/investor/endor-labs)
- Socket raised a $60M Series C at a $1B valuation on 20 May 2026. The Secure Annex acquisition on 28 Apr 2026 added a browser extension, editor extension, MCP server and AI tools. [socket.dev](https://socket.dev/blog/socket-raises-60m-series-c-press-release), [socket.dev](https://socket.dev/blog/socket-acquires-secure-annex)
- Secret scanning. gitleaks is MIT and free but in maintenance mode per one source, and its GitHub Action wants a license key in org repos. TruffleHog is AGPL-3.0 in most sources (one calls it Apache, a conflict) and Enterprise pricing is private. GitGuardian is freemium per contributor. GitHub Secret Protection is $19 per active contributor per month. [tech-insider](https://tech-insider.org/trufflehog-vs-gitleaks-vs-gitguardian-2026/), [gitguardian.com](https://www.gitguardian.com/pricing), [dev.co](https://dev.co/security/open-source/trufflehog)
- Agent and MCP scanning. Snyk agent-scan, formerly the Invariant MCP scanner, runs `uvx snyk-agent-scan`. It starts MCP servers from the config and sends tool descriptions to the Snyk API, reported for version 0.4.3. It appeared on the Thoughtworks Radar in Apr 2026. [github.com/snyk/agent-scan](https://github.com/snyk/agent-scan), [dev.to](https://dev.to/bawbel/snyk-scans-your-mcp-servers-by-running-them-here-is-what-that-means-a4b), [thoughtworks](https://www.thoughtworks.com/en-cl/radar/tools/agent-scan)
- Cisco mcp-scanner is open source, license unverified. It combines YARA, an LLM judge, the Cisco AI Defense API and behavioral code analysis. RSAC 2026 showed DefenseClaw with MCP Scanner, Skills Scanner, AI BoM and CodeGuard. [github.com/cisco-ai-defense/mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner), [cisco blog](https://blogs.cisco.com/ai/ciscos-mcp-scanner-introduces-behavioral-code-threat-analysis), [newsroom](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m03/cisco-reimagines-security-for-the-agentic-workforce.html)
- Bug bounty and AI pentest. XBOW raised a $120M Series C on 18 Mar 2026 at over $1B valuation and integrated with Microsoft Security Copilot and Sentinel. HackerOne US leadership in 2025 was about 1060 reports with human review. [businesswire](https://www.businesswire.com/news/home/20260318258057/en/XBOW-Raises-$120M-to-Scale-its-Autonomous-Hacker), [helpnetsecurity](https://www.helpnetsecurity.com/2025/06/25/xbow-ai-funding/)
- Open source AI pentest. Shannon (Keygraph, Lite AGPL-3.0, source analysis plus live exploit), Strix (Apache-2.0, Docker sandbox) and PentestGPT. One third party comparison scored Escape 75%, Claude 70%, Shannon 30% and Strix 5%, a single data point. [helpnetsecurity](https://www.helpnetsecurity.com/2026/02/02/open-source-ai-pentesting-tools-test/), [stingrai](https://www.stingrai.io/blog/open-source-ai-pentest-agents-compared-2026)
- ProjectDiscovery. Nuclei OSS is free. Cloud Pro is about $2,500 per year or $200 per seat per month, sources conflict. Neo, the AI attacker platform, went GA in Aug 2026 with pay as you go and BYOK. [docs.projectdiscovery.io](https://docs.projectdiscovery.io/cloud/pricing), [prnewswire](https://www.prnewswire.com/news-releases/projectdiscovery-makes-neo-generally-available-with-pay-as-you-go-pricing-302842104.html)
- Container and IaC OSS. Trivy covers image, filesystem, repo, K8s and IaC with SARIF and VEX. Syft and Grype cover SBOM and advisory matching with SARIF and OpenVEX. Checkov covers IaC with disputed quality. Kubescape prioritizes runtime loaded vulnerabilities. [aikido trivy-alternatives](https://www.aikido.dev/blog/trivy-alternatives), [armosec](https://www.armosec.io/blog/best-kubernetes-dependency-scanners/)

### Inferences
Most OSS competitors do one job, such as secrets, SCA or MCP. Beril's single evidence chain is a differentiator, but it loses on depth in each area alone.
The agent-scan habit of running the config is a clear contrast with Beril's static first and networkless principle.

### Gaps
Burp AI by PortSwigger, exact Semgrep, Socket and Endor prices, the Aikido acquisition date and the Cisco license were not verified. The data sending behavior of current Snyk agent-scan was not verified.

## 2. Gaps, local, evidence linked, OSS and scope gated

### Takeaway
The strongest gaps are (a) static, networkless, local scanning for the agent and MCP supply chain, (b) maintainer friendly verified reports and (c) Minecraft and game mod malware. SMB and KVKK focus is also an area the large players leave aside except on price and language (inference).

### Cited findings
- curl closed its bug bounty on 21 Jan 2026, ending 31 Jan. At the peak about 20% of reports were "AI slop". Reports moved to GitHub private vulnerability reporting, and sources conflict on the paid HackerOne channel. Stenberg accepts good AI assisted reports. [daniel.haxx.se](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/), [theregister](https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/)
- Fractureiser in 2023 was a four stage Windows and Linux infostealer in CurseForge and Bukkit mods, spread through compromised developer accounts. No new 2026 campaign was found. CurseForge has its own jar scanner and the community has scripts. [bitdefender](https://www.bitdefender.com/blog/labs/infected-minecraft-mods-lead-to-multi-stage-multi-platform-infostealer-malware), [kaspersky](https://www.kaspersky.com/blog/curseforge-compromised-fractureiser/48388/), [github](https://github.com/fractureiser-investigation/fractureiser/blob/main/README.md)
- Veracode 2026 found about 44% of AI code tasks bring a risky vulnerability and the average pass rate is 56% (2025 was 55%), with XSS pass at 15%. Escape.tech found 2,038 critical vulnerabilities in 1,400 vibe-coded apps. [veracode](https://www.veracode.com/blog/2026-genai-code-security-report-ai-risk), [CSA note, AI assisted and not official](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/)

### Inferences
Maintainers are tired of low quality AI reports. Reproduced output, sandbox evidence and an ownership gate are Beril's direct value offer (medium confidence).
No commercial competitor was found for Minecraft and JAR scanning, but the search was limited. The niche is low competition (low to medium confidence).
The vibe-coded app competitors found are enterprise products (Veracode, Escape). No local OSS equivalent appeared (low confidence).

### Gaps
No search for OSS tools focused on SMB and KVKK. No GitHub OSS competitor inventory for Minecraft scanning with stars and last commit.

## 3. Expansion ideas

### Takeaway
Lowest cost and highest demand are SARIF plus SBOM and VEX output, a GitHub Action and CRA ready reporting. Medium are browser and IDE extension scanning, and mobile. High cost and saturated are IaC and K8s, and LLM red team.

### Cited findings
- Trivy and Grype support SARIF and VEX output (OpenVEX, CycloneDX VEX, CSAF). Cross tool consistency in VEX generation is an open problem. [arxiv](https://arxiv.org/html/2503.14388v3), [aikido](https://www.aikido.dev/blog/trivy-alternatives)
- The Trivy GitHub Action was compromised by TeamPCP on 23 Mar 2026, with SHA pinning advised. CI extension distribution carries trust risk. [tech-insider](https://tech-insider.org/trivy-tutorial-2026/), a secondary source with low to medium confidence.
- Socket expanded plugin, MCP and AI tool coverage in Apr 2026, demand evidence for browser and IDE extension scanning. [socket.dev](https://socket.dev/blog/socket-acquires-secure-annex)
- The IaC and K8s space already has free and established Trivy, Checkov and Kubescape. [armosec](https://www.armosec.io/blog/best-kubernetes-dependency-scanners/)
- ProjectDiscovery Neo and XBOW position continuous attack surface and autonomous pentest at enterprise pricing. [prnewswire](https://www.prnewswire.com/news-releases/projectdiscovery-makes-neo-generally-available-with-pay-as-you-go-pricing-302842104.html)

### Inferences, suggested order
1. SARIF plus CycloneDX and OpenVEX output for every `beril scan/deps/secrets/mcp/jar` command. Small work, compatible with CI, GitHub Code Scanning and CRA.
2. An own GitHub Action, SHA pinned, with networkless mode as the default. The Trivy Action incident makes this a differentiator.
3. Deeper static MCP, agent and skill scanning plus extension (VS Code and browser) coverage.
4. Report profiles for maintainer, SMB and CRA or KVKK mapping. No source was found for ISO 27001 or SOC2 mapping.
5. Avoid a full IaC or K8s engine and LLM red team. Both are crowded and the answer is unclear.
Confidence is medium and the order is not evidence ranked. No market size figure was found.

### Gaps
Not researched, ISO 27001, SOC2 and KVKK mapping tools, APK and IPA OSS competitors such as MobSF, LLM red team tools such as garak and promptfoo, threat actor and ransomware dossier competitors such as MISP and OpenCTI.

## 4. Demand trends in 2025 and 2026

### Takeaway
Four strong drivers are supply chain worms in npm and against MCP and AI tools, AI code vulnerability, CRA reporting and AI slop breaking bug bounty.

### Cited findings
- Shai-Hulud started in Sep 2025. The "2.0" wave in Nov 2025 covered 796 packages and 1,092 versions. In Apr 2026 @bitwarden/cli 2026.4.0 targeted `~/.claude.json` and `~/.claude/mcp.json`. Mini Shai-Hulud on 11 May 2026 hit the TanStack tree, Mistral AI, UiPath and OpenSearch, and the source was published on 12 May. On 1 Jun 2026 at least 32 packages under @redhat-cloud-services were hit. SANDWORM_MODE redirects MCP entries to attacker infrastructure. The worm packages carried valid SLSA L3 provenance. [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-shai-hulud-npm-worm-ai-developer-supply-ch/), [Akamai](https://www.akamai.com/blog/security-research/2026/may/mini-shai-hulud-worm-returns-goes-public), [Unit 42](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/)
- npm closed the install hook issue on 12 Jul 2026 according to Socket, the publish side is still opt in. [socket.dev glossary](https://socket.dev/glossary/shai-hulud.md)
- EU CRA Article 14 reporting started on 11 Sep 2026 for actively exploited vulnerabilities and severe incidents, including products already on the market. The single reporting platform URL was not published as of 8 Sep. Machine readable SBOM is due 11 Dec 2027. Non commercial OSS is mostly out of scope and the steward reporting regime starts 11 Dec 2027. [Travers Smith](https://www.traverssmith.com/knowledge/knowledge-container/the-eu-cyber-resilience-acts-vulnerability-and-incident-reporting-requirements-are-now-live/), [Goodwin](https://www.goodwinlaw.com/en/insights/publications/2026/09/alerts-lifesciences-technology-preparing-for-eu-cyber-resilience-act), [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-cra-vulnerability-reporting-20260910-cs/), [EC](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)
- The Trivy Action and release infrastructure were compromised in Mar 2026, see section 3.

### Inferences
The security tool itself is a target. Tool supply chain trust, with SHA pins, networkless runs and signed releases, is a marketing point.
Provenance alone is not enough. An SLSA L3 worm package proves it. Behavior and content analysis are required.

### Gaps
ENISA and CISA primary pages were not fetched. No Gartner or Forrester summaries were found. Market size data was skipped on purpose.
