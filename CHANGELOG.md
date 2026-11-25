# Changelog

All notable changes. Beril uses semantic versioning.

## Unreleased

### Added

- `beril recon`: passive subdomain collection from crt.sh, Cert Spotter,
  HackerTarget and DNS Dumpster, a local wordlist, wildcard check, HTTP and
  HTTPS probe, technology fingerprint, takeover markers, origin IP scoring,
  auth surface and email collection. Inventory JSON plus Markdown. The seed
  data came from the ARTEX Flask app and is documented in
  `references/artex-flask.md`.
- `agents/front-desk.md`: direct conversational entry. A named target starts
  with a command instead of the four-question intake. Turkish and English
  triggers for break, find, map, secrets and artifact requests.
- `/beril:do` command and `beril-front-desk` plugin agent for natural sentences.
- `beril scan` accepts a bare domain and adds the scheme.
- 27 exposed paths from the same source, 16 more common ports, and an HSTS
  `includeSubDomains` check.

### Security

- Require `soupsieve>=4.1.3` and Python 3.11.5 or newer. The three open soupsieve
  advisories (exponential ReDoS in selector compilation, uncontrolled CSS parser
  recursion, polynomial descendant combinator DoS) are only fixed from 3.0.2 and
  4.0.0, and every fixed release needs Python 3.11.5 or newer.
- Record the synthetic Google and OpenAI keys in `benchmarks/secrets` as used in
  tests, so secret scanning carries a reason instead of a standing alert, and
  exclude that directory from scanning in `.github/secret_scanning.yml`.
- Track `uv.lock` with Dependabot instead of the pip files it cannot sync, and
  add a CI job that keeps the lock in step with `pyproject.toml` and audits it
  with `uv audit`.
- Add Python 3.14 to the test matrix and classifiers.
- Restore the dedicated `catalog` job that the main ruleset requires, so pull
  requests can merge again.

## 1.4.0 - 2026-11-23

The two-line model: defence scans on artifacts you own, an attack line with an
ownership gate, one finding and report schema for both.

### Defence

- Passive web scan with header, cookie and TLS checks, plus four active probes
  behind an ownership record.
- Source, APK, IPA, PE, ELF, JAR, MCP and Supabase/RLS passes.
- Secret scan with revocation order and masked output.
- Dependency inventory with offline OSV seed, optional OSV API and an import
  reachability grep.
- KEV and EPSS priority join over CVSS.
- CycloneDX 1.5 SBOM with purl, licence, vendored SHA-256 and a licence table.
- SPDX 2.3 and OpenVEX output, each checked against its official schema.
- Python AST rules and a thin JavaScript AST pass.

### Attack and hunt

- `beril hunt` with a networkless sandbox and a maintainer report shape.
- Ownership verification through DNS TXT, file or meta tag.
- Reverse-engineering triage wrappers.

### Reports and automation

- Engineer, bug bounty, SMB and maintainer profiles from one JSON source.
- SARIF 2.1.0 output with a schema check.
- `--fail-on` severity gate and `--baseline` suppression.
- Adapters for installed Nuclei, Semgrep, Trivy, Gitleaks, OSV-Scanner, Grype,
  Syft, testssl and ZAP, all mapped through the shared finding schema.
- SARIF 2.1.0 output checked against the official schema before it is written.
- `beril ingest`, `beril watch`, `beril infra`, `beril image`, `beril netcheck`
  and `beril bgp`.
- Cached KEV, EPSS and OSV access, offline by default.
- SPDX 2.3 and OpenVEX output.
- Claude, Codex and Gemini plugin package.
- Local dashboard with a posture view.
- MCP, skill and plugin supply-chain checks.
- A reviewed `.berilignore` file with reasons and expiry.
- CRA, maintainer and SMB report shapes, plus project health and evidence
  dossier profiles.
- Incident case library with a rule and a lab for each published case.
- Labeled benchmark corpus and measured precision and recall, weak results
  included.
- 189 tests on Linux, macOS and Windows across Python 3.10 to 3.13.

### Packaging

- `pipx install .` and wheel installs resolve data and references from
  `share/beril`.
- Container image and a composite GitHub Action, both offline by default.

## 1.3.0 and earlier

The catalog, dossier, training and lab loop. See the git history.
