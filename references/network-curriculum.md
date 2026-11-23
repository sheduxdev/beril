# Network defense track

An eight-week self-training plan for the visibility and protection material.
Each week has a reading block, a lab, a proof and a review. Timebox: 6 hours per
week. Do the lab on a machine you own. Weeks 5 to 8 need a virtual lab and, for
week 8, a small PLC emulator.

The track uses the Beril labs for the web handoff and adds local network work
with standard tools. Nothing here scans a third party.

## Week 1: See the wire

Read:

- `references/network-visibility.md`
- NIST SP 800-94, sections on network IDPS and false positives
- Zeek log file reference, `conn.log`, `dns.log`, `http.log`, `ssl.log`

Lab:

1. Build a small virtual network: one Linux host, one client VM.
2. Run `tcpdump -i any -s 128 -w w1.pcap` on the host for 10 minutes while the
   client browses, resolves DNS and downloads a file.
3. Run `zeek -r w1.pcap` in a work directory.
4. Answer from the logs: how many DNS queries, which names, how many TLS
   handshakes, which SNI, how many bytes per flow.
5. Use `tshark -r w1.pcap -q -z io,phs` to see the protocol mix.

Proof: a one-page table with five flows, the DNS names, and one question the
capture cannot answer. `capture_loss.log` must be empty.

Review: which data source answered each question, and which one was blind.

## Week 2: Detect, then tune

Read:

- Sigma rule basics, especially `falsepositives` and `level`
- MITRE ATT&CK T1071.004 detection strategy
- `references/network-protection.md`, sections 8 to 10

Lab:

1. Write three Sigma rules: long DNS label, TXT query from a workstation, and
   outbound SSH from a server.
2. Convert them with `sigma-cli` to a query for a local backend or read them
   against the week 1 logs by hand.
3. Generate 30 benign events and 3 synthetic bad ones.
4. Measure: how many rules fire on benign traffic, and how many bad events are
   caught.
5. Add a filter and repeat. Keep the filter and the false positive note.

Proof: a table with rule, true positives, false positives and the filter. One
rule must have zero false positives after tuning without losing the bad event.

Review: what baseline would have made the rule cheaper to run.

## Week 3: Protect a segment

Read:

- CISA microsegmentation guidance, phases 1 to 4
- CISA CPG 2.F and 2.T
- MITRE D3FEND Network Isolation, DNS allowlisting and outbound filtering

Lab:

1. Create three zones: client, server, management.
2. Default deny between them. Allow DNS and one application port only.
3. Put a jump host in a DMZ. Reach the management zone only through it.
4. Log denied traffic.
5. Test from the client: DNS works, app works, SSH to management fails, direct
   internet egress fails.
6. Try to bypass with a second NIC or a NAT rule, then close the bypass.

Proof: the rule set, five test results, and the deny log line. A traceroute
showing the jump host.

Review: which bypass was easiest, and what would detect it.

## Week 4: Respond to a synthetic incident

Read:

- `docs/network-runbook.md`
- NIST SP 800-61r3, Detect and Respond functions
- SANS flow paper, the containment section

Lab:

1. Start a listener on an external VM.
2. On a lab client, run a loop that calls the listener every 30 seconds with a
   fixed payload.
3. Treat the alert as real. Scope with flows and DNS, write the timeline, and
   contain with a DNS sinkhole or an edge block.
4. Preserve the pcap and hash any file moved.
5. Write the closing note with the gap that allowed the beacon.

Proof: timeline, containment action and time, one rule or ACL change.

Review: what the sensor saw, what it missed, and how long the scope took.

## Week 5: BGP

Read:

- `references/bgp-security.md`
- RFC 7454, sections 4 to 11
- RFC 6811 and the MANRS actions

Lab:

1. Build two namespaces or VMs with ExaBGP and a route server.
2. Announce a test prefix from the wrong origin and confirm the other side sees
   it. `./beril bgp --prefix <lab-prefix>` shows the public view once announced.
3. Add an RPKI ROA with `maxLength` 24 and run Routinator locally.
4. Mark the false origin invalid and confirm the route is rejected.
5. Send a more specific /25 and confirm longest match wins.
6. Break it with a route leak and catch it with an AS path filter.

Proof: the route table before and after each step, the RPKI state, and the filter
that fixed it. `docs/bgp-runbook.md` is the incident script.

Review: which step would a public collector have missed.

## Week 6: IPv6

Read:

- RFC 7454 special-purpose and specificity sections
- Your platform's RA guard and ND documentation
- `references/network-protection.md`, section 1

Lab:

1. Build a dual-stack client and server segment.
2. Add a rogue RA and confirm the client takes the false prefix.
3. Enable RA guard and repeat.
4. Test an IPv6 prefix filter and a /64 to /48 aggregation rule.
5. Run `ndisc6` and `dig -6` checks.

Proof: the client address before and after the rogue RA, and the guard output.

Review: which IPv4 habit does not carry over.

## Week 7: Cloud network

Read:

- The provider VPC and security group documentation for one cloud
- CISA CPG 2.F and 2.W
- `references/network-protection.md`, sections 2 and 5

Lab:

1. In a free tier account, build a VPC with public and private subnets.
2. Put an app in the private subnet behind a load balancer.
3. Default deny the security groups, then allow only the load balancer.
4. Add a VPC flow log and a NAT gateway.
5. Try direct egress from the private subnet and confirm the deny.
6. Add an interface endpoint for object storage and remove the NAT path.

Proof: the security group JSON, flow log line and the failed direct path.

Review: which control is the cloud equivalent of a DMZ.

## Week 8: OT

Read:

- CISA IT/OT segmentation advisory
- Purdue model summary
- `references/network-protection.md`, section 1

Lab:

1. Run an OpenPLC or Modbus simulator in a lab VLAN.
2. From the IT VLAN, read a holding register with `mbpoll`.
3. Put a firewall between the zones and allow only TCP 502 to one host.
4. Add a read-only Modbus proxy and confirm writes fail.
5. Log the denied IT-to-OT scan.

Proof: the register read, the firewall rule and the deny log.

Review: which test could stop a production line.

## Weekly review questions

- Which evidence line would convince a skeptical peer?
- Which source was noisy, and why?
- What did the test change in the design?
- Which control failed first?

## Rules

- One site or one virtual network at a time.
- Capture before you change.
- Record the time of every action.
- Keep the pcap and the logs until the note is written.
- A clean test is not a certificate. List the parts you did not test.

## Where it connects

The web side of the same skills is in `docs/defending.md` and the Beril web lab.
The protection checklist is `references/network-checklist.md`. The incident
runbook is `docs/network-runbook.md`.
