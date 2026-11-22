# Artifact scan: ./fixture

Type: source. Scanned 2026-11-22T09:22:15+00:00. Static only. Score: 53.

| Severity | Count |
|---|---:|
| critical | 2 |
| high | 2 |
| medium | 5 |
| low | 6 |
| info | 5 |

Languages: Python (1), Terraform (1), JavaScript (1)
Files: 7  Lines: 27

## Findings

### CRITICAL

- **Possible aws access key**
  - Evidence: `.env: AKIAIOSFODNN7EXAMPLE`
  - Advice: Confirm the value is live and not a placeholder.
- **Possible stripe live key**
  - Evidence: `.env: sk_live_51H8xYzABC...`
  - Advice: Confirm the value is live and not a placeholder.
### HIGH

- **Possible database url**
  - Evidence: `.env: postgres://admin:s3cret@`
  - Advice: Confirm the value is live and not a placeholder.
- **Public S3 ACL**
  - Evidence: `infra/main.tf:1`
  - Advice: Confirm the bucket should be public.
### MEDIUM

- **Possible generic secret**
  - Evidence: `.env: sk_live_51H8xYzABC...`
  - Advice: Confirm the value is live and not a placeholder.
- **Debug mode enabled**
  - Evidence: `config.py:2`
  - Advice: Disable debug in production.
- **Python TLS verification disabled**
  - Evidence: `config.py:5`
  - Advice: Enable verification or pin a CA.
- **Ingress open to the world**
  - Evidence: `infra/main.tf:2`
  - Advice: Restrict to known ranges.
- **pull_request_target workflow**
  - Evidence: `.github/workflows/ci.yml:1`
  - Advice: Check out and run untrusted code carefully.
### LOW

- **Django allows every host**
  - Evidence: `config.py:3`
  - Advice: List the real hostnames.
- **CORS allows every origin**
  - Evidence: `config.py:4`
  - Advice: Restrict origins in production.
- **Docker base image uses latest**
  - Evidence: `Dockerfile:1`
  - Advice: Pin a version or digest.
- **Remote script piped to shell**
  - Evidence: `Dockerfile:2`
  - Advice: Pin a version and verify the checksum.
- **Workflow has write-all permissions**
  - Evidence: `.github/workflows/ci.yml:2`
  - Advice: Grant the minimum scope.
- **Missing package-lock.json**
  - Evidence: `package.json`
  - Advice: Commit the lockfile for reproducible builds.
### INFO

- **TLS verification disabled**
  - Evidence: `config.py:5 verify=False`
  - Advice: Review the data flow at this sink.
- **Dynamic code execution**
  - Evidence: `src/app.js:3 eval(`
  - Advice: Review the data flow at this sink.
- **Process execution**
  - Evidence: `src/app.js:1 child_process`
  - Advice: Review the data flow at this sink.
- **DOM HTML sink**
  - Evidence: `src/app.js:2 innerHTML`
  - Advice: Review the data flow at this sink.
- **.env present**
  - Evidence: `.env`
  - Advice: Make sure the file is gitignored and has no production secrets.

## Limits

- Static analysis only. Nothing was executed.
- Patterns can miss context and can flag placeholders.
- APK/IPA checks cover the manifest and obvious strings, not runtime behavior.
- Source checks are a lead generator. Confirm every hit by hand.
- A clean result is a starting point, not a certification.
