# Capability gap map

This is a self-assessment, not a roadmap promise. It lists what Beril covers,
what it covers thinly and what it lacks in the network and infrastructure
domain. The point is to pick the next training block from evidence.

Status: C = covered, P = partial, M = missing.

## Routing

| Area | Status | Current artifact | Gap | Next |
|---|---|---|---|---|
| BGP threats and controls | C | `references/bgp-security.md`, `scripts/bgp.py` | No route collector feed | Add BMP lab |
| RPKI | P | ROA and ROV procedure | No validator integration | `beril bgp --prefix` with RIPEstat |
| IRR and PeeringDB | P | Lookup workflow | Manual | Contact and object checklist |
| Route leak detection | P | BMP and ARTEMIS section | No feed | Lab with ExaBGP |
| Looking glass and collectors | C | HE, bgp.tools, RIS | No parser | Export a prefix snapshot |
| BGP session hardening | C | RFC 7454 checklist | No config parser | Sample configs per vendor |

## Network visibility

| Area | Status | Current artifact | Gap | Next |
|---|---|---|---|---|
| Flow analysis | P | Method and limits | No nfdump query set | A flow baseline script |
| Packet capture | P | Retention and privacy | No pcap triage | `scripts/pcap_summary.py` |
| DNS telemetry | P | Signals and limits | No dnstap lab | Local resolver lab |
| IDS tuning | P | Sigma basics | No rule test harness | Small Sigma repo |
| Honeypots | P | Cowrie rules | No deployment | Docker Cowrie lab |
| eBPF | P | Tetragon overview | No lab | Tetragon on kind |
| NDR metrics | M | None | Beacon scoring | RITA lab with public pcap |

## Protection

| Area | Status | Current artifact | Gap | Next |
|---|---|---|---|---|
| Segmentation | C | 50 control checklist | No config parser | Lab with nftables zones |
| Egress control | C | Default deny procedure | No baseline | Egress allowlist lab |
| Management plane | C | Out-of-band and AAA | No vendor examples | Cisco and Juniper excerpts |
| DDoS | P | Layers and mitigations | No drill | Edge rule drill |
| WAF tuning | P | Count then block | No rule set | CRS lab |
| DNS protection | P | DNSSEC and firewall | No zone lab | BIND and Knot lab |
| TLS and ECH | P | Test and compensation | No measurement | Local ECH measurement |
| Email | C | SPF, DKIM, DMARC | No mail server lab | Mailcow lab |
| VPN and ZTNA | M | None | Whole area | WireGuard and Pomerium lab |
| Cloud network | M | None | VPC, TGW, security groups | AWS VPC lab with Terraform |
| Kubernetes network | M | None | CNI and policy | kind plus Cilium lab |
| IPv6 | M | Only filter notes | RA, ND, transition | IPv6 segment lab |
| Wireless | M | None | WPA2/3, rogue AP, EAP | Hostapd lab |
| OT and ICS | M | Only IT/OT advisory | Modbus, Purdue, DNP3 | OpenPLC lab |
| PKI and ACME | M | None | CA, revocation, pinning | step-ca lab |
| Time sync | P | One checklist row | NTP attacks | Chrony lab |
| Backups | C | Restore test | No sample | Restore drill |

## Tooling and automation

| Area | Status | Gap | Next |
|---|---|---|---|
| BGP lookup command | C | `beril bgp` passive lookup | Add validator drift alarm |
| Pcap summary | M | No command | Protocol and top talker summary |
| NetFlow summary | M | No command | nfdump wrapper |
| Config diff | P | `patch_diff.sh` is binary only | Text config diff mode |
| SBOM and deps | C | None | Keep current |
| Network dashboard | M | Dashboard has no network page | Prefix and flow card |
| Sigma rules | M | No generator | Rule skeleton command |

## Reading and training

| Area | Status | Gap | Next |
|---|---|---|---|
| Source list | C | 16 network sources added | Keep fresh |
| Research log | C | Confidence and gaps | Add a new log per block |
| Four-week track | C | Weeks 1 to 4 | Add weeks 5 to 8 |
| BGP track | P | Runbook only | Add BGP lab week |
| Measurement | M | No scored exercise | Add a rule tuning score |

## Priority

### Now

1. BGP lookup is done. Add a validator drift alarm.
2. Pcap summary command, no external dependency.
3. Egress and segmentation lab with nftables.
4. Weeks 5 to 8: BGP, IPv6, cloud VPC, wireless.

### Next

5. Kubernetes network policy lab.
6. OT lab with Modbus and a Purdue zone map.
7. PKI lab with step-ca and revocation.
8. Sigma rule test harness.
9. Dashboard network page.

### Later

10. NDR beacon scoring.
11. RPKI validator integration and drift alarm.
12. IPv6 transition and RA guard.

## What not to build

- A full BGP daemon. ExaBGP and Routinator already exist.
- A packet capture engine. tcpdump and Zeek exist.
- A vulnerability scanner for network devices. Nuclei and vendor advisories
  exist.
- A cloud CSPM. The cloud provider and Steampipe exist.

## How to pick the next block

Take the highest priority row that has a lab you can build in a day. Write the
lab, the test and the note before starting. If the lab needs hardware you do not
have, move to the next row.

## Sources

The gaps are inferred from the current repository, not from a market study.
Coverage claims are checked against the files named in the table.
