# Knowledge gaps

81 gaps. A gap is a card that does not exist yet, ranked by priority.

| # | Domain | Gap | Priority | Source | Status |
|---|---|---|---|---|---|
| 1 | web | CSRF beyond token checks: SameSite, state-changing GET, JSON content type | high | `references/techniques.md` | covered by `web-csrf-samesite` |
| 2 | web | CORS origin reflection, null origin, credentials and preflight cache | high | `references/techniques.md` | covered by `web-cors-null-origin` |
| 3 | web | Host header and password-reset poisoning across proxies | high | `references/techniques.md` | covered by `web-host-header-reset` |
| 4 | web | Open redirect and its use in OAuth and SSO chains | high | `references/techniques.md` | covered by `web-open-redirect-chain` |
| 5 | web | Upload validation: extension, MIME, magic, polyglot, storage path | high | `references/techniques.md` | covered by `web-upload-validation` |
| 6 | web | WebSocket origin checks, token handling and message auth | high | `references/techniques.md` | covered by `web-websocket-origin` |
| 7 | web | Cache deception versus poisoning, extension confusion | medium | `references/techniques.md` | covered by `web-cache-deception` |
| 8 | web | Prototype pollution sources, merge sinks and gadget paths | high | `references/techniques.md` | covered by `web-prototype-pollution` |
| 9 | web | Python pickle, PHP unserialize, Java streams, .NET formatters | high | `references/techniques.md` | covered by `web-deserialization-gadget` |
| 10 | web | XXE in XML, SAML, DOCX and SVG parsers | medium | `references/techniques.md` | covered by `web-xxe-parser` |
| 11 | web | LDAP and XPath injection syntax and blind variants | medium | `references/techniques.md` | covered by `web-ldap-xpath` |
| 12 | api | gRPC reflection, proto exposure, per-method auth | medium | `references/techniques.md` | covered by `api-grpc` |
| 13 | api | Mass assignment through JSON and form binding | high | `references/techniques.md` | covered by `api-mass-assignment` |
| 14 | cloud | IAM wildcard actions, trust policies and privilege escalation paths | high | `references/vulnerability-research.md` | covered by `cloud-iam-wildcard` |
| 15 | cloud | Privileged pods, hostPath, service account tokens and admission bypass | high | `labs/cloud` | covered by `cloud-k8s-hostpath` |
| 16 | cloud | Docker socket, root container, image digest and build secrets | medium | `labs/cloud` | covered by `cloud-docker` |
| 17 | cloud | Terraform public resources, state secrets and provider trust | medium | `labs/cloud` | covered by `cloud-terraform` |
| 18 | supply-chain | Typosquatting, dependency confusion and install scripts | high | `references/vulnerability-research.md` | covered by `supply-typosquat` |
| 19 | supply-chain | Lockfile integrity, registry pinning and reproducible builds | medium | `references/vulnerability-research.md` | covered by `supply-lockfile` |
| 20 | supply-chain | Signing, provenance and verification of build artifacts | medium | `references/vulnerability-research.md` | covered by `supply-sigstore` |
| 21 | supply-chain | pull_request_target, workflow permissions and untrusted checkout | high | `labs/cloud` | covered by `cicd-pr-target` |
| 22 | supply-chain | Secret scanning with verification and blast-radius proof | high | `references/tooling.md` | covered by `secrets-verified` |
| 23 | mobile | iOS ATS exceptions and WKWebView bridges | medium | `references/mobile-reverse.md` | covered by `mobile-ios-ats` |
| 24 | mobile | Android FileProvider paths and exported providers | high | `labs/mobile` | covered by `mobile-provider-paths` |
| 25 | mobile | Flutter Dart snapshots, SSL pinning and reFlutter | medium | `references/mobile-reverse.md` | covered by `mobile-flutter` |
| 26 | firmware | UART discovery, baud detection and console access | high | `references/firmware-iot.md` | covered by `firmware-uart` |
| 27 | firmware | JTAG and SWD identification and flash dump | medium | `references/firmware-iot.md` | covered by `firmware-jtag` |
| 28 | firmware | SPI flash read, verification and recovery | medium | `references/firmware-iot.md` | covered by `firmware-spi` |
| 29 | firmware | Update signature, downgrade and rollback | high | `labs/firmware` | covered by `firmware-update-sign` |
| 30 | windows | Service ACL, unquoted path and weak service permissions | high | `references/vulnerability-research.md` | covered by `win-service-acl` |
| 31 | windows | Token privileges, impersonation and potato family | high | `references/vulnerability-research.md` | covered by `win-token` |
| 32 | windows | DPAPI, Credential Manager and browser stores | medium | `references/vulnerability-research.md` | covered by `win-credential` |
| 33 | linux | SUID and capabilities review and GTFOBins paths | high | `references/vulnerability-research.md` | covered by `linux-suid` |
| 34 | linux | Cron, systemd unit and PATH privilege paths | medium | `references/vulnerability-research.md` | covered by `linux-cron-systemd` |
| 35 | container | Container escape primitives and host mounts | high | `references/vulnerability-research.md` | covered by `container-escape` |
| 36 | browser | Extension permissions, content scripts and message passing | medium | `references/vulnerability-research.md` | covered by `browser-extension` |
| 37 | browser | Electron context isolation, preload and nodeIntegration | medium | `references/vulnerability-research.md` | covered by `electron-context` |
| 38 | detection | Sigma rule structure, logsource and false-positive analysis | high | `labs/detection` | covered by `detection-sigma` |
| 39 | detection | Beaconing detection from flow timing and jitter | medium | `references/techniques.md` | covered by `detection-beacon` |
| 40 | ir | Incident timeline from logs, disk and memory | medium | `references/vulnerability-research.md` | covered by `ir-timeline` |
| 41 | ir | Memory capture order and volatile evidence | medium | `references/vulnerability-research.md` | covered by `ir-memory` |
| 42 | ai | Agent tool-call confusion and argument injection | high | `labs/llm` | covered by `ai-agent-tool` |
| 43 | ai | Agent memory poisoning and later action | high | `references/techniques.md` | covered by `ai-memory-poison` |
| 44 | ai | MCP server config, tool permissions and prompt injection | high | `references/claude-bughunter.md` | covered by `ai-mcp` |
| 45 | ai | Token budget, loop control and cost caps for agents | medium | `docs/dashboard.md` | covered by `ai-cost` |
| 46 | process | CVSS with business context and severity defense | medium | `references/scoring.md` | covered by `report-cvss` |
| 47 | process | Evidence redaction and chain of custody | high | `references/claude-bughunter.md` | covered by `report-evidence` |
| 48 | crypto | TLS versions, ciphers, certificate chain and pinning | medium | `references/tooling.md` | covered by `tls-config` |
| 49 | crypto | Key storage, rotation and envelope encryption | medium | `references/vulnerability-research.md` | covered by `key-management` |
| 50 | api | Webhook HMAC, timestamp and replay | high | `references/techniques.md` | covered by `api-webhook-signature` |
| 51 | web | Database isolation, unique constraints and idempotency keys | medium | `references/techniques.md` | covered by `race-db` |
| 52 | web | CSP bypass: JSONP, base-uri, script gadgets and nonce reuse | high | `references/techniques.md` | covered by `web-csp-bypass` |
| 53 | web | DOM clobbering and named element collisions | medium | `references/techniques.md` | open |
| 54 | web | postMessage origin and target origin checks | high | `references/techniques.md` | covered by `web-postmessage` |
| 55 | web | HTTP/2 pseudo-header, HPACK and downgrade behavior | high | `references/techniques.md` | covered by `web-http2` |
| 56 | web | JSONP and callback injection | medium | `references/techniques.md` | open |
| 57 | web | Client-side path traversal in routers and file pickers | medium | `references/techniques.md` | open |
| 58 | api | OAuth device code flow and code phishing | medium | `references/techniques.md` | open |
| 59 | api | Server-sent events auth, replay and cross-user leakage | medium | `references/techniques.md` | open |
| 60 | api | Rate limit keying and bypass through identity, IP and route | high | `references/techniques.md` | covered by `api-rate-limit` |
| 61 | cloud | Azure AD, managed identity and role assignment paths | high | `references/vulnerability-research.md` | covered by `cloud-azure` |
| 62 | cloud | GCP service accounts, workload identity and bucket IAM | high | `references/vulnerability-research.md` | covered by `cloud-gcp` |
| 63 | cloud | Lambda and Cloud Functions event injection and role scope | medium | `references/vulnerability-research.md` | open |
| 64 | cloud | EKS IRSA, aws-auth and node role paths | medium | `references/vulnerability-research.md` | open |
| 65 | binary | Kernel drivers, IOCTL buffers and object lifetime | high | `references/reverse-engineering.md` | covered by `binary-kernel` |
| 66 | binary | Browser exploitation: JIT, GC and renderer sandbox | high | `references/exploit-development.md` | covered by `binary-browser` |
| 67 | binary | JIT spraying, RWX pages and code generation bugs | medium | `references/exploit-development.md` | open |
| 68 | re | Go symbols, pclntab, goroutines and interface calls | medium | `references/reverse-engineering.md` | open |
| 69 | re | .NET Native AOT metadata and method recovery | medium | `references/reverse-engineering.md` | open |
| 70 | re | Swift mangling, witness tables and value types | medium | `references/reverse-engineering.md` | open |
| 71 | ai | Model extraction and membership inference | medium | `references/techniques.md` | open |
| 72 | ai | Training and RAG data poisoning | high | `references/techniques.md` | covered by `ai-data-poison` |
| 73 | ai | Embedding inversion and vector store access | medium | `references/techniques.md` | open |
| 74 | detection | EDR telemetry and process tree detection | medium | `labs/detection` | open |
| 75 | ir | Disk artifacts: MFT, USN, registry and prefetch | medium | `references/vulnerability-research.md` | open |
| 76 | process | Duplicate search before writing a report | high | `references/claude-bughunter.md` | covered by `process-duplicate` |
| 77 | process | Scope parsing and out-of-scope asset checks | high | `docs/break-my-app.md` | covered by `process-scope` |
| 78 | crypto | Weak randomness, predictability and seed reuse | high | `references/vulnerability-research.md` | covered by `crypto-random` |
| 79 | mobile | Swift runtime, Objective-C bridging and Swift hooks | medium | `references/mobile-reverse.md` | open |
| 80 | firmware | BLE, Zigbee and sub-GHz capture and replay | medium | `references/firmware-iot.md` | open |
| 81 | hardware | Power, timing and EM side channels | low | `references/firmware-iot.md` | open |

Close a gap with `./beril remember add`, then `./beril gaps --cover <gap> --card <id>`.
