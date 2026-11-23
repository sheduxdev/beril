# Network toolkit

A tool list with the question each tool answers and the way it lies. Install
only what you will tune. Every active tool needs a scope and a budget.

## Public lookup and routing

| Tool | Answers | Limits | Safety |
|---|---|---|---|
| Hurricane Electric BGP Toolkit (`bgp.he.net`) | Announcements, origin, upstreams, bogons, RPKI and ASPA report | One collector, caching, no policy | Passive HTTP |
| bgp.tools | Second collector, RPKI state, IRR view, looking glass | Partial paid features, sampling | Passive HTTP |
| RIPEstat (`stat.ripe.net`) | RIS routing history, prefix and ASN data, RPKI validity | Historical gaps, API rate | Passive HTTP |
| PeeringDB | NOC and abuse contacts, IX presence | Self-reported, can be stale | Passive HTTP |
| RouteViews and RIPE RIS | Public BGP archives | Sampled collectors, storage heavy | Bulk download |
| CAIDA Spoofer | Whether your network can send forged sources | Needs a client on two segments | Active test, light |
| Looking glasses | Router view from a network | Policy filtered, one view | Passive HTTP or telnet |

## Routing operations

| Tool | Answers | Limits | Safety |
|---|---|---|---|
| Routinator | Local RPKI validator, VRP output, RTR server | Needs updates, resource use | Local service |
| rpki-client | OpenBSD RPKI validator, file output | Platform preference | Local batch |
| ARTEMIS | Hijack and route leak detection from public feeds | Needs tuning, false positives | Passive monitor |
| BGPalerter | Prefix and path change alerts | Needs feed and config | Passive monitor |
| ExaBGP | Inject or receive routes for testing | Not a full router | Lab only |
| Batfish | Offline config analysis and policy test | Model, not live state | Read-only files |
| SuzieQ | Network state snapshot and query | Needs device access | Read-only API |
| NetBox | Source of truth for prefixes, devices and circuits | Manual data quality | Read/write app |

## Packet and flow

| Tool | Answers | Limits | Safety |
|---|---|---|---|
| tcpdump | Raw capture | No protocol decode, fast disk use | Passive |
| Wireshark and tshark | Protocol decode, stream follow, statistics | Memory on large files | Passive |
| Zeek | Protocol logs and scripting | No block by default, tuning | Passive |
| Suricata | Signature alerts, EVE JSON | False positives, TLS blindness | Passive or IPS |
| nfdump and nfsen | NetFlow analysis and graphs | Flow only, no content | Passive |
| pmacct | Flow and metadata export | Config heavy | Passive |
| Arkime | Full packet indexing and search | Storage heavy | Passive |
| Malcolm | Zeek, Suricata and Arkime bundle | Resource heavy | Passive |
| Security Onion | Detection and forensics suite | Large install | Passive |
| RITA | Beacon scoring from Zeek | Needs clean baseline | Passive |

## Host and runtime

| Tool | Answers | Limits | Safety |
|---|---|---|---|
| ss and lsof | Sockets and owning process | Host only | Passive |
| conntrack | Connection table | Kernel limits | Passive |
| nftables | Firewall and NAT state | Config risk | Write |
| Tetragon | eBPF process, file and network events, enforcement | Kernel and K8s focus | Passive or block |
| Falco | Runtime rule alerts | Rule tuning | Passive or block |
| Cilium | eBPF networking and network policy | CNI specific | Write |
| auditd | Syscall audit | Volume | Passive |
| Sysdig | Runtime capture | Commercial features | Passive |

## DNS and TLS

| Tool | Answers | Limits | Safety |
|---|---|---|---|
| dig | Query and DNSSEC check | One resolver view | Passive |
| dnstap | Structured DNS telemetry | Needs resolver support | Passive |
| dnstop | Live DNS query summary | Text only | Passive |
| Routinator or rpki-client | RPKI state for a prefix | Validator dependent | Passive |
| openssl s_client | TLS version, chain, SNI, ECH behavior | One connection | Passive |
| testssl.sh | Broad TLS configuration check | Noisy on shared hosts | Low rate |
| ZGrab2 | TLS and protocol fingerprint at scale | Go tool, needs scope | Low rate |

## Deception and email

| Tool | Answers | Limits | Safety |
|---|---|---|---|
| Cowrie | SSH and Telnet interaction, uploaded files | Emulated shell | Isolated host |
| Canary tokens | Whether a file or URL was opened | Callback dependency | Passive |
| mailoney | SMTP honeypot | Separate service | Isolated host |
| SPF and DMARC checkers | Mail policy state | DNS view only | Passive |

## Selection rules

1. Start with the question, then the tool. "I want to see beacons" needs flows,
   not a full pcap.
2. Prefer a tool that exports structured data. Screenshots do not correlate.
3. Check the data retention before deploying. A sensor that keeps two hours is
   an alert source, not a forensic source.
4. Tune in count mode first. A blocking tool with defaults is an outage waiting
   for a rule update.
5. Record the version. A finding without a version cannot be reproduced.
6. Pin the install. `latest` changes under you at the worst time.

## Anti-tool list

| Situation | Do not |
|---|---|
| Large east-west traffic | Mirror all packets to one box |
| Encrypted traffic only | Buy a signature IDS and expect host names |
| Small team | Deploy five consoles nobody opens |
| Production change window | Enable IPS blocking without a count phase |
| Shared IXP port | Send unsolicited ARP or routing changes |
| Cloud only | Assume VPC flow logs have packet content |

## Install notes

Most tools are package manager or container installs. Keep them off the
management network. For a lab, Docker with `--network none` works for offline
analysis. For production, a tap or span port, a dedicated capture NIC and a
separate management address.

## Sources

The tool behavior claims come from the project docs linked in
`network-visibility.md`, `network-protection.md` and `bgp-security.md`.
