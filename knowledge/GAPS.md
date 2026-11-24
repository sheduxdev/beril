# Knowledge gaps

266 gaps. A gap is a card that does not exist yet, ranked by priority.

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
| 53 | web | DOM clobbering and named element collisions | medium | `references/techniques.md` | covered by `web-dom-clobbering` |
| 54 | web | postMessage origin and target origin checks | high | `references/techniques.md` | covered by `web-postmessage` |
| 55 | web | HTTP/2 pseudo-header, HPACK and downgrade behavior | high | `references/techniques.md` | covered by `web-http2` |
| 56 | web | JSONP and callback injection | medium | `references/techniques.md` | covered by `web-jsonp` |
| 57 | web | Client-side path traversal in routers and file pickers | medium | `references/techniques.md` | covered by `web-client-path` |
| 58 | api | OAuth device code flow and code phishing | medium | `references/techniques.md` | covered by `api-oauth-device` |
| 59 | api | Server-sent events auth, replay and cross-user leakage | medium | `references/techniques.md` | covered by `api-sse` |
| 60 | api | Rate limit keying and bypass through identity, IP and route | high | `references/techniques.md` | covered by `api-rate-limit` |
| 61 | cloud | Azure AD, managed identity and role assignment paths | high | `references/vulnerability-research.md` | covered by `cloud-azure` |
| 62 | cloud | GCP service accounts, workload identity and bucket IAM | high | `references/vulnerability-research.md` | covered by `cloud-gcp` |
| 63 | cloud | Lambda and Cloud Functions event injection and role scope | medium | `references/vulnerability-research.md` | covered by `cloud-serverless` |
| 64 | cloud | EKS IRSA, aws-auth and node role paths | medium | `references/vulnerability-research.md` | covered by `cloud-eks` |
| 65 | binary | Kernel drivers, IOCTL buffers and object lifetime | high | `references/reverse-engineering.md` | covered by `binary-kernel` |
| 66 | binary | Browser exploitation: JIT, GC and renderer sandbox | high | `references/exploit-development.md` | covered by `binary-browser` |
| 67 | binary | JIT spraying, RWX pages and code generation bugs | medium | `references/exploit-development.md` | covered by `binary-jit` |
| 68 | re | Go symbols, pclntab, goroutines and interface calls | medium | `references/reverse-engineering.md` | covered by `re-go` |
| 69 | re | .NET Native AOT metadata and method recovery | medium | `references/reverse-engineering.md` | covered by `re-dotnet-aot` |
| 70 | re | Swift mangling, witness tables and value types | medium | `references/reverse-engineering.md` | covered by `re-swift` |
| 71 | ai | Model extraction and membership inference | medium | `references/techniques.md` | covered by `ai-model-extraction` |
| 72 | ai | Training and RAG data poisoning | high | `references/techniques.md` | covered by `ai-data-poison` |
| 73 | ai | Embedding inversion and vector store access | medium | `references/techniques.md` | covered by `ai-embedding` |
| 74 | detection | EDR telemetry and process tree detection | medium | `labs/detection` | covered by `detection-edr` |
| 75 | ir | Disk artifacts: MFT, USN, registry and prefetch | medium | `references/vulnerability-research.md` | covered by `ir-disk` |
| 76 | process | Duplicate search before writing a report | high | `references/claude-bughunter.md` | covered by `process-duplicate` |
| 77 | process | Scope parsing and out-of-scope asset checks | high | `docs/break-my-app.md` | covered by `process-scope` |
| 78 | crypto | Weak randomness, predictability and seed reuse | high | `references/vulnerability-research.md` | covered by `crypto-random` |
| 79 | mobile | Swift runtime, Objective-C bridging and Swift hooks | medium | `references/mobile-reverse.md` | covered by `mobile-swift` |
| 80 | firmware | BLE, Zigbee and sub-GHz capture and replay | medium | `references/firmware-iot.md` | covered by `firmware-radio` |
| 81 | hardware | Power, timing and EM side channels | low | `references/firmware-iot.md` | covered by `hardware-sidechannel` |
| 82 | ai | Agent goal drift, subagent permissions and plan hijack | high | `references/techniques.md` | covered by `ai-agent-planning` |
| 83 | ai | Code interpreter and tool sandbox escape | high | `labs/llm` | covered by `ai-sandbox-escape` |
| 84 | ai | Vector store authorization and metadata filtering | medium | `references/techniques.md` | covered by `ai-vector-auth` |
| 85 | api | Idempotency keys, retries and duplicate side effects | high | `references/techniques.md` | covered by `api-idempotency` |
| 86 | cloud | AKS workload identity and Azure RBAC | medium | `references/vulnerability-research.md` | covered by `cloud-aks` |
| 87 | cloud | OCI compartments, instance principals and policy | low | `references/vulnerability-research.md` | covered by `cloud-oci` |
| 88 | binary | UEFI DXE drivers, SMM and secure boot | medium | `references/reverse-engineering.md` | covered by `binary-uefi` |
| 89 | binary | Hypervisor interfaces, VTL and synthetic MSRs | low | `references/reverse-engineering.md` | covered by `binary-hypervisor` |
| 90 | re | JVM bytecode, JIT and deserialization gadgets | medium | `references/reverse-engineering.md` | covered by `re-jvm` |
| 91 | mobile | SwiftUI state, deep links and scene lifecycle | low | `references/mobile-reverse.md` | covered by `mobile-swiftui` |
| 92 | firmware | Secure boot chain, key enrollment and rollback | high | `references/firmware-iot.md` | covered by `firmware-secureboot` |
| 93 | detection | IOC versus behavior, intel aging and false positives | medium | `labs/detection` | covered by `detection-threatintel` |
| 94 | ir | CloudTrail and audit log timeline reconstruction | medium | `references/vulnerability-research.md` | covered by `ir-cloud` |
| 95 | process | Coordinated disclosure, timelines and vendor silence | medium | `references/claude-bughunter.md` | covered by `process-disclosure` |
| 96 | crypto | Post-quantum migration and hybrid key exchange | low | `references/vulnerability-research.md` | covered by `crypto-postquantum` |
| 97 | api | OpenAPI and Swagger exposure and schema abuse | high | `references/techniques.md` | covered by `api-openapi` |
| 98 | api | JWT key rotation, kid and JWKS cache poisoning | high | `references/techniques.md` | covered by `api-jwt-rotation` |
| 99 | api | Cursor and offset pagination leaks and total-count oracles | medium | `references/techniques.md` | covered by `api-pagination` |
| 100 | api | Shadow and deprecated API versions | high | `references/techniques.md` | covered by `api-versioning` |
| 101 | cloud | Secrets manager policy, rotation and cross-account access | high | `references/vulnerability-research.md` | covered by `cloud-secrets` |
| 102 | cloud | CI OIDC trust policy and subject claim confusion | high | `references/vulnerability-research.md` | covered by `cloud-oidc-ci` |
| 103 | cloud | Alibaba Cloud RAM roles and STS | low | `references/vulnerability-research.md` | covered by `cloud-alibaba` |
| 104 | binary | Mach-O, dyld and code signing on macOS | medium | `references/reverse-engineering.md` | covered by `binary-macos` |
| 105 | re | Mach-O load commands, entitlements and universal binaries | medium | `references/reverse-engineering.md` | covered by `re-macho` |
| 106 | re | AArch64 calling convention, PAC and MTE | medium | `references/reverse-engineering.md` | covered by `re-arm64` |
| 107 | detection | DNS tunneling and unusual query patterns | medium | `labs/detection` | covered by `detection-dns` |
| 108 | detection | Living-off-the-land binaries and parent-child anomalies | high | `labs/detection` | covered by `detection-lolbins` |
| 109 | detection | JA3/JA4 and TLS fingerprint anomalies | medium | `references/techniques.md` | covered by `detection-tls` |
| 110 | ir | Mobile incident triage: backups, sysdiagnose and Frida | low | `references/mobile-reverse.md` | covered by `ir-mobile` |
| 111 | ir | Container incident triage and image diffing | medium | `references/vulnerability-research.md` | covered by `ir-container` |
| 112 | ai | Tool output trust and second-order injection | high | `references/techniques.md` | covered by `ai-tool-output` |
| 113 | ai | Guardrail bypass through encoding, length and language | medium | `references/techniques.md` | covered by `ai-guardrail` |
| 114 | process | Program rules, payout terms and disclosure policy | medium | `references/claude-bughunter.md` | covered by `process-bounty-platform` |
| 115 | process | Retest after a fix and regression notes | high | `docs/break-my-app.md` | covered by `process-retest` |
| 116 | crypto | Password KDF choice, cost and salt handling | medium | `references/vulnerability-research.md` | covered by `crypto-kdf` |
| 117 | web | Clickjacking, frame-ancestors and UI redress | high | `references/techniques.md` | covered by `web-clickjacking` |
| 118 | web | CSS injection, attribute selectors and data exfiltration | medium | `references/techniques.md` | covered by `web-css-injection` |
| 119 | web | Dangling markup and CSRF token exfiltration | medium | `references/techniques.md` | covered by `web-dangling-markup` |
| 120 | web3 | Solidity reentrancy, access control and oracle bugs | high | `references/techniques.md` | covered by `web3-contract` |
| 121 | api | WebSocket message auth, subscriptions and cross-user channels | high | `references/techniques.md` | covered by `api-websocket-auth` |
| 122 | api | Batch endpoints, partial failures and authorization per item | medium | `references/techniques.md` | covered by `api-batch` |
| 123 | cloud | vCenter SSO, ESXi and appliance chains | high | `references/vulnerability-research.md` | covered by `cloud-vmware` |
| 124 | cloud | OpenStack keystone, nova metadata and policy | low | `references/vulnerability-research.md` | covered by `cloud-openstack` |
| 125 | cloud | Istio and Envoy mTLS, authorization policy and sidecar bypass | medium | `references/vulnerability-research.md` | covered by `cloud-service-mesh` |
| 126 | binary | Windows kernel drivers, IOCTL and object manager | high | `references/reverse-engineering.md` | covered by `binary-windows-kernel` |
| 127 | binary | WebAssembly validation, JIT and sandbox boundaries | medium | `references/reverse-engineering.md` | covered by `binary-wasm` |
| 128 | binary | eBPF verifier, maps and helper abuse | low | `references/reverse-engineering.md` | covered by `binary-ebpf` |
| 129 | re | C++ RTTI, vtables and multiple inheritance | medium | `references/reverse-engineering.md` | covered by `re-cpp-rtti` |
| 130 | re | Android JNI, ART and native library analysis | medium | `references/mobile-reverse.md` | covered by `re-android-native` |
| 131 | detection | Identity logs, impossible travel and token anomalies | high | `labs/detection` | covered by `detection-identity` |
| 132 | detection | Cloud control-plane detections and role assumptions | high | `labs/detection` | covered by `detection-cloud` |
| 133 | ir | Ransomware triage, note, encryption and backups | high | `references/vulnerability-research.md` | covered by `ir-ransomware` |
| 134 | ir | Phishing triage, headers, URLs and payloads | medium | `references/vulnerability-research.md` | covered by `ir-phishing` |
| 135 | ai | Multi-agent delegation, shared memory and trust | high | `references/techniques.md` | covered by `ai-multiagent` |
| 136 | process | Safe harbor, authorization and data handling | medium | `docs/break-my-app.md` | covered by `process-legal` |
| 137 | process | Payout expectations, VRT and severity negotiation | medium | `references/scoring.md` | covered by `report-pricing` |
| 138 | engineering | Consensus, quorum and leader election | high | `references/engineering-mastery.md` | covered by `eng-consensus` |
| 139 | engineering | Consistency models and read-your-writes | high | `references/engineering-mastery.md` | covered by `eng-consistency` |
| 140 | engineering | B-tree, LSM and write amplification | medium | `references/engineering-mastery.md` | covered by `eng-storage` |
| 141 | engineering | Query planning, indexes and statistics | high | `references/engineering-mastery.md` | covered by `eng-query-planner` |
| 142 | engineering | Virtual memory, page cache and allocators | medium | `references/engineering-mastery.md` | covered by `eng-memory` |
| 143 | engineering | Congestion control, queues and bufferbloat | medium | `references/engineering-mastery.md` | covered by `eng-congestion` |
| 144 | engineering | Type systems, variance and exhaustiveness | medium | `references/engineering-mastery.md` | covered by `eng-type-systems` |
| 145 | engineering | Feature stores, training serving skew and evaluation | high | `references/engineering-mastery.md` | covered by `eng-ml-systems` |
| 146 | engineering | SLOs, error budgets and alerting | high | `references/engineering-mastery.md` | covered by `eng-slo` |
| 147 | engineering | Tenant isolation, noisy neighbors and data partitioning | high | `references/engineering-mastery.md` | covered by `eng-multi-tenancy` |
| 148 | engineering | Event sourcing, replay and projections | medium | `references/engineering-mastery.md` | covered by `eng-event-sourcing` |
| 149 | engineering | CQRS and read model consistency | medium | `references/engineering-mastery.md` | covered by `eng-cqrs` |
| 150 | engineering | Sagas, outbox and compensation | high | `references/engineering-mastery.md` | covered by `eng-distributed-tx` |
| 151 | engineering | At-least-once delivery and idempotent consumers | high | `references/engineering-mastery.md` | covered by `eng-idempotent-consumer` |
| 152 | engineering | Token bucket, leaky bucket and fairness | medium | `references/engineering-mastery.md` | covered by `eng-rate-limit` |
| 153 | engineering | Cache-aside, write-through and stampede | medium | `references/engineering-mastery.md` | covered by `eng-cache-topology` |
| 154 | engineering | Backward and forward compatible schema changes | high | `references/engineering-mastery.md` | covered by `eng-schema-evolution` |
| 155 | engineering | API versioning and deprecation | medium | `references/engineering-mastery.md` | covered by `eng-api-versioning` |
| 156 | engineering | Platform teams, golden paths and paved roads | medium | `references/engineering-mastery.md` | covered by `eng-platform` |
| 157 | engineering | Team boundaries and ownership | medium | `references/engineering-mastery.md` | covered by `eng-team-topology` |
| 158 | engineering | Roadmaps, bets and kill criteria | medium | `references/engineering-mastery.md` | covered by `eng-roadmap` |
| 159 | engineering | Hiring signals and interview design | low | `references/engineering-mastery.md` | covered by `eng-hiring` |
| 160 | engineering | Privacy by design and data minimization | high | `references/engineering-mastery.md` | covered by `eng-privacy` |
| 161 | engineering | SOC2, GDPR and evidence collection | medium | `references/engineering-mastery.md` | covered by `eng-compliance` |
| 162 | engineering | Unit economics and cost allocation | medium | `references/engineering-mastery.md` | covered by `eng-finops` |
| 163 | engineering | Client state, server state and cache ownership | medium | `references/engineering-mastery.md` | covered by `eng-frontend-state` |
| 164 | engineering | Offline-first mobile architecture | medium | `references/engineering-mastery.md` | covered by `eng-mobile-arch` |
| 165 | engineering | Lexing, parsing, IR and optimization | low | `references/engineering-mastery.md` | covered by `eng-compiler` |
| 166 | engineering | Garbage collection and allocation pressure | medium | `references/engineering-mastery.md` | covered by `eng-gc` |
| 167 | engineering | Cardinality, sampling and telemetry cost | medium | `references/engineering-mastery.md` | covered by `eng-observability-cost` |
| 168 | distributed | Network partitions and split-brain behavior | high | `references/engineering-mastery.md` | covered by `dist-partition` |
| 169 | distributed | Clock skew, logical clocks and causality | high | `references/engineering-mastery.md` | covered by `dist-clock` |
| 170 | distributed | CRDTs and conflict-free merge | high | `references/engineering-mastery.md` | covered by `dist-crdt` |
| 171 | distributed | Gossip membership and failure detection | medium | `references/engineering-mastery.md` | covered by `dist-gossip` |
| 172 | distributed | Message ordering, dedup and exactly-once myth | high | `references/engineering-mastery.md` | covered by `dist-ordering` |
| 173 | distributed | Safe backfills and read repair | medium | `references/engineering-mastery.md` | covered by `dist-backfill` |
| 174 | distributed | Quorum reads, sticky reads and monotonicity | medium | `references/engineering-mastery.md` | covered by `dist-quorum-read` |
| 175 | compilers | SSA form, phi nodes and dataflow | high | `references/engineering-mastery.md` | covered by `comp-ssa` |
| 176 | compilers | Register allocation and spilling | medium | `references/engineering-mastery.md` | covered by `comp-regalloc` |
| 177 | compilers | JIT tiers, deopt and code cache | high | `references/engineering-mastery.md` | covered by `comp-jit` |
| 178 | compilers | Type checking, inference and soundness | medium | `references/engineering-mastery.md` | covered by `comp-type-check` |
| 179 | compilers | Optimization passes and semantic preservation | medium | `references/engineering-mastery.md` | covered by `comp-optimizer` |
| 180 | storage | Write-ahead log, fsync and crash consistency | high | `references/engineering-mastery.md` | covered by `storage-wal` |
| 181 | storage | Compaction policy, tombstones and write stalls | medium | `references/engineering-mastery.md` | covered by `storage-compaction` |
| 182 | storage | Checksums, bit rot and scrub | medium | `references/engineering-mastery.md` | covered by `storage-checksum` |
| 183 | storage | Replication lag, failover and data loss windows | high | `references/engineering-mastery.md` | covered by `storage-replication` |
| 184 | organization | Conway's law and service ownership | high | `references/engineering-mastery.md` | covered by `org-conway` |
| 185 | organization | On-call load, escalation and handoff | high | `references/engineering-mastery.md` | covered by `org-oncall` |
| 186 | organization | Delegation, decision rights and DACI | medium | `references/engineering-mastery.md` | covered by `org-delegation` |
| 187 | organization | Architecture decision records and durable context | medium | `references/engineering-mastery.md` | covered by `org-adr` |
| 188 | organization | Headcount, maintenance and innovation budget | medium | `references/engineering-mastery.md` | covered by `org-budget` |
| 189 | organization | Incentives, metrics and local optimization | medium | `references/engineering-mastery.md` | covered by `org-incentives` |
| 190 | engineering | Backup, restore and the untested backup | high | `references/engineering-mastery.md` | covered by `eng-backup-restore` |
| 191 | engineering | RTO, RPO and disaster exercises | high | `references/engineering-mastery.md` | covered by `eng-disaster-recovery` |
| 192 | engineering | Chaos experiments and steady-state hypothesis | medium | `references/engineering-mastery.md` | covered by `eng-chaos` |
| 193 | engineering | Load models, open vs closed loop and saturation | medium | `references/engineering-mastery.md` | covered by `eng-load-test` |
| 194 | engineering | Capacity models and headroom | medium | `references/engineering-mastery.md` | covered by `eng-capacity` |
| 195 | engineering | Data retention, archival and deletion | medium | `references/engineering-mastery.md` | covered by `eng-retention` |
| 196 | distributed | Raft membership changes and joint consensus | high | `references/engineering-mastery.md` | covered by `consensus-membership` |
| 197 | distributed | Log snapshots and install-snapshot safety | medium | `references/engineering-mastery.md` | covered by `consensus-snapshot` |
| 198 | distributed | Paxos phases and multi-Paxos | medium | `references/engineering-mastery.md` | covered by `consensus-paxos` |
| 199 | distributed | Linearizable reads without a log write | high | `references/engineering-mastery.md` | covered by `consensus-linearizable-read` |
| 200 | compilers | Instruction selection and pattern matching | high | `references/engineering-mastery.md` | covered by `comp-instr-select` |
| 201 | compilers | ABI, calling conventions and stack layout | high | `references/engineering-mastery.md` | covered by `comp-abi` |
| 202 | compilers | Linking, relocation and symbol resolution | medium | `references/engineering-mastery.md` | covered by `comp-linking` |
| 203 | compilers | DWARF, source maps and optimized code | medium | `references/engineering-mastery.md` | covered by `comp-debug-info` |
| 204 | compilers | Undefined behavior and optimizer assumptions | high | `references/engineering-mastery.md` | covered by `comp-ub` |
| 205 | database | MVCC versions, snapshots and visibility | high | `references/engineering-mastery.md` | covered by `db-mvcc` |
| 206 | database | Vacuum, bloat and transaction id wraparound | medium | `references/engineering-mastery.md` | covered by `db-vacuum` |
| 207 | database | Isolation levels and write skew | high | `references/engineering-mastery.md` | covered by `db-isolation` |
| 208 | database | Lock modes, wait queues and fairness | medium | `references/engineering-mastery.md` | covered by `db-lock-manager` |
| 209 | database | Deadlock detection and retry policy | medium | `references/engineering-mastery.md` | covered by `db-deadlock` |
| 210 | organization | Platform team API and internal SLA | high | `references/engineering-mastery.md` | covered by `platform-team-api` |
| 211 | organization | Internal pricing, chargeback and showback | medium | `references/engineering-mastery.md` | covered by `platform-pricing` |
| 212 | organization | Platform support and office hours | medium | `references/engineering-mastery.md` | covered by `platform-support` |
| 213 | organization | On-call compensation and time off | high | `references/engineering-mastery.md` | covered by `org-oncall-comp` |
| 214 | organization | Rotation length, handoff and shadowing | medium | `references/engineering-mastery.md` | covered by `org-rotation` |
| 215 | organization | Skill matrix and bus factor | medium | `references/engineering-mastery.md` | covered by `org-skill-matrix` |
| 216 | organization | Writing culture and decision visibility | medium | `references/engineering-mastery.md` | covered by `org-docs-culture` |
| 217 | organization | Blameless postmortems and learning loops | high | `references/engineering-mastery.md` | covered by `org-postmortem-culture` |
| 218 | distributed | Crash recovery, log replay and commit index | high | `references/engineering-mastery.md` | covered by `consensus-crash-recovery` |
| 219 | distributed | Log compaction and snapshot retention | medium | `references/engineering-mastery.md` | covered by `consensus-log-compaction` |
| 220 | distributed | Witness replicas and quorum cost | low | `references/engineering-mastery.md` | covered by `consensus-witness` |
| 221 | distributed | Pre-vote and disruptive server rejoin | high | `references/engineering-mastery.md` | covered by `consensus-pre-vote` |
| 222 | distributed | Byzantine faults and BFT quorum | low | `references/engineering-mastery.md` | covered by `consensus-bft` |
| 223 | allocator | Size classes, rounding and internal fragmentation | medium | `references/engineering-mastery.md` | covered by `alloc-size-class` |
| 224 | allocator | External fragmentation and compaction | high | `references/engineering-mastery.md` | covered by `alloc-fragmentation` |
| 225 | allocator | Arena and region allocation | medium | `references/engineering-mastery.md` | covered by `alloc-arena` |
| 226 | allocator | Thread caches, remote free and false sharing | high | `references/engineering-mastery.md` | covered by `alloc-tcache` |
| 227 | allocator | NUMA locality and first-touch policy | medium | `references/engineering-mastery.md` | covered by `alloc-numa` |
| 228 | database | Nested loop, hash and merge join cost | high | `references/engineering-mastery.md` | covered by `db-join-algorithms` |
| 229 | database | Vectorized execution and batch size | medium | `references/engineering-mastery.md` | covered by `db-vectorized-exec` |
| 230 | database | Parallel plans, skew and worker limits | medium | `references/engineering-mastery.md` | covered by `db-parallel-query` |
| 231 | database | External sort, spill files and memory limits | medium | `references/engineering-mastery.md` | covered by `db-spill-sort` |
| 232 | database | Cardinality estimates, histograms and bad plans | high | `references/engineering-mastery.md` | covered by `db-cardinality-estimate` |
| 233 | economics | Build versus buy with maintenance cost | high | `references/engineering-mastery.md` | covered by `econ-make-buy` |
| 234 | economics | Total cost of ownership and hidden cost | high | `references/engineering-mastery.md` | covered by `econ-total-cost` |
| 235 | economics | Opportunity cost and the next best use | medium | `references/engineering-mastery.md` | covered by `econ-opportunity` |
| 236 | economics | Technical debt interest and repayment | high | `references/engineering-mastery.md` | covered by `econ-debt-interest` |
| 237 | economics | Pricing, margin and unit economics | medium | `references/engineering-mastery.md` | covered by `econ-pricing` |
| 238 | economics | Headcount cost and ramp time | medium | `references/engineering-mastery.md` | covered by `econ-headcount` |
| 239 | economics | Vendor lock-in and exit cost | high | `references/engineering-mastery.md` | covered by `econ-vendor-lock` |
| 240 | economics | Sunk cost and kill decisions | medium | `references/engineering-mastery.md` | covered by `econ-sunk-cost` |
| 241 | economics | Risk-adjusted return and expected value | medium | `references/engineering-mastery.md` | covered by `econ-risk-adjusted` |
| 242 | formal | Invariants, preconditions and postconditions | high | `references/engineering-mastery.md` | covered by `formal-invariant` |
| 243 | formal | Model checking and state explosion | high | `references/engineering-mastery.md` | covered by `formal-model-check` |
| 244 | formal | TLA+ specs for concurrent protocols | high | `references/engineering-mastery.md` | covered by `formal-tla` |
| 245 | formal | Refinement from spec to implementation | medium | `references/engineering-mastery.md` | open |
| 246 | formal | Design by contract and runtime checks | medium | `references/engineering-mastery.md` | open |
| 247 | formal | Proof assistants and cost | low | `references/engineering-mastery.md` | open |
| 248 | os | Scheduler classes, priority and starvation | high | `references/engineering-mastery.md` | covered by `os-scheduler` |
| 249 | os | Virtual memory, page tables and TLB | medium | `references/engineering-mastery.md` | open |
| 250 | os | Page faults, demand paging and minor/major cost | high | `references/engineering-mastery.md` | covered by `os-page-fault` |
| 251 | os | Syscall ABI, errno and seccomp | medium | `references/engineering-mastery.md` | open |
| 252 | os | Signals, async safety and restart | medium | `references/engineering-mastery.md` | open |
| 253 | os | cgroups v2, limits and OOM | medium | `references/engineering-mastery.md` | open |
| 254 | os | Namespaces, mounts and isolation | medium | `references/engineering-mastery.md` | open |
| 255 | protocol | Framing, length prefixes and desync | high | `references/engineering-mastery.md` | covered by `proto-framing` |
| 256 | protocol | Protocol state machines and illegal transitions | high | `references/engineering-mastery.md` | covered by `proto-state-machine` |
| 257 | protocol | Version negotiation and downgrade | high | `references/engineering-mastery.md` | covered by `proto-versioning` |
| 258 | protocol | Flow control and window management | medium | `references/engineering-mastery.md` | open |
| 259 | protocol | Message ids, retries and duplicate suppression | medium | `references/engineering-mastery.md` | open |
| 260 | protocol | Handshake, transcript binding and replay | high | `references/engineering-mastery.md` | covered by `proto-security` |
| 261 | hci | Fitts's law and target placement | medium | `references/engineering-mastery.md` | open |
| 262 | hci | Error prevention, undo and confirmation | high | `references/engineering-mastery.md` | covered by `hci-error-prevention` |
| 263 | accessibility | Keyboard order, focus and traps | high | `references/engineering-mastery.md` | covered by `a11y-keyboard` |
| 264 | accessibility | Labels, roles and live regions | medium | `references/engineering-mastery.md` | open |
| 265 | accessibility | Contrast, non-color cues and zoom | medium | `references/engineering-mastery.md` | open |
| 266 | accessibility | Reduced motion and vestibular safety | medium | `references/engineering-mastery.md` | open |

Close a gap with `./beril remember add`, then `./beril gaps --cover <gap> --card <id>`.
