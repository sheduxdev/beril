# Research log: network defense

Date: 2026-11-23. Purpose: build the visibility and protection notes from primary
or near-primary sources, and mark what is not verified.

## Sources read

| Source | Key claim used | Confidence | Gap |
|---|---|---|---|
| CISA/NSA/FBI joint advisory, 2025 | IT users reached a SCADA VLAN; default deny, DMZ, bastion, out-of-band management | High | One victim environment |
| CISA microsegmentation guidance, 2025 | Segment policy follows the resource; study bypasses; phased rollout | High | FCEB focus, generalizes |
| CISA CPGs | 2.F segmentation, 2.T logging, 2.U log protection, 2.M email auth | High | Outcome list, not a build guide |
| CISA communications hardening, 2024 | Flow monitoring at ingress and egress, config change alerts, packet capture with retention policy | High | Telecom focus |
| NIST SP 800-94 | IDPS types; false positives and negatives; anomaly profiles can absorb slow attacks | High | 2007, note says replacement pending |
| NIST SP 800-61r3 | Detect function needs continuous monitoring and correlation across sources | High | Framework, not tooling |
| SANS flow paper | Flows survive encryption, show scope and beaconing, prove who talked to whom | Medium | 2012 paper, technique stable |
| SANS metadata paper | Enriched metadata sits between full pcap and flow; tiered retention | Medium | Vendor hosted paper |
| Zeek log reference | Protocol logs and `capture_loss.log` | High | Documentation only |
| Suricata EVE reference | Alert, flow, DNS, TLS and anomaly records; community ID | High | Documentation only |
| MITRE ATT&CK T1071.004 | DNS as C2, encoded labels, detection analytics | High | Technique catalog |
| MITRE D3FEND Network Isolation | DNS and traffic filtering taxonomy | High | Taxonomy, not product |
| Cloudflare DDoS page | Volumetric, protocol and application attacks; rate limit, WAF, anycast, blackhole | Medium | Vendor explainer |
| Cloudflare ECH article | ECH encrypts ClientHello and SNI, depends on DoH key distribution | Medium | 2020 article, protocol has moved |
| RFC 8484 | DoH hides DNS from on-path inspection | High | Standard |
| Sigma rule docs | Rule structure, false positives field, level semantics | High | Documentation |
| Tetragon docs | eBPF process and network observability with enforcement | Medium | Product docs |
| Cowrie docs | SSH/Telnet honeypot, JSON events, uploaded files | Medium | Product docs |

## Inferences

- ECH plus DoH shifts weight to endpoint and runtime telemetry. This follows from
  the two encryption layers, but the exact coverage depends on the sensor.
- A flow-only program is cheap and still catches beaconing and scope. It cannot
  prove content theft. The SANS paper says the same.
- A WAF is an IDS with a block action and needs the same tuning discipline. This
  is an analogy, not a sourced claim.

## Not verified

- Current market share of ECH on major sites.
- Whether every cloud flow log includes the fields needed for beacon scoring.
- Exact Zeek and Suricata performance limits on 10G and above.
- Legal retention limits for packet capture in Turkey. Needs a lawyer.

## Next research

- TLS 1.3 and ECH measurement on a sample of local sites, with `openssl s_client`.
- Sigma conversion for a local backend, with a small rule set.
- A beacon scoring script against a public pcap.
- Cloud flow log field inventory for AWS, GCP and Azure.
