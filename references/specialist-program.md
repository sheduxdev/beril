# Specialist program

A senior tester is not a person who knows every payload. It is a person who can
enter an unfamiliar system, build a threat model, choose one class, prove it,
explain the business impact and stop at the right time.

This program turns the existing Beril material into twelve four week tracks.
Each track ends with an artifact a client, a maintainer or a peer can review.
`references/senior-bar.md` is the cross track rubric.

## Rules

1. One track at a time. One week per theme.
2. Read the primary source before the lab.
3. Every week has an artifact. A week without evidence is a read.
4. The local lab comes first. External labs fill the classes the lab lacks.
5. Redo one old track week each month.
6. Keep a portfolio. Track artifacts are the portfolio.
7. A track is done when a peer can rerun the exit proof from your notes.

## How to choose

| Your current work | Start with |
|---|---|
| Bounty programs on SaaS | Track 1, then 2 and 3 |
| Enterprise internal pentest | Track 2, then 5 and 4 |
| Product security at a vendor | Track 1, then 9 and 8 |
| Cloud or platform team | Track 4, then 9 |
| Malware or exploit research | Track 6, then 11 |
| Mobile product | Track 7, then 3 |
| SOC or IR | Track 8, then 5 and 4 |
| AI product | Track 10, then 3 and 9 |

Do not start with the track you already know. Use the entry drill to confirm
the level, then move.

## Weekly loop

| Day | Work | Artifact |
|---|---|---|
| 1 | Read the primary source and write five questions | Question sheet |
| 2 | First drill, no notes | Raw output |
| 3 | Second drill, debug the failure | Debug log |
| 4 | Lab, first pass | Request or input |
| 5 | Exit proof, write it for a reviewer | One page |

Two hours a day. Ten hours a week. A missed day is not a missed week.

## The tracks

### 1. Web application and business logic

Outcome. You can find authorization, state machine and parser bugs that a
scanner cannot see.

Prerequisite. `labs/web`, ten PortSwigger labs, HTTP confidence.

| Week | Focus | Drill | Artifact |
|---|---|---|---|
| 1 | Threat model the app and the money flow | Draw the objects, actors and state changes | Threat model |
| 2 | Access control and IDOR | Two accounts, swap every id | Request pair |
| 3 | Race and state machine | Parallel requests on one transition | Timing table |
| 4 | Parser and cache differentials | Compare proxy, app and CDN parsing | Diff sheet |

Key material. `references/techniques.md` cards 6, 7, 9, 14, 15, 16,
`references/bug-method-matrix.md`, `labs/web`.

Senior failure. Reporting a reflection as XSS, or an IDOR without the second
account proof.

Exit proof. One chain with a business impact and a fix a developer can apply.

### 2. Identity, authentication and SSO

Outcome. You can test OAuth, OIDC, SAML, JWT, session and MFA flows without
breaking the login for everyone.

Prerequisite. Track 1 week 2. Basic crypto and cookie handling.

| Week | Focus | Drill | Artifact |
|---|---|---|---|
| 1 | Session model and cookie scope | Map every session transition | Session map |
| 2 | OAuth and OIDC | Redirect binding, state, nonce, PKCE downgrade | Request chain |
| 3 | SAML and JWT | Signature wrapping, algorithm confusion, claim trust | Forged assertion |
| 4 | Reset, MFA and account recovery | Host header, token reuse, OTP race | Bypass chain |

Key material. `references/techniques.md` card 17, `knowledge/web-saml-signature-wrapping.md`,
`knowledge/web-jwt-signature-trust.md`, `knowledge/web-oauth-redirect-binding.md`,
PortSwigger OAuth and SAML labs.

Senior failure. Calling a decoded JWT a bypass, or testing MFA lockout on the
only admin account.

Exit proof. One account takeover path with two victims and a clean reset.

### 3. API, GraphQL and mobile backends

Outcome. You can test object, field and operation authorization across REST,
GraphQL and WebSocket APIs.

Prerequisite. Track 1. JSON and schema reading.

| Week | Focus | Drill | Artifact |
|---|---|---|---|
| 1 | Inventory and schema | Diff the public schema against the calls | Schema diff |
| 2 | BOLA and mass assignment | Change every object and field | Field matrix |
| 3 | GraphQL depth and batching | Alias batching, depth limit, introspection | Query pair |
| 4 | Rate limit and webhook trust | Bypass one quota, forge one signature | Bypass note |

Key material. `references/techniques.md` cards 16 and 18, `knowledge/api-*`,
`docs/scan-artifacts.md`.

Senior failure. Introspection alone as a finding, or a batch query without the
rate limit impact.

Exit proof. One cross tenant read or write with a request pair.

### 4. Cloud, container and Kubernetes

Outcome. You can follow a role, a token and a workload to a blast radius and
prove it read only.

Prerequisite. Track 2. Linux and one cloud CLI.

| Week | Focus | Drill | Artifact |
|---|---|---|---|
| 1 | Identity and metadata | Trace a role to its policies | Role graph |
| 2 | Storage and secrets | Find one public or over broad path | Read only proof |
| 3 | Container and pod | Socket, hostPath, service account | Escape path |
| 4 | CI identity and trust | OIDC trust policy and subject claim | Trust diff |

Key material. `labs/cloud`, `references/techniques.md` card 19,
`knowledge/cloud-*`, `docs/network-runbook.md`.

Senior failure. A wildcard policy without the reachable action, or a metadata
read without the role's real permissions.

Exit proof. A read only path from a low privilege workload to a named asset.

### 5. Active Directory and Windows enterprise

Outcome. You can map an AD path, choose the shortest edge and prove access
without locking accounts.

Prerequisite. Track 2. Windows basics and BloodHound.

| Week | Focus | Drill | Artifact |
|---|---|---|---|
| 1 | Enumeration and ACL graph | Map users, groups and control edges | Graph path |
| 2 | Kerberos | Kerberoast, AS REP roast, delegation | Ticket evidence |
| 3 | ADCS and certificate paths | ESC1 and one other template flaw | Certificate proof |
| 4 | Lateral movement | One hop with a clean log trail | Hop chain |

Key material. `labs/ad`, `references/techniques.md` card 20,
`knowledge/ad-*`, `knowledge/detection-identity.md`.

Senior failure. Running a spray without the lockout policy, or calling an ACL
edge exploitable without the write proof.

Exit proof. A path from a normal user to a named high value group.

### 6. Binary exploitation and exploit development

Outcome. You can turn a crash into a primitive, then into a reliable PoC with
mitigations accounted for.

Prerequisite. C, assembly, `labs/binary`.

| Week | Focus | Drill | Artifact |
|---|---|---|---|
| 1 | Crash triage | Classify five crashes by primitive | Triage sheet |
| 2 | Stack and ROP | Build a chain on the NX binary | Chain and reliability |
| 3 | Heap and UAF | Reallocate and control a pointer | Heap note |
| 4 | Mitigation bypass | Leak, ASLR, canary, then a full PoC | PoC and limits |

Key material. `labs/binary`, `labs/fuzz`, `references/exploit-development.md`,
`knowledge/re-crash-triage-primitive.md`, `knowledge/binary-*`.

Senior failure. A one shot PoC with no reliability number, or a crash called
exploitable without control proof.

Exit proof. A PoC that works 18 of 20 runs on the agreed build.

### 7. Mobile and client side

Outcome. You can test deep links, WebView bridges, storage and transport on a
real device without losing the evidence.

Prerequisite. Track 1. ADB or Xcode basics.

| Week | Focus | Drill | Artifact |
|---|---|---|---|
| 1 | Manifest and surface | List exported components and schemes | Surface sheet |
| 2 | Deep link to data | Drive one component with an external intent | Intent proof |
| 3 | WebView and bridge | Reach a native method from page script | Bridge trace |
| 4 | Storage, ATS and pinning | Extract one protected value | Extraction note |

Key material. `labs/mobile`, `references/mobile-reverse.md`,
`knowledge/mobile-*`, MASTG.

Senior failure. A debuggable build as the only finding, or a hook that only
works on a rooted device without saying so.

Exit proof. One external entry to sensitive data or action, with device state.

### 8. Detection, incident response and forensics

Outcome. You can build a timeline, write a rule, measure false positives and
explain containment order.

Prerequisite. Track 5 or 4. Log reading.

| Week | Focus | Drill | Artifact |
|---|---|---|---|
| 1 | Timeline and evidence | Order a five event incident | Timeline |
| 2 | Sigma and logsource | Write and test one rule | Rule and match |
| 3 | False positive analysis | Tune the rule against a clean day | FP table |
| 4 | Containment and recovery | Write the order and the rollback | Runbook |

Key material. `labs/detection`, `references/network-curriculum.md`,
`knowledge/detection-*`, `docs/network-runbook.md`.

Senior failure. A rule with no false positive measurement, or containment that
destroys the evidence first.

Exit proof. A rule with a measured false positive rate and a runbook.

### 9. Supply chain, CI and build security

Outcome. You can audit a build from source to artifact and find the trust
boundary that actually matters.

Prerequisite. Track 1. Git and CI.

| Week | Focus | Drill | Artifact |
|---|---|---|---|
| 1 | Dependency and lockfile | Find one reachable vulnerable path | Reachability note |
| 2 | CI permissions and triggers | Map token scope and fork rules | Permission table |
| 3 | Artifact and provenance | Verify one SBOM and one signature | Verify log |
| 4 | Publish and install path | Test one install hook or postinstall | Hook trace |

Key material. `docs/secrets.md`, `knowledge/cicd-*`, `knowledge/build-*`,
`data/osv_seed.json`, `scripts/deps.py`, `scripts/sbom.py`.

Senior failure. A dependency CVE with no import reachability, or a pin that
only moves the trust to an unpinned action.

Exit proof. One build path with a named trust gap and a fix.

### 10. AI, LLM and agent security

Outcome. You can model the data, tool and tenant boundaries of an AI feature
and prove one boundary crossing.

Prerequisite. Track 3. Basic prompt and RAG reading.

| Week | Focus | Drill | Artifact |
|---|---|---|---|
| 1 | Threat model | Map data, tools, tenants and memory | Boundary map |
| 2 | Direct and indirect injection | Plant one instruction through content | Injection trace |
| 3 | Tool and sandbox | Reach one tool side effect | Tool call proof |
| 4 | RAG and memory isolation | Cross one tenant filter | Leak proof |

Key material. `labs/llm`, `knowledge/ai-*`,
`references/techniques.md` card 24, `docs/prompt-injection.md`.

Senior failure. A system prompt leak as impact, or a tool call without a
side effect.

Exit proof. One boundary crossing with a reproducible prompt and result.

### 11. Firmware, hardware and IoT

Outcome. You can extract an image, map the boot path and prove one update or
debug weakness.

Prerequisite. Track 6. Linux and a UART adapter.

| Week | Focus | Drill | Artifact |
|---|---|---|---|
| 1 | Extraction | Unblob the image and map the rootfs | File tree |
| 2 | Services and CGI | Find and prove one injection | Request pair |
| 3 | Update and signature | Check the verify path and rollback | Verify note |
| 4 | Debug and boot | UART or JTAG access, secure boot state | Boot log |

Key material. `labs/firmware`, `references/firmware-iot.md`,
`knowledge/firmware-*`.

Senior failure. A shadow hash as root proof, or a debug port on a production
board without a recovery note.

Exit proof. One command execution or boot control with a recovery path.

### 12. Network, DNS, TLS and BGP

Outcome. You can test segmentation, egress and routing without flooding the
target.

Prerequisite. Track 4 or 8. Packet reading.

| Week | Focus | Drill | Artifact |
|---|---|---|---|
| 1 | Segmentation | Map allowed and denied paths | Matrix |
| 2 | DNS and TLS | Test resolver and certificate trust | Trust note |
| 3 | Egress and proxy | Find one allowed channel | Channel proof |
| 4 | BGP and RPKI | Check one prefix and its ROA | Posture note |

Key material. `references/network-curriculum.md`, `references/network-checklist.md`,
`labs/netcheck`, `docs/bgp-runbook.md`, `knowledge/detection-dns.md`.

Senior failure. A port scan as segmentation proof, or a BGP claim without the
RPKI state.

Exit proof. One closed bypass and one measured rule or route check.

## Sequence

| Months | Track | Why |
|---|---|---|
| 1 | 1 and 2 | Every other track depends on web and identity |
| 2 | 3 and 4 | Modern product surface |
| 3 | 5 or 6 | Choose enterprise or exploit depth |
| 4 | 7 or 8 | Choose client or defense |
| 5 | 9 and 10 | Current supply chain and AI risk |
| 6 | 11 or 12 | Depth or infrastructure |

Twelve tracks is a year. That is the point. A senior does not finish the
program, they keep one track warm every month.

## Assessment

Score each track artifact on the senior bar. Twenty four or more is a pass,
thirty or more is principal level. Below eighteen means repeat the exit proof
with a new target.

## Portfolio

Keep one artifact per track. Redact client data. Publish the writeups that are
allowed. A portfolio of twelve exit proofs beats a list of certificates.

## Sources

Every track uses a local lab, a reference and a knowledge card set. Add one
primary source per week from `references/books.md` or the vendor docs. A track
without an external primary source is a rehearsal, not a study.
