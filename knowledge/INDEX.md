# Knowledge index

90 durable cards. Read this before a web search; open a card only when it matches.

| id | title | tags | confidence | updated |
|---|---|---|---|---|
| `ad-acl-path` | AD compromise is an edge path, not a single bug | ad, windows, acl | high | 2026-11-24 |
| `ad-adcs-esc1` | ESC1 is an enrollable SAN on a client-auth template | ad, adcs, certificate | high | 2026-11-24 |
| `ai-memory-poison` | Agent memory is a write target | ai, agent, memory | high | 2026-11-24 |
| `ai-agent-tool` | Agent tool abuse is argument control, not prompt text | ai, agent, tool | high | 2026-11-24 |
| `ai-cost-control` | An agent loop is a budget bug | ai, cost, agent | medium | 2026-11-24 |
| `ai-indirect-injection-tool` | Indirect injection turns a document into an instruction | ai, llm, prompt-injection | high | 2026-11-24 |
| `ai-mcp` | MCP config is a trust boundary with filesystem and network rights | ai, mcp, config | high | 2026-11-24 |
| `ai-data-poison` | Poisoned data changes the model or the retrieval set | ai, data, poisoning | high | 2026-11-24 |
| `ai-rag-tenant-filter` | RAG leaks when retrieval ignores the tenant | ai, llm, rag | high | 2026-11-24 |
| `api-webhook-signature` | A webhook without HMAC is an unauthenticated write | api, webhook, hmac | high | 2026-11-24 |
| `api-mass-assignment` | Mass assignment is a binder trusting extra fields | api, json, mass-assignment | high | 2026-11-24 |
| `api-rate-limit-bypass` | Rate limits are only as strong as the key | api, rate-limit, bypass | high | 2026-11-24 |
| `api-grpc-reflection` | gRPC reflection is a map, per-method auth is the bug | api, grpc, reflection | medium | 2026-11-24 |
| `binary-kernel` | A kernel bug is an object lifetime bug with a user buffer | binary, kernel, driver | high | 2026-11-24 |
| `binary-browser` | Browser exploitation needs a renderer bug and a sandbox path | binary, browser, jit | high | 2026-11-24 |
| `browser-extension-permissions` | An extension is a trusted page with broad APIs | browser, extension, permissions | medium | 2026-11-24 |
| `cloud-docker-socket` | A mounted Docker socket is root on the host | cloud, docker, container | medium | 2026-11-24 |
| `cloud-k8s-hostpath` | A privileged pod with hostPath is a host escape | cloud, kubernetes, container | high | 2026-11-24 |
| `cloud-azure-role` | Azure identity is a role assignment graph | cloud, azure, iam | high | 2026-11-24 |
| `cloud-metadata-role` | Cloud metadata is a credential endpoint | cloud, ssrf, iam | high | 2026-11-24 |
| `cloud-gcp-iam` | GCP IAM binds a member to a role on a resource | cloud, gcp, iam | high | 2026-11-24 |
| `cloud-iam-wildcard` | IAM wildcard is administrator access until proven otherwise | cloud, iam, aws | high | 2026-11-24 |
| `cloud-terraform-state` | Terraform state is a secret store | cloud, terraform, state | medium | 2026-11-24 |
| `container-escape` | A container escape is a host resource exposed to the container | container, escape, kubernetes | high | 2026-11-24 |
| `key-management` | Key management is where crypto bugs become data bugs | crypto, keys, storage | medium | 2026-11-24 |
| `crypto-weak-random` | Predictable randomness is a key recovery bug | crypto, random, predictability | high | 2026-11-24 |
| `tls-config-review` | TLS is a version, a chain and a policy | crypto, tls, certificate | medium | 2026-11-24 |
| `detection-sigma` | A Sigma rule needs a logsource, a selection and a false-positive note | detection, sigma, log | high | 2026-11-24 |
| `detection-beacon` | A beacon is a timing pattern, not a single request | detection, beacon, network | medium | 2026-11-24 |
| `electron-context-isolation` | Electron is Node with a browser attached | electron, desktop, context-isolation | medium | 2026-11-24 |
| `exploit-uaf-reallocate` | UAF becomes control when the freed slot is reallocated | exploit, uaf, heap | high | 2026-11-24 |
| `exploit-rop-argument-registers` | x86_64 ROP needs the argument registers | exploit, rop, linux | high | 2026-11-24 |
| `firmware-update-sign` | A signed update is useless if verification is off | firmware, update, signature | high | 2026-11-24 |
| `firmware-cgi-injection` | Firmware CGI builds a shell string from the query | firmware, iot, command | high | 2026-11-24 |
| `firmware-jtag` | JTAG and SWD are identified by pinout and IDCODE | firmware, hardware, jtag | medium | 2026-11-24 |
| `firmware-spi` | SPI flash reads need two matching dumps | firmware, hardware, spi | medium | 2026-11-24 |
| `firmware-uart` | UART is found by idle levels and confirmed by baud | firmware, hardware, uart | high | 2026-11-24 |
| `ir-timeline` | An incident timeline needs three independent clocks | ir, timeline, forensics | medium | 2026-11-24 |
| `ir-memory` | Memory is the most volatile evidence | ir, memory, forensics | medium | 2026-11-24 |
| `linux-suid` | A SUID binary is a path, not a finding | linux, privesc, suid | high | 2026-11-24 |
| `linux-cron-systemd` | Scheduled jobs inherit a weak PATH or writable unit | linux, privesc, cron, systemd | medium | 2026-11-24 |
| `mobile-deep-link-bridge` | A deep link plus a JS bridge is a chain | mobile, android, deep-link | high | 2026-11-24 |
| `mobile-ios-ats` | ATS exceptions are domain-scoped trust decisions | mobile, ios, ats | medium | 2026-11-24 |
| `mobile-provider-paths` | An exported provider with a broad path leaks files | mobile, android, provider | high | 2026-11-24 |
| `mobile-flutter` | Flutter hides logic in libapp.so and pins in Dart | mobile, flutter, dart | medium | 2026-11-24 |
| `report-impact-chain` | A report is a chain a triager can rerun | process, report, impact | high | 2026-11-24 |
| `report-cvss-context` | CVSS without business context misranks the bug | process, report, cvss | medium | 2026-11-24 |
| `cost-job-ledger` | Every job has an actor and a cost | process, cost, jobs | high | 2026-11-24 |
| `report-evidence` | Evidence must be reproducible and redacted | process, report, evidence | high | 2026-11-24 |
| `process-recall-before-research` | Recall before searching | process, memory, research | high | 2026-11-24 |
| `process-scope-parse` | Scope is a list of rules, not a domain | process, scope, recon | high | 2026-11-24 |
| `process-duplicate-search` | Search duplicates before writing a report | process, triage, duplicate | high | 2026-11-24 |
| `re-crash-triage-primitive` | A crash is a lead; the primitive is the finding | re, triage, crash | high | 2026-11-24 |
| `re-ghidrust-vs-ghidra` | GhidRust is a paused Ghidra plugin, not Ghidrust | re, ghidra, rust | high | 2026-11-24 |
| `re-rust-layout` | Rust types are not C types | re, rust, layout | high | 2026-11-24 |
| `supply-lockfile` | A lockfile is an integrity contract | supply-chain, lockfile, reproducible | medium | 2026-11-24 |
| `supply-typosquat` | A package name one character off is a supply-chain bug | supply-chain, package, typosquat | high | 2026-11-24 |
| `secrets-verified` | A secret is a finding only after a read-only proof | supply-chain, secret, verification | high | 2026-11-24 |
| `supply-sigstore` | Signatures are only useful when verified | supply-chain, sigstore, provenance | medium | 2026-11-24 |
| `cicd-pr-target` | pull_request_target can run untrusted code with a write token | supply-chain, ci, github-actions | high | 2026-11-24 |
| `web-race-single-packet` | A race is a check and a write without one lock | web, race, logic | high | 2026-11-24 |
| `race-idempotency` | A unique constraint is the cheapest race fix | web, race, database | medium | 2026-11-24 |
| `web-cors-null-origin` | CORS reflection is only a bug with credentials | web, cors, browser | high | 2026-11-24 |
| `web-csp-bypass` | CSP is bypassed by a trusted script source, not by a weak directive alone | web, csp, xss | high | 2026-11-24 |
| `web-csrf-samesite` | CSRF survives when state changes on a safe method | web, csrf, session | high | 2026-11-24 |
| `web-cache-deception` | Cache deception dresses a private page as a static file | web, cache, deception | medium | 2026-11-24 |
| `web-cache-key-unkeyed-input` | Cache poisoning is an unkeyed input that changes the response | web, cache, cdn | high | 2026-11-24 |
| `web-desync-parser-disagreement` | Desync needs two HTTP parsers and an ambiguous length | web, http, smuggling | high | 2026-11-24 |
| `web-graphql-field-auth` | GraphQL authorization is per field, not per endpoint | web, graphql, api | high | 2026-11-24 |
| `web-http2-downgrade` | HTTP/2 adds a second parser for the same request | web, http2, smuggling | medium | 2026-11-24 |
| `web-idor-owner-check` | IDOR is a missing owner check, not a hidden id | web, idor, access-control | high | 2026-11-24 |
| `web-jwt-signature-trust` | JWT bugs are claim trust, not base64 | web, jwt, identity | high | 2026-11-24 |
| `web-ldap-xpath` | LDAP and XPath injection are filter syntax bugs | web, ldap, xpath, injection | medium | 2026-11-24 |
| `web-deserialization-gadget` | Native deserialization is RCE when a gadget chain exists | web, deserialization, rce | high | 2026-11-24 |
| `web-oauth-redirect-binding` | OAuth redirect matching is prefix logic under pressure | web, oauth, identity | high | 2026-11-24 |
| `web-open-redirect-chain` | Open redirect matters when a token rides the URL | web, redirect, oauth | high | 2026-11-24 |
| `web-host-header-reset` | Password reset trusts the request host | web, host-header, email | high | 2026-11-24 |
| `web-prototype-pollution` | Prototype pollution needs a merge sink and a gadget | web, javascript, prototype | high | 2026-11-24 |
| `web-saml-signature-wrapping` | SAML trusts the assertion, not the signature | web, saml, identity | high | 2026-11-24 |
| `web-sqli-parameterized` | SQL injection is a string-built query at a boundary | web, sqli, database | high | 2026-11-24 |
| `web-ssrf-parser-differential` | SSRF hides in URL parser disagreement | web, ssrf, parser | high | 2026-11-24 |
| `web-traversal-canonical-path` | Traversal is a join before canonicalization | web, file, traversal | high | 2026-11-24 |
| `web-upload-validation` | Upload validation is four separate checks | web, upload, file | high | 2026-11-24 |
| `web-websocket-origin` | WebSocket handshakes skip the same-origin policy | web, websocket, origin | high | 2026-11-24 |
| `web-xss-parser-differential` | XSS survives when two parsers disagree | web, xss, parser | high | 2026-11-24 |
| `web-xxe-parser` | XXE depends on entity expansion and the parser feature set | web, xxe, xml | medium | 2026-11-24 |
| `web-postmessage` | postMessage is a bug when the receiver trusts any origin or sends to any origin | web, postmessage, client-side | high | 2026-11-24 |
| `win-service-acl` | A weak service ACL is local privilege escalation | windows, privesc, service | high | 2026-11-24 |
| `win-credential-stores` | Windows keeps credentials in more than one place | windows, credentials, dpapi | medium | 2026-11-24 |
| `win-token-privileges` | Windows token privileges are the privesc surface | windows, token, privesc | high | 2026-11-24 |
