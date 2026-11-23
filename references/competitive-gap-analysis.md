# Competitive gap analysis

Beril is not a replacement for a DAST scanner, an SCA platform, a SIEM or a
cloud posture tool. This document scores it against each category, names where
it loses, and says what to borrow and what to leave.

Scores are 1 (weak) to 5 (best in class). They are judgments from the linked
documentation and the current repository, not benchmark results. A missing tool
in a category is not an insult; the point is fit.

## Score matrix

| Dimension | Beril | Best in class | Why Beril scores there |
|---|---:|---:|---|
| Breadth across artifact types | 4 | 3 | Web, source, APK, IPA, PE, ELF, JAR, MCP, Supabase, BGP |
| Depth per class | 2 | 5 | Four active probes, 27 source rules. Nuclei has 6,500+ templates |
| False positive control | 4 | 4 | Confidence, false positive note, dedupe. Baseline suppression just added |
| Evidence and replay | 5 | 3 | Request pair, file line, scope and limits in the schema |
| Report shapes | 5 | 3 | Engineer, bounty, SMB, maintainer, JSON, SARIF |
| CI integration | 3 | 5 | `--fail-on` and baseline now; no PR annotation or ticketing |
| Authenticated scanning | 1 | 5 | No session or token support |
| Scale and concurrency | 2 | 5 | One target, 2 requests per second |
| Dynamic runtime | 2 | 5 | Sandbox build only; no browser or proxy |
| Continuous monitoring | 1 | 5 | Manual runs, no scheduler or agent |
| Cloud, K8s and IaC posture | 1 | 5 | One Docker and Terraform rule, no API collector |
| Secret detection | 3 | 5 | 20 providers, masking, history. TruffleHog has 800+ detectors and live proof |
| Supply chain depth | 3 | 5 | Offline OSV seed, reachability grep. Trivy and OSV-Scanner have full databases and images |
| Network and BGP | 3 | 5 | Visibility and BGP checklist, passive lookup. No collector or validator |
| Cost and licence | 5 | 3 | MIT, no account, no per-seat fee |
| Local and private | 5 | 3 | No telemetry, no upload, offline by default |
| Maintenance and ecosystem | 2 | 5 | One maintainer, no plugin API, no integrations |
| Agent compatibility | 5 | 3 | Skill, routers and CLI for Claude, Codex, Gemini, Cursor, Cline |

## Category notes

### DAST: ZAP, Nuclei, Burp

ZAP's baseline scan spiders a site and runs passive rules, with a rule config
for FAIL, WARN and IGNORE, a progress file for known issues and CI exit codes.
Nuclei runs 6,500+ YAML templates over HTTP, DNS, TCP and file, with auth and
workflows.

Beril loses on coverage and authenticated flows. It wins on the honesty block
and the report shape. A team should run Nuclei or ZAP for depth and use Beril
for the brief and the scope gate.

### SAST: Semgrep, CodeQL, Bandit

Semgrep has a maintained rule registry and data flow. Beril's 27 rules are a
triage filter, not a SAST engine. Keep Semgrep as the engine and Beril as the
report and dedupe layer. Do not grow the rule set to hundreds by hand.

### SCA and SBOM: OSV-Scanner, Trivy, Syft, Grype

OSV-Scanner covers 11+ ecosystems, container images, OS packages and guided
remediation. Trivy adds IaC, secret, licence and Kubernetes scanning. Syft
produces CycloneDX and SPDX.

Beril emits CycloneDX 1.5 with a purl, licence and, for vendored packages, a
SHA-256 hash, plus SPDX 2.3 and OpenVEX. It still loses on database coverage,
image layers and remediation. It wins on the KEV and EPSS join and the import
reachability filter. The right split is Trivy or OSV
for the inventory, Beril for priority and the fix list.

### Secrets: Gitleaks, TruffleHog, GitGuardian

Gitleaks has baselines, allowlists, archive and decode depth, and SARIF.
TruffleHog has 800+ detectors, live verification and source coverage beyond git.

Beril loses on detector count and verification depth. It wins on the revocation
order and the fix text. For a serious secret program, use TruffleHog and let
Beril write the revoke plan.

### CSPM: Prowler, ScoutSuite, Wiz

Prowler supports AWS, Azure, GCP, Kubernetes, images, GitHub, M365 and LLM
providers with thousands of checks and compliance mapping.

Beril has one cloud rule. It cannot see an account. Add Prowler to the stack and
keep Beril for the cross-domain brief.

### SIEM and XDR: Wazuh, Splunk, Elastic

Wazuh covers agents, FIM, SCA, vulnerability detection, active response and
compliance. Beril has no agent and no event store. It wins only as a checklist
and report generator around the SIEM.

### NDR: Zeek, Suricata, Corelight, Darktrace

Zeek and Suricata are the open sensors. Beril documents them, does not run them.
A gap to close is a small pcap summary command, not a sensor.

### ASM: Shodan, Censys, Intruder, Detectify

These enumerate the external surface. Beril scans one target you name. Subdomain
and asset discovery is a later phase.

### Pentest agents: Strix, PentAGI, XBOW

Strix runs a browser, a proxy, a shell and a Python exploit sandbox in Docker,
with working PoCs and auto-fix. Beril runs four passive probes and a source
audit.

Beril loses on exploit depth and runtime. It wins on determinism, low cost and
the evidence schema. Strix needs an LLM key and Docker; Beril does not.

### BGP: Routinator, rpki-client, ARTEMIS, bgp.tools

Routinator and rpki-client validate RPKI. ARTEMIS detects hijacks from public
feeds. bgp.tools and HE give a public view.

Beril's `bgp` command is a lookup, not a monitor. It wins on the combined RPKI,
visibility and contact links in one report and on the runbook. Do not build an
RTR server.

### Niche checks

- MCP configs: `mcp-scan` and vendor linters. Beril's rules are simple and
  local. Good enough for a first pass, not a substitute.
- Supabase RLS: the Supabase CLI has a database linter with more policies.
  Beril's static check catches the missing migration line before deploy.
- JAR: capa and a decompiler do the depth. Beril's job is triage and hash.

## Where Beril wins

1. One schema across web, source, artifact, MCP, JAR, cloud config and BGP.
2. Scope, authorization and limits written into every report.
3. Low noise by design: confidence, false positive note, top five cap.
4. Local, MIT, no account, no telemetry.
5. Works as an agent skill, not only as a CLI.
6. Report profiles for four different readers from one evidence set.
7. Revoke-first secret guidance instead of a detector dump.

## Where Beril loses

1. Depth and template volume in every scanner category.
2. Auth, browser, proxy and stateful flows.
3. Scale, scheduling and continuous monitoring.
4. Cloud, Kubernetes and IaC API collection.
5. Integrations: tickets, chat, PR annotations, DefectDojo.
6. Detector and rule maintenance.

## What to borrow

| Borrow | From | Why |
|---|---|---|
| Baseline suppression | Gitleaks, ZAP | Known findings stay quiet without losing new ones |
| `--fail-on` severity gate | ZAP, Trivy | A CI check that can actually fail |
| Rule ignore file | ZAP, Semgrep | Per project tuning with a review trail |
| SARIF upload flow | Gitleaks, TruffleHog | Inline PR findings |
| Reachability and call analysis | OSV-Scanner | Fewer dependency false positives |
| Rule registry and tests | Semgrep | Community rules need a harness |
| Session and header auth | ZAP, Nuclei | Reach logged-in areas |
| Baseline of expected network state | SuzieQ | Drift detection, not one-shot |

## What not to borrow

- A browser engine. Playwright and Camoufox already exist.
- A package database. OSV and the vendors maintain it.
- An agent fleet and event store. Wazuh and Elastic do it better.
- Thousands of regex rules. Maintenance will win over quality.
- Exploit weaponization. Strix and Metasploit already do it.

## Position

Beril is the **scope gate, evidence schema and report layer** that sits on top
of specialist tools. Use it to decide what to run, to keep the output honest and
to hand a reader a fix list. Pair it with:

- Nuclei or ZAP for web depth.
- Semgrep for SAST.
- Trivy or OSV-Scanner for dependencies and images.
- TruffleHog for secrets.
- Prowler for cloud posture.
- Zeek and Suricata for traffic.
- Routinator and ARTEMIS for BGP.

## Closed in this pass

- `--fail-on` severity gate for CI.
- `--baseline` suppression by finding fingerprint.
- `beril bgp` passive lookup with RPKI state.
- Header, cookie and auth-file support for authenticated scans.
- Adapter layer for Nuclei, Semgrep, Trivy, Gitleaks, OSV, Grype, Syft and testssl.
- `beril ingest` for SARIF and tool JSON.
- `beril watch` with baseline diff and webhook.
- `beril infra` for Terraform, K8s, Docker and CloudFormation.
- `beril image` and `beril netcheck`.
- Claude, Codex and Gemini plugin package.
- Posture dashboard with trend, coverage and baseline suppression.
- Cached KEV, EPSS and OSV access with a seed fallback and an `--online` gate.
- SARIF 2.1.0 structural check before a document is written.
- CycloneDX hash and licence completion, SPDX 2.3 and OpenVEX output.
- 184 tests, including baseline, suppression, gate, feeds, SARIF schema, SPDX/VEX, adapters, AST, incidents, health, evidence,
  ingest, infra and plugin behavior.

## Still open

- Browser and proxy runtime inside Beril.
- Full cloud API collector and Kubernetes cluster collector.
- SARIF upload example for GitHub code scanning.
- DefectDojo and Jira export.
- Pcap summary command.
- Rule harness and community rule import.
- Multi-target scale beyond one host per run.

## Sources

- ZAP baseline scan: https://www.zaproxy.org/docs/docker/baseline-scan/
- Nuclei overview: https://docs.projectdiscovery.io/opensource/nuclei/overview
- Semgrep quickstart: https://semgrep.dev/docs/getting-started/quickstart
- Trivy user guide: https://trivy.dev/latest/docs/
- OSV-Scanner: https://github.com/google/osv-scanner
- Gitleaks: https://github.com/gitleaks/gitleaks
- TruffleHog: https://github.com/trufflesecurity/trufflehog
- Syft: https://github.com/anchore/syft
- Prowler: https://docs.prowler.com/
- Wazuh: https://documentation.wazuh.com/current/index.html
- Strix: https://github.com/usestrix/strix
- Zeek and Suricata docs in `network-visibility.md`
- Routinator and ARTEMIS in `bgp-security.md`
