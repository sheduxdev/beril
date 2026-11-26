# Firewall, WAF and filter defense

Why filters get bypassed, and how a defender closes the gap. This is a defender's page. Understand evasion so you can test your own controls and layer them. A filter is a speed bump, never the fix. Use it only against systems you own or have written scope for.

Snapshot 2026-11-26.

## The core idea

A firewall, WAF or IPS makes a decision on a parsed view of traffic. Every bypass is a disagreement between what the filter parsed and what the backend will parse. Defense is therefore two moves: fix the real sink behind the filter, and shrink the parser gap so the filter and the backend agree.

## Why filters fail, and the defensive answer

| Evasion principle | Why it works | Defensive answer |
|---|---|---|
| Encoding and normalization gaps | Filter and app decode differently (URL, double-URL, unicode, case) | Normalize to one canonical form before the rule, then decode once in the app |
| Parser differential | Filter and backend disagree on boundaries (CL/TE, charset, multipart) | One parser, reject ambiguous requests, keep WAF and app decoders in step |
| Protocol downgrade / smuggling | HTTP/2 to HTTP/1.1 rewrite changes framing | Terminate consistently, reject malformed framing (`web-http2-downgrade`, `web-desync-parser-disagreement`) |
| Obfuscated payloads | Comments, whitespace, alternative syntax slip signatures | Prefer positive security (allowlist) over blocklists; score, don't single-match |
| Traffic volume / distribution | Many IPs via proxies dilute per-source rules | Rate-limit per identity and behavior, not per IP alone |
| Encryption | Payload rules cannot see inside TLS | Decrypt at the edge for inspection, or rely on behavior and egress |
| Allowed-channel abuse | C2 rides 443, 53, cloud APIs that are permitted | Egress allowlist and protective DNS (`net-egress-filtering`) |

## WAF deployment

- Run OWASP CRS or Coraza in detection-only first, collect a week of real traffic, then tune. See `defense-waf-anomaly-score`.
- CRS scores per rule and blocks on a threshold (default inbound 5). Raise paranoia level one step at a time.
- Write exclusions per path and parameter, never a global off switch.
- A WAF virtual-patches a known CVE while the real patch ships. It does not replace the patch.

## IDS and IPS baseline

- Suricata or Snort in IDS mode first; rank rules by alert volume. Threshold or suppress the noisy ones with a note. See `defense-ips-inline-tuning`.
- Switch to inline drop per rule category, not all at once.
- Encrypted traffic needs decryption or the payload rules are blind; lean on TLS metadata, JA3/JA4 and egress.

## Egress and C2 prevention

- Default-deny outbound, allow known-good per host, deny-and-log the rest (`net-egress-filtering`).
- Force internal or protective DNS resolvers; filter DNS to untrusted domains (MITRE M1037.004).
- Servers should not browse the internet; give each a narrow destination list.
- C2 hides in permitted traffic, so blocking known-bad indicators alone always lags.

## Layer the controls

No single box is the perimeter. A workable stack is edge DDoS and anycast, then TLS termination with WAF, then app-level input handling and authz, then host egress control and EDR, then detection on what still gets through (`detection-sigma`, `detection-beacon`, `detection-dns`). Each layer assumes the one in front can fail.

## Primary sources

| Source | Endpoint | Use |
|---|---|---|
| MITRE ATT&CK Filter Network Traffic | `https://attack.mitre.org/mitigations/M1037/` | Egress and protocol filtering |
| MITRE ATT&CK T1071 | `https://attack.mitre.org/techniques/T1071/` | C2 over permitted protocols |
| SANS ISC egress filtering | `https://isc.sans.edu/diary/18379` | Building an egress allowlist |
| OWASP CRS docs | `https://coreruleset.org/docs/` | Anomaly scoring, paranoia levels |
| Coraza | `https://coraza.io/docs/` | CRS-compatible WAF |
| Suricata docs | `https://docs.suricata.io/` | IDS/IPS tuning |
| NIST SP 800-94 | `https://csrc.nist.gov/pubs/sp/800/94/final` | IDPS classes |
| CISA DDoS joint guide | `https://www.cisa.gov/resources-tools/resources/understanding-and-responding-distributed-denial-service-attacks` | Layered DDoS defense |

Rule of the page. Every evasion listed here is a reason to add a layer and fix the sink, not a recipe to run against someone else's network.
