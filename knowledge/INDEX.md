# Knowledge index

246 durable cards. Read this before a web search; open a card only when it matches.

| id | title | tags | confidence | updated |
|---|---|---|---|---|
| `ad-acl-path` | AD compromise is an edge path, not a single bug | ad, windows, acl | high | 2026-11-24 |
| `ad-adcs-esc1` | ESC1 is an enrollable SAN on a client-auth template | ad, adcs, certificate | high | 2026-11-24 |
| `ai-sandbox-escape` | A code interpreter is a process with a filesystem | ai, sandbox, interpreter | high | 2026-11-24 |
| `ai-guardrail` | A guardrail is a classifier with an input distribution | ai, guardrail, bypass | medium | 2026-11-25 |
| `ai-vector-auth` | A vector query still needs an ACL | ai, rag, vector | medium | 2026-11-24 |
| `ai-memory-poison` | Agent memory is a write target | ai, agent, memory | high | 2026-11-24 |
| `ai-agent-tool` | Agent tool abuse is argument control, not prompt text | ai, agent, tool | high | 2026-11-24 |
| `ai-cost-control` | An agent loop is a budget bug | ai, cost, agent | medium | 2026-11-24 |
| `ai-agent-planning` | An agent plan is a permission boundary | ai, agent, planning | high | 2026-11-24 |
| `ai-embedding` | An embedding is not anonymized data | ai, embedding, rag | medium | 2026-11-24 |
| `ai-indirect-injection-tool` | Indirect injection turns a document into an instruction | ai, llm, prompt-injection | high | 2026-11-24 |
| `ai-mcp` | MCP config is a trust boundary with filesystem and network rights | ai, mcp, config | high | 2026-11-24 |
| `ai-model-extraction` | Model extraction is a query budget problem | ai, model, extraction | medium | 2026-11-24 |
| `ai-multiagent` | Multi-agent trust is a delegation graph | ai, multiagent, delegation | high | 2026-11-25 |
| `ai-data-poison` | Poisoned data changes the model or the retrieval set | ai, data, poisoning | high | 2026-11-24 |
| `ai-rag-tenant-filter` | RAG leaks when retrieval ignores the tenant | ai, llm, rag | high | 2026-11-24 |
| `ai-tool-output` | Tool output is untrusted input to the next turn | ai, tool, injection | high | 2026-11-24 |
| `api-batch` | A batch endpoint checks the envelope, not each item | api, batch, auth | medium | 2026-11-25 |
| `api-webhook-signature` | A webhook without HMAC is an unauthenticated write | api, webhook, hmac | high | 2026-11-24 |
| `api-openapi` | An exposed schema is a map, not a finding | api, openapi, schema | high | 2026-11-24 |
| `api-oauth-device` | Device code flow is phishing with a real code | api, oauth, device-code | medium | 2026-11-24 |
| `api-jwt-rotation` | Key rotation is a cache and trust problem | api, jwt, jwks | high | 2026-11-24 |
| `api-mass-assignment` | Mass assignment is a binder trusting extra fields | api, json, mass-assignment | high | 2026-11-24 |
| `api-versioning` | Old API versions keep old authorization | api, versioning, shadow | high | 2026-11-24 |
| `api-pagination` | Pagination is an enumeration and counting oracle | api, pagination, enumeration | medium | 2026-11-25 |
| `api-rate-limit-bypass` | Rate limits are only as strong as the key | api, rate-limit, bypass | high | 2026-11-24 |
| `api-idempotency` | Retries need an idempotency key at the write | api, idempotency, retry | high | 2026-11-24 |
| `api-sse` | Server-sent events need per-connection auth | api, sse, stream | medium | 2026-11-24 |
| `api-websocket-auth` | WebSocket authorization is per message and per channel | api, websocket, auth | high | 2026-11-25 |
| `api-grpc-reflection` | gRPC reflection is a map, per-method auth is the bug | api, grpc, reflection | medium | 2026-11-24 |
| `binary-hypervisor` | A hypervisor exposes synthetic MSRs and VTL boundaries | binary, hypervisor, virtualization | low | 2026-11-24 |
| `binary-kernel` | A kernel bug is an object lifetime bug with a user buffer | binary, kernel, driver | high | 2026-11-24 |
| `binary-browser` | Browser exploitation needs a renderer bug and a sandbox path | binary, browser, jit | high | 2026-11-24 |
| `binary-jit` | JIT bugs are about generated code and stale metadata | binary, jit, exploit | medium | 2026-11-24 |
| `binary-macos` | Mach-O and dyld define what loads before main | binary, macos, macho | medium | 2026-11-25 |
| `binary-ebpf` | The eBPF verifier is the security boundary | binary, ebpf, verifier | low | 2026-11-25 |
| `binary-uefi` | UEFI is an event-driven firmware runtime | binary, uefi, firmware | medium | 2026-11-24 |
| `binary-wasm` | Wasm modules have validation and a host boundary | binary, wasm, sandbox | medium | 2026-11-25 |
| `binary-windows-kernel` | Windows kernel bugs are object and IRP lifetime bugs | binary, windows, kernel | high | 2026-11-25 |
| `browser-extension-permissions` | An extension is a trusted page with broad APIs | browser, extension, permissions | medium | 2026-11-24 |
| `cloud-docker-socket` | A mounted Docker socket is root on the host | cloud, docker, container | medium | 2026-11-24 |
| `cloud-k8s-hostpath` | A privileged pod with hostPath is a host escape | cloud, kubernetes, container | high | 2026-11-24 |
| `cloud-secrets` | A secrets manager is only as strong as its policy | cloud, secrets, iam | high | 2026-11-24 |
| `cloud-service-mesh` | A sidecar is a second network path | cloud, istio, mtls | medium | 2026-11-25 |
| `cloud-aks-identity` | AKS mixes Azure RBAC and Kubernetes RBAC | cloud, aks, kubernetes | medium | 2026-11-24 |
| `cloud-alibaba-ram` | Alibaba RAM roles and STS follow the same trust graph | cloud, alibaba, ram | low | 2026-11-25 |
| `cloud-azure-role` | Azure identity is a role assignment graph | cloud, azure, iam | high | 2026-11-24 |
| `cloud-oidc-ci` | CI OIDC trust is a subject claim match | cloud, oidc, ci | high | 2026-11-24 |
| `cloud-metadata-role` | Cloud metadata is a credential endpoint | cloud, ssrf, iam | high | 2026-11-24 |
| `cloud-eks` | EKS has two identity planes: IAM and Kubernetes | cloud, eks, kubernetes | medium | 2026-11-24 |
| `cloud-gcp-iam` | GCP IAM binds a member to a role on a resource | cloud, gcp, iam | high | 2026-11-24 |
| `cloud-iam-wildcard` | IAM wildcard is administrator access until proven otherwise | cloud, iam, aws | high | 2026-11-24 |
| `cloud-oci` | OCI policy is compartment and tenancy scoped | cloud, oci, iam | low | 2026-11-24 |
| `cloud-openstack` | OpenStack policy is a service and project graph | cloud, openstack, keystone | low | 2026-11-25 |
| `cloud-serverless` | Serverless events are input, not a trusted trigger | cloud, serverless, lambda | medium | 2026-11-24 |
| `cloud-terraform-state` | Terraform state is a secret store | cloud, terraform, state | medium | 2026-11-24 |
| `cloud-vmware` | VMware appliances are a chain of SSO and service bugs | cloud, vmware, vcenter | high | 2026-11-25 |
| `comp-jit` | A JIT has tiers, guards and a code cache | compiler, jit, deopt | high | 2026-11-25 |
| `comp-ssa` | SSA makes each definition single and explicit | compiler, ssa, dataflow | high | 2026-11-25 |
| `container-escape` | A container escape is a host resource exposed to the container | container, escape, kubernetes | high | 2026-11-24 |
| `crypto-kdf` | A password hash is a cost parameter | crypto, kdf, password | medium | 2026-11-25 |
| `key-management` | Key management is where crypto bugs become data bugs | crypto, keys, storage | medium | 2026-11-24 |
| `crypto-postquantum` | PQC migration is a hybrid, not a flag | crypto, pqc, hybrid | low | 2026-11-24 |
| `crypto-weak-random` | Predictable randomness is a key recovery bug | crypto, random, predictability | high | 2026-11-24 |
| `tls-config-review` | TLS is a version, a chain and a policy | crypto, tls, certificate | medium | 2026-11-24 |
| `detection-sigma` | A Sigma rule needs a logsource, a selection and a false-positive note | detection, sigma, log | high | 2026-11-24 |
| `detection-beacon` | A beacon is a timing pattern, not a single request | detection, beacon, network | medium | 2026-11-24 |
| `detection-cloud` | Cloud detection is control-plane and role-assumption first | detection, cloud, audit | high | 2026-11-25 |
| `detection-dns` | DNS tunneling is a length and entropy pattern | detection, dns, tunnel | medium | 2026-11-25 |
| `detection-edr` | EDR detection is a process tree and a sequence | detection, edr, process | medium | 2026-11-24 |
| `detection-identity` | Identity detections need a baseline and a token context | detection, identity, logs | high | 2026-11-25 |
| `detection-lolbins` | LOLBins hide in parent-child and arguments | detection, lolbins, process | high | 2026-11-24 |
| `detection-tls` | TLS fingerprints identify a client stack, not a person | detection, tls, ja3 | medium | 2026-11-25 |
| `detection-threatintel` | Threat intel ages and IOCs are easy to rotate | detection, intel, ioc | medium | 2026-11-24 |
| `dist-crdt` | A CRDT merges without coordination | distributed, crdt, merge | high | 2026-11-25 |
| `dist-partition` | A partition forces a choice between availability and consistency | distributed, partition, cap | high | 2026-11-25 |
| `dist-ordering` | Exactly-once is at-least-once plus dedup | distributed, ordering, dedup | high | 2026-11-25 |
| `dist-clock` | Physical clocks skew; logical clocks order events | distributed, clock, causality | high | 2026-11-25 |
| `electron-context-isolation` | Electron is Node with a browser attached | electron, desktop, context-isolation | medium | 2026-11-24 |
| `eng-gc` | A GC trades throughput for pause and space | engineering, gc, allocation | medium | 2026-11-25 |
| `eng-regression` | A bug fix needs a test that failed before it | engineering, testing, regression | high | 2026-11-25 |
| `eng-repro-build` | A build should be reproducible from a clean checkout | engineering, build, reproducible | high | 2026-11-25 |
| `eng-cache-invalidation` | A cache needs a key, a TTL and an invalidation path | engineering, cache, invalidation | high | 2026-11-25 |
| `eng-timeouts` | A call without a deadline can hang a pool | engineering, timeouts, reliability | high | 2026-11-25 |
| `eng-compiler` | A compiler is a pipeline of representations | engineering, compiler, parsing | low | 2026-11-25 |
| `eng-communication` | A decision nobody understands is a future incident | engineering, communication, writing | high | 2026-11-25 |
| `eng-feature-flags` | A feature flag is a temporary branch with an owner | engineering, feature-flag, release | medium | 2026-11-25 |
| `eng-migrations` | A migration is expand, backfill, switch, contract | engineering, database, migration | high | 2026-11-25 |
| `eng-platform` | A platform is a paved road, not a gate | engineering, platform, dx | medium | 2026-11-25 |
| `eng-postmortem` | A postmortem is blameless and actionable | engineering, postmortem, learning | high | 2026-11-25 |
| `eng-backpressure` | A queue without a limit is a memory leak | engineering, queue, backpressure | high | 2026-11-25 |
| `eng-rate-limit` | A rate limiter needs a key, a cost and a fairness rule | engineering, rate-limit, fairness | medium | 2026-11-25 |
| `eng-roadmap` | A roadmap is a set of bets with kill criteria | engineering, roadmap, product | medium | 2026-11-25 |
| `eng-distributed-tx` | A saga is a sequence with compensation | engineering, distributed, transaction | high | 2026-11-25 |
| `eng-boundaries` | A service boundary owns a decision and its data | engineering, architecture, boundaries, boundary, ownership, service, data, team | high | 2026-11-25 |
| `eng-tradeoffs` | A tradeoff without a cost is marketing | engineering, tradeoffs, design, cost, architecture | high | 2026-11-25 |
| `eng-transactions` | A transaction is a boundary, not a decoration | engineering, database, transactions | high | 2026-11-25 |
| `eng-api-versioning` | A version is a deprecation clock | engineering, api, versioning | medium | 2026-11-25 |
| `eng-accessibility` | Accessibility is a correctness requirement | engineering, accessibility, ui | medium | 2026-11-25 |
| `eng-api-contract` | An API is a promise about errors and time | engineering, api, contract | high | 2026-11-25 |
| `eng-slo` | An SLO is a budget for unreliability | engineering, sre, slo | high | 2026-11-25 |
| `eng-errors` | An error is a value with a caller decision | engineering, errors, api | high | 2026-11-25 |
| `eng-estimation` | An estimate is a range and its assumptions | engineering, estimation, planning | medium | 2026-11-25 |
| `eng-hiring` | An interview samples the job, not trivia | engineering, hiring, interview | low | 2026-11-25 |
| `eng-backup-restore` | An untested backup is a hope | engineering, backup, restore | high | 2026-11-25 |
| `eng-mentoring` | Ask until the blocker is clear | engineering, mentoring, teaching | high | 2026-11-25 |
| `eng-idempotent-consumer` | At-least-once delivery needs an idempotent consumer | engineering, queue, consumer | high | 2026-11-25 |
| `eng-debug-bisect` | Bisect the space, not the code | engineering, debugging, bisect | high | 2026-11-25 |
| `eng-cqrs` | CQRS separates the write model from the read model | engineering, cqrs, read-model | medium | 2026-11-25 |
| `eng-cache-topology` | Cache placement decides the failure mode | engineering, cache, topology | medium | 2026-11-25 |
| `eng-frontend-state` | Client state and server state are different caches | engineering, frontend, state | medium | 2026-11-25 |
| `eng-compliance` | Compliance is evidence of a control | engineering, compliance, soc2 | medium | 2026-11-25 |
| `eng-concurrency` | Concurrency bugs are about shared state and ordering | engineering, concurrency, locks | high | 2026-11-25 |
| `eng-config` | Config belongs to the environment, secrets belong to a store | engineering, config, secrets | high | 2026-11-25 |
| `eng-congestion` | Congestion control is a queue management problem | engineering, network, congestion | medium | 2026-11-25 |
| `eng-consensus` | Consensus is quorum plus a log | engineering, distributed, consensus | high | 2026-11-25 |
| `eng-consistency` | Consistency is a contract about reads | engineering, distributed, consistency | high | 2026-11-25 |
| `eng-cost` | Cost is a design constraint | engineering, cost, cloud | medium | 2026-11-25 |
| `eng-disaster-recovery` | DR is RTO, RPO and a rehearsal | engineering, disaster, recovery | high | 2026-11-25 |
| `eng-data-model` | Data outlives code | engineering, data, schema | high | 2026-11-25 |
| `eng-deletion` | Deletion is a feature | engineering, deletion, maintenance | medium | 2026-11-25 |
| `eng-legacy-strangler` | Do not rewrite the legacy system; strangle it | engineering, legacy, refactor | high | 2026-11-25 |
| `eng-docs` | Docs are for the next decision | engineering, docs, writing | medium | 2026-11-25 |
| `eng-ethics` | Engineering judgment includes who pays | engineering, ethics, product | medium | 2026-11-25 |
| `eng-event-sourcing` | Events are the source of truth, state is a projection | engineering, event-sourcing, events | medium | 2026-11-25 |
| `eng-dependencies` | Every dependency is a maintenance contract | engineering, dependencies, supply-chain | medium | 2026-11-25 |
| `eng-idempotency` | Every retryable write needs a key | engineering, idempotency, retry | high | 2026-11-25 |
| `eng-logging` | Log the decision, not the whole world | engineering, logging, observability | medium | 2026-11-25 |
| `eng-memory` | Memory is virtual, cached and allocated in tiers | engineering, os, memory | medium | 2026-11-25 |
| `eng-multi-tenancy` | Multi-tenancy is isolation plus noisy-neighbor control | engineering, multi-tenant, isolation | high | 2026-11-25 |
| `eng-observability` | Observability answers the next question | engineering, observability, logs | high | 2026-11-25 |
| `eng-mobile-arch` | Offline-first is a merge problem | engineering, mobile, offline | medium | 2026-11-25 |
| `eng-performance-budget` | Performance is a budget before it is an optimization | engineering, performance, budget | high | 2026-11-25 |
| `eng-privacy` | Privacy is data minimization with a retention clock | engineering, privacy, data | high | 2026-11-25 |
| `eng-property-tests` | Property tests find the input you did not imagine | engineering, testing, property | medium | 2026-11-25 |
| `eng-refactor-small` | Refactor in small, behavior-preserving steps | engineering, refactor, testing | high | 2026-11-25 |
| `eng-requirements` | Requirements are a decision, not a transcript | engineering, requirements, product | high | 2026-11-25 |
| `eng-code-review` | Review the change, not the author | engineering, review, quality | high | 2026-11-25 |
| `eng-schema-evolution` | Schema changes must be compatible in both directions | engineering, schema, evolution, deploy, migration | high | 2026-11-25 |
| `eng-security-design` | Security is a property of the design | engineering, security, design | high | 2026-11-25 |
| `eng-simplicity` | Simplicity is removing accidental complexity | engineering, design, simplicity | high | 2026-11-25 |
| `eng-incident` | Stabilize before you diagnose | engineering, incident, operations | high | 2026-11-25 |
| `eng-storage` | Storage engines trade read cost for write cost | engineering, database, storage | medium | 2026-11-25 |
| `eng-team-topology` | Team boundaries shape the architecture | engineering, team, ownership | medium | 2026-11-25 |
| `eng-observability-cost` | Telemetry is a sampled product | engineering, observability, cost | medium | 2026-11-25 |
| `eng-testing-pyramid` | Test at the lowest level that can catch the bug | engineering, testing, pyramid | high | 2026-11-25 |
| `eng-i18n` | Text, time and money are not strings | engineering, i18n, locale | medium | 2026-11-25 |
| `eng-query-planner` | The planner is the database's brain | engineering, database, query | high | 2026-11-25 |
| `eng-ml-systems` | Training and serving must share the same features | engineering, ml, features | high | 2026-11-25 |
| `eng-type-systems` | Types are a proof the compiler can check | engineering, types, compiler | medium | 2026-11-25 |
| `eng-finops` | Unit economics make cost a design signal | engineering, finops, cost | medium | 2026-11-25 |
| `exploit-uaf-reallocate` | UAF becomes control when the freed slot is reallocated | exploit, uaf, heap | high | 2026-11-24 |
| `exploit-rop-argument-registers` | x86_64 ROP needs the argument registers | exploit, rop, linux | high | 2026-11-24 |
| `firmware-update-sign` | A signed update is useless if verification is off | firmware, update, signature | high | 2026-11-24 |
| `firmware-cgi-injection` | Firmware CGI builds a shell string from the query | firmware, iot, command | high | 2026-11-24 |
| `firmware-jtag` | JTAG and SWD are identified by pinout and IDCODE | firmware, hardware, jtag | medium | 2026-11-24 |
| `firmware-radio` | Radio protocols are state machines with replay windows | firmware, radio, ble | medium | 2026-11-24 |
| `firmware-spi` | SPI flash reads need two matching dumps | firmware, hardware, spi | medium | 2026-11-24 |
| `firmware-secureboot` | Secure boot is a chain, not a boolean | firmware, secureboot, boot | high | 2026-11-24 |
| `firmware-uart` | UART is found by idle levels and confirmed by baud | firmware, hardware, uart | high | 2026-11-24 |
| `hardware-sidechannel` | Side channels leak through power, timing or EM | hardware, sidechannel | low | 2026-11-24 |
| `ir-timeline` | An incident timeline needs three independent clocks | ir, timeline, forensics | medium | 2026-11-24 |
| `ir-cloud` | Cloud audit logs are the timeline | ir, cloud, logs | medium | 2026-11-24 |
| `ir-container` | Container triage is image diff plus runtime state | ir, container, docker | medium | 2026-11-25 |
| `ir-disk` | Disk artifacts answer who, what and when | ir, disk, forensics | medium | 2026-11-24 |
| `ir-memory` | Memory is the most volatile evidence | ir, memory, forensics | medium | 2026-11-24 |
| `ir-mobile` | Mobile triage starts with the backup and the sysdiagnose | ir, mobile, ios | low | 2026-11-25 |
| `ir-phishing` | Phishing triage reads headers and detonates the payload | ir, phishing, email | medium | 2026-11-25 |
| `ir-ransomware` | Ransomware triage is scope, encryption and backups | ir, ransomware, backup | high | 2026-11-25 |
| `linux-suid` | A SUID binary is a path, not a finding | linux, privesc, suid | high | 2026-11-24 |
| `linux-cron-systemd` | Scheduled jobs inherit a weak PATH or writable unit | linux, privesc, cron, systemd | medium | 2026-11-24 |
| `mobile-deep-link-bridge` | A deep link plus a JS bridge is a chain | mobile, android, deep-link | high | 2026-11-24 |
| `mobile-ios-ats` | ATS exceptions are domain-scoped trust decisions | mobile, ios, ats | medium | 2026-11-24 |
| `mobile-provider-paths` | An exported provider with a broad path leaks files | mobile, android, provider | high | 2026-11-24 |
| `mobile-flutter` | Flutter hides logic in libapp.so and pins in Dart | mobile, flutter, dart | medium | 2026-11-24 |
| `mobile-swift` | Swift hooks need mangled names or a bridge | mobile, ios, swift | medium | 2026-11-24 |
| `mobile-swiftui-state` | SwiftUI state is not a security boundary | mobile, ios, swiftui | low | 2026-11-24 |
| `org-oncall` | On-call load is a reliability input | organization, oncall, reliability | high | 2026-11-25 |
| `org-conway` | The org chart leaks into the architecture | organization, conway, law, ownership, service, teams | high | 2026-11-25 |
| `process-retest` | A fix is not a fix until the same request fails | process, retest, regression | high | 2026-11-24 |
| `report-impact-chain` | A report is a chain a triager can rerun | process, report, impact | high | 2026-11-24 |
| `report-cvss-context` | CVSS without business context misranks the bug | process, report, cvss | medium | 2026-11-24 |
| `process-disclosure` | Disclosure is a timeline with a paper trail | process, disclosure, vendor | medium | 2026-11-24 |
| `cost-job-ledger` | Every job has an actor and a cost | process, cost, jobs | high | 2026-11-24 |
| `report-evidence` | Evidence must be reproducible and redacted | process, report, evidence | high | 2026-11-24 |
| `report-pricing` | Payout is a negotiation with evidence | process, pricing, severity | medium | 2026-11-25 |
| `process-bounty-platform` | Program rules decide what is payable | process, bounty, scope | medium | 2026-11-25 |
| `process-recall-before-research` | Recall before searching | process, memory, research | high | 2026-11-24 |
| `process-legal` | Safe harbor is written, not assumed | process, legal, authorization | medium | 2026-11-25 |
| `process-scope-parse` | Scope is a list of rules, not a domain | process, scope, recon | high | 2026-11-24 |
| `process-duplicate-search` | Search duplicates before writing a report | process, triage, duplicate | high | 2026-11-24 |
| `re-crash-triage-primitive` | A crash is a lead; the primitive is the finding | re, triage, crash | high | 2026-11-24 |
| `re-arm64` | AArch64 has a calling convention, PAC and MTE | re, arm64, pac | medium | 2026-11-25 |
| `re-cpp-rtti` | C++ RTTI and vtables reveal the class graph | re, cpp, rtti | medium | 2026-11-25 |
| `re-ghidrust-vs-ghidra` | GhidRust is a paused Ghidra plugin, not Ghidrust | re, ghidra, rust | high | 2026-11-24 |
| `re-go` | Go binaries carry pclntab and interface metadata | re, go, language | medium | 2026-11-24 |
| `re-android-native` | JNI is the bridge between Java and native code | re, android, jni | medium | 2026-11-25 |
| `re-jvm` | JVM bytecode is a stack machine with metadata | re, java, jvm | medium | 2026-11-24 |
| `re-macho` | Mach-O is a set of load commands, not a PE | re, macho, macos | medium | 2026-11-25 |
| `re-dotnet-aot` | Native AOT is not IL | re, dotnet, aot | medium | 2026-11-24 |
| `re-rust-layout` | Rust types are not C types | re, rust, layout | high | 2026-11-24 |
| `re-swift` | Swift uses witness tables and value types | re, swift, ios | medium | 2026-11-24 |
| `storage-wal` | A write-ahead log makes the write durable before the page | storage, wal, durability | high | 2026-11-25 |
| `storage-replication` | Replication has a lag and a loss window | storage, replication, failover | high | 2026-11-25 |
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
| `web-css-injection` | CSS injection exfiltrates attributes without script | web, css, injection | medium | 2026-11-25 |
| `web-cache-deception` | Cache deception dresses a private page as a static file | web, cache, deception | medium | 2026-11-24 |
| `web-cache-key-unkeyed-input` | Cache poisoning is an unkeyed input that changes the response | web, cache, cdn | high | 2026-11-24 |
| `web-clickjacking` | Clickjacking is a missing frame policy with a valuable action | web, clickjacking, ui | high | 2026-11-25 |
| `web-client-path-traversal` | Client-side path traversal is a router normalization bug | web, spa, router | medium | 2026-11-24 |
| `web-dom-clobbering` | DOM clobbering turns an id into a variable | web, dom, clobbering | medium | 2026-11-24 |
| `web-dangling-markup` | Dangling markup leaks what follows the injection | web, html, csrf | medium | 2026-11-25 |
| `web-desync-parser-disagreement` | Desync needs two HTTP parsers and an ambiguous length | web, http, smuggling | high | 2026-11-24 |
| `web-graphql-field-auth` | GraphQL authorization is per field, not per endpoint | web, graphql, api | high | 2026-11-24 |
| `web-http2-downgrade` | HTTP/2 adds a second parser for the same request | web, http2, smuggling | medium | 2026-11-24 |
| `web-idor-owner-check` | IDOR is a missing owner check, not a hidden id | web, idor, access-control | high | 2026-11-24 |
| `web-jsonp` | JSONP is script injection with a callback name | web, jsonp, script | medium | 2026-11-24 |
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
| `web3-contract` | Smart contracts fail on external calls and access control | web3, solidity, contract | high | 2026-11-25 |
| `win-service-acl` | A weak service ACL is local privilege escalation | windows, privesc, service | high | 2026-11-24 |
| `win-credential-stores` | Windows keeps credentials in more than one place | windows, credentials, dpapi | medium | 2026-11-24 |
| `win-token-privileges` | Windows token privileges are the privesc surface | windows, token, privesc | high | 2026-11-24 |
