# Network defense checklist

Run this quarterly. Each row has a test and an evidence line. A row marked done
without evidence is a wish.

Scope: one site or one cloud account per pass. Record the date, the tester and
the asset group. Anything not tested stays open.

Legend: A = asset, P = passive check, T = active test.

## Inventory and architecture

| ID | Control | Test | Evidence | Common false positive |
|---|---|---|---|---|
| N01 | Asset inventory with owner | Sample 10 IPs from DHCP and DNS, find the owner | IPAM export, owner column | A lab device without a ticket |
| N02 | Current network diagram | Compare the diagram with LLDP and routing | Diagram date, diff list | A decommissioned link still drawn |
| N03 | VLAN map matches policy | Dump VLANs from switches, compare | `show vlan brief` per switch | Voice VLAN shared with PCs |
| N04 | No flat server and user subnet | Traceroute from a user host to a server | Traceroute path | A routed path that still crosses a firewall |
| N05 | IT and OT separated | Scan OT ports from an IT workstation | `nc` output, port list | A vendor jump host |
| N06 | Management network out of band | SSH to a switch from a user host | Result, source VLAN | Console server on the data VLAN |
| N07 | No management from the internet | Shodan or external scan of the management range | External scan result | A VPN portal on 443 |
| N08 | DHCP and DNS inventory joined | Query an IP, resolve the name and lease | Join output | Static IP outside IPAM |

## Filtering and segmentation

| ID | Control | Test | Evidence | Common false positive |
|---|---|---|---|---|
| N09 | Default deny inbound | External port scan of one host | Scan output, rule counter | A CDN range |
| N10 | Default deny egress | `curl` a random host from a server | Result, deny log | A proxy that allows it |
| N11 | Denied traffic logged | Trigger a deny, search the log | Log line with rule ID | Sampling hides it |
| N12 | Inter-VLAN ACL reviewed | Read the ACL, list unused rules | ACL snapshot, age | A temporary rule with no expiry |
| N13 | DMZ between tiers | Trace from DMZ to the database | Path, open port | A shared monitoring subnet |
| N14 | No dual-homed bypass | List hosts with two NICs in different VLANs | Host list, routes | A backup NIC that is down |
| N15 | Cloud security groups least privilege | Read groups, flag 0.0.0.0/0 on admin ports | Group JSON | A load balancer group |
| N16 | Kubernetes network policy | List namespaces without a policy | `kubectl get networkpolicy -A` | A CNI that ignores policy |
| N17 | Break-glass path documented | Find the path, test it, check expiry | Path note, date | A permanent any-any rule |

## Management and identity

| ID | Control | Test | Evidence | Common false positive |
|---|---|---|---|---|
| N18 | SSH v2 only | `ssh -1` or `nmap --script ssh2-enum-algos` | Version and algorithm list | A legacy appliance |
| N19 | No Telnet or FTP | `nc -vz host 23 21` | Result | An isolated lab device |
| N20 | SNMPv3 with auth and privacy | `snmpwalk -v3` with and without creds | Output | A read-only v2c collector |
| N21 | AAA central, local only for break-glass | Read the config, count local users | Config excerpt | An emergency account in a safe |
| N22 | VTY ACL | Try SSH from an unapproved subnet | Result | A jump host in the allowed range |
| N23 | Discovery protocols limited | Check CDP/LLDP on edge ports | Interface config | Phone ports that need LLDP |
| N24 | Phishing resistant MFA on admin | Try a password-only login | Result, policy ID | A console port |
| N25 | Separate admin and user accounts | Read group membership | Member list | A shared on-call account |
| N26 | Unique credentials per device | Compare password hashes or vault entries | Vault report | A vendor default in staging |

## Detection and logging

| ID | Control | Test | Evidence | Common false positive |
|---|---|---|---|---|
| N27 | Flow export at border and tiers | Query the collector for a known flow | Flow record | Sampling or a missing exporter |
| N28 | DNS query logging | Resolve a canary name, find the log | Log line with client IP | DoH to an external resolver |
| N29 | IDS sensor sees both directions | Generate a test alert, check the packet count | Alert with both directions | A one-way tap |
| N30 | Sensor loss monitored | Read `capture_loss.log` or the equivalent | Graph | A quiet link |
| N31 | Time sync | `chronyc tracking` on a sample | Offset | A device that refuses NTP |
| N32 | Central log store, access controlled | Try to delete an index as an analyst | Result | A retention job |
| N33 | Critical source down alert | Stop a source for 10 minutes | Alert | A scheduled reboot |
| N34 | Honeypot in a server VLAN | Connect to it, check the event | Event JSON, source IP | A scanner |
| N35 | Alert has an owner and a runbook | Open the top five rules | Owner column | A rule owned by a team, not a person |
| N36 | False positive review | Pull one week of alerts, count duplicates | Tuning note | A seasonal scan |

## Edge and service protection

| ID | Control | Test | Evidence | Common false positive |
|---|---|---|---|---|
| N37 | Rate limit on auth and search | Send a small burst | 429 and edge rule ID | A load test window |
| N38 | WAF in count then block | Replay a benign and a known bad request | Rule log, block page | A managed rule on a JSON body |
| N39 | DDoS runbook with contacts | Read it, call the contact in a drill | Drill note | An upstream that handles it |
| N40 | TLS 1.3 and strong ciphers | `openssl s_client -tls1_3` | Negotiated version | A legacy client that needs 1.2 |
| N41 | DNSSEC on the zone | `dig +dnssec`, check the AD bit | Output | A validating resolver that strips it |
| N42 | SPF, DKIM, DMARC reject | Send a forged message | Header, DMARC result | A mailing list that rewrites |
| N43 | security.txt | `curl /.well-known/security.txt` | Content, expiry | A redirect to a stale page |
| N44 | No admin panel on the internet | External scan of admin paths | Result | A VPN only panel |

## Recovery

| ID | Control | Test | Evidence | Common false positive |
|---|---|---|---|---|
| N45 | Backup stored off the production trust zone | Read the path and credentials | Path, account | A second disk in the same host |
| N46 | Restore test | Restore one service, measure time | Run book, timing | A database replica mistaken for a backup |
| N47 | Backup host not reachable with prod admin | Try the admin credential | Result | A shared domain admin |
| N48 | KEV patch clock | Compare KEV with the exposed asset list | Diff, owner, date | An asset behind a compensating control |
| N49 | Emergency change process | Read the process, find the approval | Ticket example | A direct push by an admin |
| N50 | Incident contact list current | Call two contacts | Call log | A shared mailbox |

## Scoring

Count only rows with evidence. Report the percentage per section. A section
under 50 percent is the next quarter's project. Do not average sections into one
number, because a strong backup score hides a flat network.

## Stop conditions

- The tester loses access and cannot recover it.
- A test needs a production restart.
- The firewall rule change cannot be rolled back.
- A cloud account is shared with another team.

## Sources

The controls synthesize CISA CPGs, CISA microsegmentation guidance, CISA
communications hardening, NIST SP 800-94 and SP 800-61r3, and MITRE D3FEND.
Links are in `network-protection.md` and `network-visibility.md`.
