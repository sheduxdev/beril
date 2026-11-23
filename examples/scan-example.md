# Scan: http://127.0.0.1:8099

Generated 2026-11-23T11:12:17+00:00 by Beril 1.4.0. Mode: passive.

| Severity | Count |
|---|---:|
| critical | 0 |
| high | 0 |
| medium | 2 |
| low | 4 |
| info | 3 |

## Fix now

1. **CSP missing** (medium, confidence high): Add a Content-Security-Policy that fits the app.
2. **HTTP answers and does not force HTTPS** (medium, confidence high): Add a permanent redirect and HSTS.

## Authorization

- No authorization record. Fine for passive checks, not for active ones.

## Scope

**Checks attempted**
- Security headers and CSP content
- Cookie flags
- CORS behavior (one Origin)
- Common exposed files and admin paths
- TLS certificate, expiry and version
- SPF, DKIM and DMARC records
- MySQL, PostgreSQL, MongoDB, Redis, Elasticsearch, Memcached and Docker ports
- Technology and version hints, error signatures, directory listing

**Checks not attempted**
- Pages and APIs behind a login
- Business logic, authorization and IDOR
- Parameter injection (active mode required)
- Content built by JavaScript
- Subdomains and hosts outside the inventory
- WAF rule quality and rate limit policy
- Known CVE matching (dependency scan is a separate command)

**Out of scope**
- Out of scope subdomains
- Write operations
- Authenticated areas

## Limits

- User agent: Beril/1.4 (authorized read-only scan; +https://github.com/sheduxdev/beril)
- Request budget: 250
- Requests sent: 38
- Rate limit: 2.0
- Backoff on 429/503: 0
- robots.txt: respected

## Findings

### [MEDIUM] CSP missing

- Confidence: high
- Source: passive
- CWE: CWE-693

**Evidence:** http://127.0.0.1:8099: header missing

```http
GET / HTTP/1.1
```

```http
HTTP 200
```

**Impact:** Browser defence is weak, so the impact of the same bug class grows.

**Fix:** Add a Content-Security-Policy that fits the app.

### [MEDIUM] HTTP answers and does not force HTTPS

- Confidence: high
- Source: passive
- CWE: CWE-319

**Evidence:** GET http://127.0.0.1:8099 -> HTTP 200

**Impact:** An active attacker can change the content.

**Fix:** Add a permanent redirect and HSTS.

### [LOW] X-Content-Type-Options missing

- Confidence: high
- Source: passive
- CWE: CWE-693

**Evidence:** http://127.0.0.1:8099: header missing

```http
GET / HTTP/1.1
```

```http
HTTP 200
```

**Impact:** Browser defence is weak, so the impact of the same bug class grows.

**Fix:** Set nosniff.

### [LOW] X-Frame-Options missing

- Confidence: high
- Source: passive
- CWE: CWE-693

**Evidence:** http://127.0.0.1:8099: header missing

```http
GET / HTTP/1.1
```

```http
HTTP 200
```

**Impact:** Browser defence is weak, so the impact of the same bug class grows.

**Fix:** Use CSP frame-ancestors or X-Frame-Options.

### [LOW] Referrer-Policy missing

- Confidence: high
- Source: passive
- CWE: CWE-693

**Evidence:** http://127.0.0.1:8099: header missing

```http
GET / HTTP/1.1
```

```http
HTTP 200
```

**Impact:** Browser defence is weak, so the impact of the same bug class grows.

**Fix:** Set strict-origin-when-cross-origin.

### [LOW] Permissions-Policy missing

- Confidence: high
- Source: passive
- CWE: CWE-693

**Evidence:** http://127.0.0.1:8099: header missing

```http
GET / HTTP/1.1
```

```http
HTTP 200
```

**Impact:** Browser defence is weak, so the impact of the same bug class grows.

**Fix:** Disable unused browser features.

### [INFO] COOP missing

- Confidence: high
- Source: passive
- CWE: CWE-693

**Evidence:** http://127.0.0.1:8099: header missing

```http
GET / HTTP/1.1
```

```http
HTTP 200
```

**Impact:** Browser defence is weak, so the impact of the same bug class grows.

**Fix:** Consider same-origin.

### [INFO] CORP missing

- Confidence: high
- Source: passive
- CWE: CWE-693

**Evidence:** http://127.0.0.1:8099: header missing

```http
GET / HTTP/1.1
```

```http
HTTP 200
```

**Impact:** Browser defence is weak, so the impact of the same bug class grows.

**Fix:** Consider same-site.

### [INFO] Server version exposed

- Confidence: high
- Source: passive

**Evidence:** http://127.0.0.1:8099: BerilLab/oops Python/3.14.9

**Impact:** Makes version specific matching easier.

**Fix:** Shorten the banner or hide the version.
