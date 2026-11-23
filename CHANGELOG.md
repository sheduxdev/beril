# Changelog

All notable changes. Beril uses semantic versioning.

## 1.4.0

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
- CycloneDX 1.5 SBOM with licence and a licence table.

### Attack and hunt

- `beril hunt` with a networkless sandbox and a maintainer report shape.
- Ownership verification through DNS TXT, file or meta tag.
- Reverse-engineering triage wrappers.

### Reports and automation

- Engineer, bug bounty, SMB and maintainer profiles from one JSON source.
- SARIF 2.1.0 output with a schema check.
- `--fail-on` severity gate and `--baseline` suppression.
- Adapters for installed Nuclei, Semgrep, Trivy, Gitleaks, OSV-Scanner, Grype,
  Syft and testssl.
- `beril ingest`, `beril watch`, `beril infra`, `beril image`, `beril netcheck`
  and `beril bgp`.
- Cached KEV, EPSS and OSV access, offline by default.
- SPDX 2.3 and OpenVEX output.
- Claude, Codex and Gemini plugin package.
- Local dashboard with a posture view.

### Packaging

- `pipx install .` and wheel installs resolve data and references from
  `share/beril`.
- Container image and a composite GitHub Action, both offline by default.

## 1.3.0 and earlier

The catalog, dossier, training and lab loop. See the git history.
