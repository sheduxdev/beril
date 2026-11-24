# Knowledge gaps

51 gaps. A gap is a card that does not exist yet, ranked by priority.

| # | Domain | Gap | Priority | Source | Status |
|---|---|---|---|---|---|
| 1 | web | CSRF beyond token checks: SameSite, state-changing GET, JSON content type | high | `references/techniques.md` | covered by `web-csrf-samesite` |
| 2 | web | CORS origin reflection, null origin, credentials and preflight cache | high | `references/techniques.md` | covered by `web-cors-null-origin` |
| 3 | web | Host header and password-reset poisoning across proxies | high | `references/techniques.md` | covered by `web-host-header-reset` |
| 4 | web | Open redirect and its use in OAuth and SSO chains | high | `references/techniques.md` | covered by `web-open-redirect-chain` |
| 5 | web | Upload validation: extension, MIME, magic, polyglot, storage path | high | `references/techniques.md` | covered by `web-upload-validation` |
| 6 | web | WebSocket origin checks, token handling and message auth | high | `references/techniques.md` | covered by `web-websocket-origin` |
| 7 | web | Cache deception versus poisoning, extension confusion | medium | `references/techniques.md` | open |
| 8 | web | Prototype pollution sources, merge sinks and gadget paths | high | `references/techniques.md` | covered by `web-prototype-pollution` |
| 9 | web | Python pickle, PHP unserialize, Java streams, .NET formatters | high | `references/techniques.md` | covered by `web-deserialization-gadget` |
| 10 | web | XXE in XML, SAML, DOCX and SVG parsers | medium | `references/techniques.md` | covered by `web-xxe-parser` |
| 11 | web | LDAP and XPath injection syntax and blind variants | medium | `references/techniques.md` | open |
| 12 | api | gRPC reflection, proto exposure, per-method auth | medium | `references/techniques.md` | open |
| 13 | api | Mass assignment through JSON and form binding | high | `references/techniques.md` | covered by `api-mass-assignment` |
| 14 | cloud | IAM wildcard actions, trust policies and privilege escalation paths | high | `references/vulnerability-research.md` | covered by `cloud-iam-wildcard` |
| 15 | cloud | Privileged pods, hostPath, service account tokens and admission bypass | high | `labs/cloud` | covered by `cloud-k8s-hostpath` |
| 16 | cloud | Docker socket, root container, image digest and build secrets | medium | `labs/cloud` | open |
| 17 | cloud | Terraform public resources, state secrets and provider trust | medium | `labs/cloud` | open |
| 18 | supply-chain | Typosquatting, dependency confusion and install scripts | high | `references/vulnerability-research.md` | covered by `supply-typosquat` |
| 19 | supply-chain | Lockfile integrity, registry pinning and reproducible builds | medium | `references/vulnerability-research.md` | open |
| 20 | supply-chain | Signing, provenance and verification of build artifacts | medium | `references/vulnerability-research.md` | open |
| 21 | supply-chain | pull_request_target, workflow permissions and untrusted checkout | high | `labs/cloud` | covered by `cicd-pr-target` |
| 22 | supply-chain | Secret scanning with verification and blast-radius proof | high | `references/tooling.md` | covered by `secrets-verified` |
| 23 | mobile | iOS ATS exceptions and WKWebView bridges | medium | `references/mobile-reverse.md` | open |
| 24 | mobile | Android FileProvider paths and exported providers | high | `labs/mobile` | covered by `mobile-provider-paths` |
| 25 | mobile | Flutter Dart snapshots, SSL pinning and reFlutter | medium | `references/mobile-reverse.md` | open |
| 26 | firmware | UART discovery, baud detection and console access | high | `references/firmware-iot.md` | covered by `firmware-uart` |
| 27 | firmware | JTAG and SWD identification and flash dump | medium | `references/firmware-iot.md` | open |
| 28 | firmware | SPI flash read, verification and recovery | medium | `references/firmware-iot.md` | open |
| 29 | firmware | Update signature, downgrade and rollback | high | `labs/firmware` | covered by `firmware-update-sign` |
| 30 | windows | Service ACL, unquoted path and weak service permissions | high | `references/vulnerability-research.md` | covered by `win-service-acl` |
| 31 | windows | Token privileges, impersonation and potato family | high | `references/vulnerability-research.md` | open |
| 32 | windows | DPAPI, Credential Manager and browser stores | medium | `references/vulnerability-research.md` | open |
| 33 | linux | SUID and capabilities review and GTFOBins paths | high | `references/vulnerability-research.md` | covered by `linux-suid` |
| 34 | linux | Cron, systemd unit and PATH privilege paths | medium | `references/vulnerability-research.md` | open |
| 35 | container | Container escape primitives and host mounts | high | `references/vulnerability-research.md` | open |
| 36 | browser | Extension permissions, content scripts and message passing | medium | `references/vulnerability-research.md` | open |
| 37 | browser | Electron context isolation, preload and nodeIntegration | medium | `references/vulnerability-research.md` | open |
| 38 | detection | Sigma rule structure, logsource and false-positive analysis | high | `labs/detection` | covered by `detection-sigma` |
| 39 | detection | Beaconing detection from flow timing and jitter | medium | `references/techniques.md` | open |
| 40 | ir | Incident timeline from logs, disk and memory | medium | `references/vulnerability-research.md` | open |
| 41 | ir | Memory capture order and volatile evidence | medium | `references/vulnerability-research.md` | open |
| 42 | ai | Agent tool-call confusion and argument injection | high | `labs/llm` | covered by `ai-agent-tool` |
| 43 | ai | Agent memory poisoning and later action | high | `references/techniques.md` | open |
| 44 | ai | MCP server config, tool permissions and prompt injection | high | `references/claude-bughunter.md` | covered by `ai-mcp` |
| 45 | ai | Token budget, loop control and cost caps for agents | medium | `docs/dashboard.md` | open |
| 46 | process | CVSS with business context and severity defense | medium | `references/scoring.md` | covered by `report-cvss` |
| 47 | process | Evidence redaction and chain of custody | high | `references/claude-bughunter.md` | covered by `report-evidence` |
| 48 | crypto | TLS versions, ciphers, certificate chain and pinning | medium | `references/tooling.md` | open |
| 49 | crypto | Key storage, rotation and envelope encryption | medium | `references/vulnerability-research.md` | open |
| 50 | api | Webhook HMAC, timestamp and replay | high | `references/techniques.md` | open |
| 51 | web | Database isolation, unique constraints and idempotency keys | medium | `references/techniques.md` | open |

Close a gap with `./beril remember add`, then `./beril gaps --cover <gap> --card <id>`.
