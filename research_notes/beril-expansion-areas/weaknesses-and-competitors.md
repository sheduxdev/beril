# Beril weaknesses vs competitors (gap analysis, Nov 2026)

Note: limited research budget. Repo facts verified by local inspection. Competitor facts only where cited; the rest marked inferred/unknown.

## 1. Repo inspection (size, depth, packaging)

### Takeaway
Beril is a small (~13k lines Python), young, regex/rule-table-driven toolkit with tiny data catalogs. Tooling hygiene (CI, lint, pyright, tests, SARIF, CycloneDX) is better than expected, but depth is snapshot-level.

### Cited Findings (all verified locally in /home/sheduxdev/Masaüstü/bounty/beril)
- scripts/*.py total 13,051 lines; largest: scan_artifact.py 1,153, web_checks.py 1,094, harvest.py 970, dashboard.py 759 (`wc -l`).
- Rule/data counts (python json load of data/*.json): secret_providers 16 providers; source_rules 27 rules; infra_rules 36 rules; mcp_rules 6 instruction patterns + 6 risky args; jar_iocs 4 files, 18 strings, 0 known_sha256, 10 plugins; cms_vulns wordpress 4 / drupal 2 / joomla 2; osv_seed 6 packages; kev 12 CVEs; epss 12 scores. data/methods.jsonl 191 lines.
- Tests: tests/ has 19 test files, 1,254 lines total. CI: .github/workflows/validate.yml runs ruff, ruff format, pyright, compileall, pytest, scripts/validate.py (Linux ubuntu-latest, Python 3.12 only). Only 2 workflows (validate, dependabot-auto-merge).
- Git: 40 commits total (`git log | wc -l`); recent commits mostly dependabot. Many modified/untracked files uncommitted at snapshot (gitStatus). Contributor breakdown not fully read (unknown; pyproject lists a single author).
- Packaging: pyproject.toml v1.4.0, setuptools, entrypoint `beril = scripts.beril_cli:main`, python>=3.10, deps camoufox[geoip], bs4, lxml, androguard, pefile, pyelftools; optional `re` extras (capa, floss, frida, pwntools, unblob...). uv.lock present. No Dockerfile found (glob error on Dockerfile*; inferred absent). No action.yml found (inferred: no GitHub Action).
- Output: SARIF rendering in scripts/report_render.py:362; CycloneDX 1.5 minimal SBOM in scripts/sbom.py:2. SPDX/VEX: grep hits scattered but no dedicated emitter confirmed (inferred absent).
- AST/dataflow: grep for `ast.` found no matching scripts (command output showed none); source rules are regex rule tables (inferred: no AST/taint engine). Verified: source_rules.json has 27 rules.
- Secrets: `--history` scans added lines in git history; `--verify` exists for provider read endpoints (scripts/beril_secrets.py:5-16) but only 16 providers have data.
- README limitations table (README.md:85-100): offline CMS/OSV seeds small; Linux is the tested platform, Windows/macOS "exist" but untested; dashboard single-user, no login; no automatic submission; deep tooling external (Ghidra, IDA, rizin, capa, MobSF, AFL++ need own install).
- Benchmarks: grep for benchmark/false-positive/baseline/suppress produced a list only partly inspected; no OWASP Benchmark/Juliet results found in docs (inferred none).

### Inferences
- Rule counts are 1-3 orders of magnitude below mature scanners; offline vuln data (12 KEV, 6 OSV packages) is a demo seed, not a database.
- No taint tracking means weak on injection/IDOR logic flows vs Semgrep/CodeQL.

### Gaps
- Performance on large repos not measured (`./beril validate` run attempted but timed out >120s in background; result not read).
- Exact commit/contributor count and test pass rate unknown.

## 2. Competitor comparison

### Takeaway
Every named competitor beats Beril on depth, ecosystem and scale in its own category. Beril's value is orchestration, not detection.

### Cited Findings
- TruffleHog: 800+ secret types classified, 700+ detectors with active verification, 29.6k stars, AGPL-3.0 — [GitHub](https://github.com/trufflesecurity/trufflehog). Beril: 16 providers. Beril weaker (~40x on detector count if the 700 figure is used).
- Gitleaks: 31.3k stars; git/dir/stdin modes, baselines, `gitleaks:allow`, `.gitleaksignore`, decoding, nested archives, JSON/CSV/JUnit/SARIF, pre-commit, GitHub Action, Docker, Homebrew; README says it is feature complete, in security-patch mode, maintainer moving to Betterleaks — [GitHub](https://github.com/gitleaks/gitleaks). Beril weaker on suppression workflow/integrations; gitleaks' stagnation is an opening.
- Semgrep rules repo: dirs for ~24 languages (apex, bash, c, clojure, csharp, dockerfile, elixir, go, html, java, javascript, json, kotlin, ocaml, php, python, ruby, rust, scala, solidity, swift, terraform, typescript, yaml); 1.3k stars; total rule count not stated on page — [GitHub](https://github.com/semgrep/semgrep-rules). Beril: 27 source rules. Weaker.
- Nuclei templates: official README shows `vuln` tag 6468 templates (undated); a third-party doc says 9,000+; 13.1k stars Oct 2026 — [README](https://raw.githubusercontent.com/projectdiscovery/nuclei-templates/main/README.md), [Mintlify](https://www.mintlify.com/projectdiscovery/nuclei/resources/template-library), [Star History](https://www.star-history.com/projectdiscovery/nuclei-templates/). Counts conflict by snapshot. Beril web_checks.py (1,094 lines) far smaller. Weaker.

### Inferences (not verified with sources this session; from general knowledge, treat as inferred)
- CodeQL/Semgrep/Snyk: interprocedural taint, auto-fix, IDE plugins, PR comments, SSO/RBAC, ticketing. Beril has none (dashboard is single-user no-login, README). Weaker/no equivalent.
- Trivy/Grype/Syft/OSV-Scanner: live advisory DBs, container/IaC/OS-package scanning, SPDX+CycloneDX, VEX. Beril: offline 6-package seed, minimal SBOM, `scripts/image.py` 107 lines only. Weaker.
- Socket/Aikido: package behavior analysis, malware feeds, continuous monitoring, SaaS. Beril: no continuous monitoring. Weaker.
- Burp/ZAP/XBOW: authenticated crawling, active scanner, fuzzing, extensions, autonomous exploit validation. Beril active.py 354 lines. Weaker.
- Ghidra/capa/Binary Ninja: Beril wraps capa/floss/rizin/Ghidra rather than competing; parity-by-delegation, requires manual installs.
- Maltego/SpiderFoot/Recorded Future/Shodan: Beril's Camoufox harvest of public pages; no graph, no internet-wide scan data, no commercial feeds. Weaker on coverage; different mode.
- MCP scanners (Invariant etc.): not researched; Beril's mcp_rules has 12 patterns. Competitive standing unknown.

### Gaps
- No current competitor numbers fetched for Semgrep total rules, CodeQL queries, Snyk, Socket, Aikido, Trivy, ZAP, XBOW, Invariant. Benchmarks (OWASP Benchmark, secret-scanner studies 2025-2026) not retrieved.

## 3. Differentiators (verified from repo/README/CLAUDE.md unless stated)
- Agent-native skill: single skill with loop, ownership gate (authz.py), scope file, networkless hunt sandbox, maintainer report generator; runs in Claude Code/Codex/Gemini/Cursor via adapter files.
- One tool spanning web scan, secrets+history, MCP audit, JAR/Minecraft plugin, vibe-coded app review, RE triage, training labs. No single competitor bundles all (inferred).
- Evidence-linked dossier from Camoufox harvest; local-first, no telemetry (README).
- Confidence labelling confirmed vs inferred; masking secrets; `--verify` off by default.
- Minecraft plugin JAR scanning niche: likely little competition (inferred).

## 4. Structural weaknesses
- Single maintainer, 40 commits, young (verified/partly): pyproject single author; low community.
- Unvalidated accuracy: no benchmark results found (verified absent in docs searched; inferred overall).
- Seed data snapshots (12 KEV CVEs) go stale; README admits it.
- Camoufox fragility: README admits CAPTCHAs/login walls win.
- Legal/ethical: harvesting forums/security sites risk ToS/copyright; README says public pages only. Legal exposure unquantified (inferred).
- LLM dependence/reproducibility: skill workflow relies on agent judgment; scan scripts deterministic but triage is agent-run (inferred).
- Linux-only tested; Windows/macOS unvalidated (README:93).
- Dependency heavy (camoufox, androguard, optional pwntools/frida) raises install fragility (inferred).

## 5. Ranked gaps and 10 fixes (impact x effort)
1. Publish accuracy benchmarks (OWASP Benchmark, Juliet subset, secret test corpora e.g. known-leak sets); show precision/recall. High impact, medium effort.
2. Replace seed vuln data with live OSV/KEV/EPSS fetch + cache (OSV API is free); high impact, low effort.
3. Expand secret providers 16 -> hundreds by importing gitleaks/TruffleHog-style rule formats (check license: TruffleHog AGPL, gitleaks MIT) plus entropy; add baseline/allowlist and `gitleaks:allow`-compatible suppression. High, medium.
4. Ship GitHub Action + Dockerfile + pip/pipx release + pre-commit hook. High, low.
5. Add SPDX and VEX output, validate SARIF against schema; keep CycloneDX full. Medium, low.
6. Delegate SAST to Semgrep (ingest its rules/SARIF) instead of 27 regex rules; add tree-sitter/AST for Python/JS. High, medium-high.
7. Windows/macOS CI matrix. Medium, low.
8. Adapter ingestion for Trivy/Grype/Nuclei/ZAP output into one normalized finding schema, with dedupe and FP triage. High, medium.
9. Reproducibility: pinned toolchain versions, run manifests, seed/date in every report; documented legal/ToS policy for harvesting. Medium, low.
10. Auto-fix suggestions as patches/PRs and ticket exports (Jira/GitHub issues), plus multi-user dashboard auth only if targeting teams. Medium-high, high.

### Gaps
- Effort/impact ranking is judgment, not measured.
