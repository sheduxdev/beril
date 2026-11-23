# Network incident runbook

Use this when an alert says a host talks to something it should not, or when a
flow graph looks wrong. The goal is a correct scope in the first hour and a
containment that does not blind you.

## 0. Before touching anything

Write down:

- Time, alert source, rule ID and severity.
- Source and destination IP, port, protocol, bytes.
- Host name, owner, business role.
- What the sensor can see and what it cannot.
- Who is the incident commander.

Do not reboot the host. Do not delete the container. Do not reset the switch.

## 1. Validate the alert

Three quick checks:

1. Is the rule known noisy? Read its false positive note and last tuning date.
2. Does the flow repeat? One connection is weak. A fixed interval is strong.
3. Does another source agree? DNS, proxy, EDR, authentication, DHCP.

If all three are negative and the rule is `low`, log and move on. If one is
positive, continue.

## 2. Scope with flow and DNS

Query flows for:

- The suspect IP in both directions over 7 days.
- The suspect host to any external address, grouped by destination and port.
- Any internal host that talked to the same destination.
- Beacon shape: interval standard deviation, bytes per connection.
- New destinations that appear only after the suspect time.

Query DNS for:

- Long labels, TXT and NULL records from the suspect host.
- Domains registered in the last 30 days.
- The resolver used, and whether the host bypasses it.

Query identity for:

- Logins from the host, service accounts used, new sessions.
- VPN and SSO events for the owner in the same window.

## 3. Classify

| Pattern | Likely | Next |
|---|---|---|
| Fixed interval, small bytes, one destination | Beacon | Pull the process, check persistence |
| Long encoded DNS labels | DNS tunnel | Capture DNS, decode a sample |
| Many destinations, one port | Scan or worm | Check SMB, RDP, SSH logs |
| Huge outbound bytes to one host | Exfil | Check proxy and file access logs |
| SYN flood from many sources | DDoS | Edge runbook, not host triage |
| New external destination from a server | Update or C2 | Compare with change log |
| Auth success from a new country | Session theft | Revoke sessions, check MFA |

## 4. Contain, in order

1. DNS sinkhole for the domain, if DNS is controlled.
2. Edge block for the destination IP and port.
3. Host isolation through EDR, keeping the management channel.
4. Disable the account or revoke sessions.
5. Remove the host from the load balancer.
6. Last resort: switch port shutdown.

Each step changes what you can still observe. Record the time of every action
and the rule or policy ID. Keep a copy of the flow and DNS data before it ages
out.

## 5. Preserve evidence

- Export the flow records and DNS answers for the window.
- Start a packet capture on the host if it is still up and the link is not
  saturated.
- Hash downloaded files before opening them.
- Copy the process tree, listening sockets and scheduled tasks.
- Note the sensor capture loss for the window.

## 6. Investigate the host

- Process tree and parent chain.
- Binary path, hash, signature, first seen.
- Listening sockets and established connections with the process ID.
- Persistence: services, cron, systemd, registry, scheduled tasks, containers.
- Credentials touched: SSH keys, cloud metadata, browser stores, config files.
- Lateral movement: SMB, RDP, WinRM, SSH, Kubernetes exec.

## 7. Eradicate and recover

- Remove persistence before reboot.
- Rebuild from a known image when the root cause is unclear.
- Rotate credentials that the host could read.
- Restore data from a backup older than the first suspicious event, then replay
  legitimate changes.
- Watch the same destination for 72 hours after recovery.

## 8. Close

- Timeline with sources.
- What the sensor missed and why.
- Rule changes, with a new false positive note.
- Segmentation or egress change that would have limited it.
- Owner and due date for each action.

## 9. Small network version

Without a SIEM:

- Firewall log to a syslog host, 30 days.
- Router flow export if it supports it.
- Pi-hole or Unbound query log.
- `tcpdump -i any -s 128 -w case.pcap` on the suspect host, time boxed.
- A paper timeline.

## Stop conditions

- The host is a hypervisor or a domain controller. Get a second pair of eyes.
- Containment would stop a production line. Agree a window first.
- The attacker is active in the management plane. Do not use the management
  network for triage until you know how.
- The evidence store is full. Free space before capturing more.

## Sources

- NIST SP 800-61r3: https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r3.pdf
- SANS Incident Handler's Handbook: https://www.sans.org/white-papers/33901
- SANS, Shedding Light on Security Incidents Using Network Flows: https://www.giac.org/paper/gcih/1241/shedding-light-security-incidents-network-flows/102204
- CISA, Enhanced Visibility and Hardening Guidance: https://www.cisa.gov/resources-tools/resources/enhanced-visibility-and-hardening-guidance-communications-infrastructure
