# Scan: https://example.com

Scanned 2026-11-22T02:29:11+00:00. Read-only checks. Score: 10.

| Severity | Count |
|---|---:|
| critical | 0 |
| high | 0 |
| medium | 2 |
| low | 4 |
| info | 1 |

## Target

- URL: https://example.com
- HTTP status: 200
- Title: Example Domain
- TLS: TLSv1.3, expires Dec 25 22:56:35 2026 GMT (33 days)
- Issuer: SSL Corporation

## Findings

### Missing strict-transport-security

- Severity: medium
- Evidence: Header absent
- Advice: HSTS is missing. Add it on HTTPS responses.

### Missing content-security-policy

- Severity: medium
- Evidence: Header absent
- Advice: CSP is missing. Add a policy that fits the app.

### Missing x-content-type-options

- Severity: low
- Evidence: Header absent
- Advice: X-Content-Type-Options is missing. Set it to nosniff.

### Missing x-frame-options

- Severity: low
- Evidence: Header absent
- Advice: X-Frame-Options is missing. Use CSP frame-ancestors or DENY.

### Missing referrer-policy

- Severity: low
- Evidence: Header absent
- Advice: Referrer-Policy is missing. Set strict-origin-when-cross-origin.

### Missing permissions-policy

- Severity: low
- Evidence: Header absent
- Advice: Permissions-Policy is missing. Disable unused browser features.

### Server header exposed

- Severity: info
- Evidence: cloudflare
- Advice: Remove version details if the server does not need to advertise them.

## What this scan does not do

- No authentication, fuzzing, injection, or brute force.
- No JavaScript rendering. Use Camoufox harvesters for app flows.
- No vulnerability database match. Run nuclei separately for known CVEs.
- A clean result is a starting point, not a certification.
