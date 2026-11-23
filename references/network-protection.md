# Network protection

This note lists controls that reduce blast radius and the tests that show
whether a control actually works. A control that has never been tested is a
diagram.

## 1. Segmentation

CISA's 2025 microsegmentation guidance defines segmentation as dividing a network
so each segment acts as its own network with access control. It calls
microsegmentation a step beyond VLANs: policy follows the resource, not the
address. The guidance also says to study how a segment can be bypassed, so the
bypass can be monitored when it cannot be blocked.

The IT/OT advisory is concrete: standard IT users could reach a SCADA VLAN over
port 21. The recommended design is default deny between IT and OT, a DMZ, a
bastion, ACLs and application aware firewalls. A full redesign is on the table
when VLANs cannot separate the two.

Test:

- From a user VLAN, `nc -vz <ot-host> 21 22 80 443 502`.
- From the OT VLAN, test back to user and server subnets.
- Check whether a compromised host can reach the management VLAN.
- Try a direct route around the firewall, such as a dual-homed host.

Failure modes: any-any rules left after a migration, a second path through a
lab switch, a hypervisor network that bypasses the firewall, and a bastion that
allows arbitrary outbound traffic.

## 2. Default deny and egress control

CISA's communications guidance asks for a strict default-deny ACL, logging of
denied traffic, and separate devices for separate controls. Egress matters as
much as ingress: most command and control is outbound.

A usable egress policy allows named destinations and protocols, not "internet
for servers". Break-glass rules need an owner and an expiry.

Test:

- `curl` to a random host from a server VLAN.
- DNS to an external resolver from a workstation.
- SSH from a server to the internet.
- Denied traffic appears in the log with source, destination and rule.

## 3. Management plane

Rules from CISA and MITRE D3FEND:

- Out-of-band management network, physically separate.
- No management from the internet.
- A dedicated admin workstation.
- No lateral management between devices.
- ACL on VTY lines.
- Disable discovery protocols where unused.
- SSH v2 only, SNMPv3 with auth and encryption.
- AAA to a central server, local accounts only for emergencies.

Test: from a normal workstation, try SSH and HTTPS to a switch. From one switch,
try to reach the neighbour. Check `show run | include transport input`,
`snmp-server`, and the ACL on VTY.

## 4. DMZ and exposed services

Externally reachable DNS, web and mail belong in a DMZ. The DMZ holds shared
services that both sides need, with tight rules and monitoring. The internal
network reaches the DMZ, not the reverse, except for replies.

Test: from the internet, enumerate the DMZ ports. From the DMZ, test the
internal database port. Confirm that a DMZ compromise does not give a direct
shell to the LAN.

## 5. Zero trust and policy enforcement

NIST SP 800-207 and CISA's microsegmentation guidance put a policy enforcement
point in front of a resource and a policy decision point behind it. Access is
granted per session, on identity and device state, not on network location.

Practical start:

- Put a proxy or ZTNA in front of one admin service.
- Require device posture and phishing resistant MFA.
- Log every decision with the policy ID.
- Keep a direct path as break-glass.

Test: remove the device from compliance and confirm the session is denied. Change
the user group and confirm the next request is re-evaluated.

## 6. DDoS

Cloudflare lists three attack layers: volumetric, protocol and application. Its
mitigation list is rate limiting, WAF, anycast diffusion and blackhole routing.

- Rate limiting at the edge absorbs floods that reach the application.
- A WAF filters HTTP patterns, not raw packet floods.
- Anycast spreads traffic across capacity.
- Blackhole drops everything to one address. It keeps the link alive and hides
  the service.

Test in a lab: `hping3 --flood`, `wrk`, and a slow POST test. Confirm the edge
rule fires and that the origin still answers through the CDN.

## 7. WAF

AWS WAF is a layer 7 filter in front of CloudFront, API Gateway, ALB, AppSync,
Cognito and similar. It allows, blocks with 403 or returns a custom response,
based on IP, headers, body and rate.

A WAF is not a patch. Tune it like an IDS:

- Start in count mode.
- Review every managed rule that fires on real traffic.
- Add app specific rules for the endpoints that break generic rules.
- Keep logs long enough to investigate.
- Test with the same requests the scanner uses.

## 8. DNS protection

Controls:

- DNSSEC signing and validation where the zone supports it.
- Redundant authoritative servers and over-provisioned capacity.
- A DNS firewall or resolver with rate limiting and malware filtering.
- Controlled resolvers, with DoH or DoT to the resolver when privacy needs it.
- Zone change monitoring and registry lock.

DoH and DoT encrypt the query to the resolver. They also remove the query from
the network sensor. Keep endpoint telemetry or force a controlled resolver if
network DNS visibility matters.

Test: `dig +dnssec`, check the AD bit, query a known malware domain from a
client, and change a record in staging to confirm alerting.

## 9. TLS and ECH

CISA asks for TLS 1.3 and strong cipher suites on management protocols. ECH
encrypts the ClientHello, including SNI, so a passive sensor sees the fronting
provider, not the real origin. Cloudflare describes the outer and inner
ClientHello and the DoH dependency for the key.

Compensations:

- JA4 and certificate fields.
- Endpoint DNS and TLS logs.
- eBPF socket and process telemetry.
- A TLS inspection proxy where policy allows it, with the privacy cost noted.

Test: `openssl s_client -connect host:443 -tls1_3 -servername host` and check
the negotiated version. Compare what the sensor sees for an ECH host against
what the endpoint reports.

## 10. Email

CISA's CPG 2.M is direct: STARTTLS, SPF, DKIM and DMARC at `p=reject`. Add
lookalike domain monitoring and a payment change call-back process.

Test: send from an unauthorized sender, check the DMARC result, and try a
display-name spoof. Confirm `p=reject` and that the mail gateway quarantines.

## 11. Backups and recovery

CISA CPG 2.R asks for regular backups, stored separately and tested. For
ransomware, the test is restore, not backup completion.

Test: restore one service to a clean segment, measure the time, and confirm the
backup host is not reachable with the production admin credentials.

## 12. Patch velocity

CISA CPG 1.E gives KEV entries in internet-facing systems a risk-informed
deadline. The practical version: a weekly KEV diff, an owner per asset, and a
compensating control recorded when patching breaks availability.

## 13. Logging and time

Without synchronized time, correlation fails. Without protected logs, the
attacker deletes the story. CISA asks for central log storage, encrypted
transport and off-site copies. CPG 2.T and 2.U add alerting when a critical
source stops and access control on the store.

Test: stop a log source deliberately and confirm the alert. Try to delete an
index as a normal analyst. Check NTP offset on a sample of devices.

## 14. What to measure

- Percentage of assets with an owner and a current config record.
- Denied egress attempts per day, and how many were reviewed.
- Mean time from KEV publication to mitigation on exposed assets.
- Segmentation test results per quarter, with the path and the date.
- Restore test result per service per year.
- False positive rate per detection rule.

## Sources

- CISA, Journey to Zero Trust: Microsegmentation, Part One, 2025: https://www.cisa.gov/sites/default/files/2025-07/ZT-Microsegmentation-Guidance-Part-One_508c.pdf
- CISA joint advisory on IT/OT segmentation, 2025: https://www.cisa.gov/sites/default/files/2025-08/joint-advisory-cisa-identifies-areas-for-cyber-hygiene-improvement-after-conducting-proactive-threat-hunt-508c.pdf
- CISA CPGs: https://www.cisa.gov/cybersecurity-performance-goals-cpgs
- CISA, Enhanced Visibility and Hardening Guidance, 2024: https://www.cisa.gov/resources-tools/resources/enhanced-visibility-and-hardening-guidance-communications-infrastructure
- MITRE D3FEND, Network Isolation: https://d3fend.mitre.org/technique/d3f:NetworkIsolation/
- Cloudflare, What is a DDoS attack: https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/
- Cloudflare, DNS security: https://www.cloudflare.com/learning/dns/dns-security/
- AWS WAF: https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html
- Cloudflare, ECH: https://blog.cloudflare.com/encrypted-client-hello/
- RFC 8484: https://www.rfc-editor.org/rfc/rfc8484.html
