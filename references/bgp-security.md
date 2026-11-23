# BGP security

BGP carries the route table of the Internet and trusts announcements by
default. An AS that announces a prefix it does not own can attract the traffic.
An AS that leaks a full table to a peer can overload it. Both happen by accident
more often than by attack, so the controls must work for mistakes too.

Sources are linked at the end. Numbers and protocol behavior below come from
those sources.

## Threats

| Threat | What happens | Covered by |
|---|---|---|
| Exact prefix hijack | A false origin announces your prefix | RPKI ROV, IRR filters |
| Sub-prefix hijack | A more specific is announced, longest match wins | RPKI maxLength, filters, monitoring |
| Squatting | A false origin announces a prefix you plan to use | RPKI, de-bogon, monitoring |
| Route leak | A customer or peer re-announces routes it should not | AS path filters, communities, monitoring |
| AS in the middle | A false AS path attracts traffic | BGPsec (limited), monitoring, RPKI is not enough |
| Session spoofing | A TCP reset or injection breaks or alters the session | GTSM, TCP-AO, control-plane ACL |
| Blackhole abuse | An attacker adds BLACKHOLE to steer traffic into a drop | Strict prefix filters, RPKI |
| RPKI repository attack | A forged or removed object flips a route to invalid | Multiple validators, monitoring, manual override |
| Spoofed source flood | Reflection and amplification with forged sources | BCP 38, uRPF, SAV |

RFC 6811 is explicit about two limits: origin validation only checks the origin
AS, and an attacker can prepend the valid origin to a forged path. It calls the
mechanism protection against misconfiguration more than strong security. Treat
it that way.

## Controls

### 1. Sign your own resources

Create a ROA for every prefix you originate, with the correct origin AS and a
maxLength that allows only the more specifics you really announce. MANRS asks
for ROAs on at least 90% of prefixes, or IRR objects as the alternative.

Test:

```bash
# Beril passive lookup with RPKI state and two collector links
./beril bgp --prefix 203.0.113.0/24

# Routinator as a local validator
routinator vrps --format json | jq '.[] | select(.asn == 64500)'
```

The expected state is `valid`. A `not-found` is a missing ROA. An `invalid` is a
wrong origin or a maxLength that is too short.

### 2. Validate what you receive

Run a validator such as Routinator or rpki-client, feed the result to the router
over RTR, and set a policy:

- Valid: accept.
- NotFound: accept with lower preference.
- Invalid: reject, and log the count.

RFC 7454 recommends exactly that order. Invalid rejection is a denial of service
risk if the validator or repository is wrong, so keep a break-glass policy and
watch the invalid counter.

### 3. Filter prefixes and AS paths

RFC 7454 is the operations reference:

- Filter special-purpose and unallocated space, and prefixes longer than the
  agreed limit (/24 IPv4, /48 IPv6 is common practice).
- With customers, accept only their registered prefixes. With peers, accept only
  their own and their customers' prefixes.
- Reject private AS numbers except from customers, reject your own AS in the
  path, and check that the first AS is the peer (route servers excepted).
- Scrub communities you own; keep no-export and other communities intact.
- Set max-prefix limits with a warning threshold below the hard limit.
- Use next-hop-self on IXP peerings unless a route server is intended.

Build filters from IRR objects and refresh daily. RFC 7454 warns that a stale
filter is worse than no filter.

### 4. Protect the session

- Control-plane ACL: only known neighbors to TCP 179, rate limited.
- GTSM (RFC 5082): TTL 255 on directly connected sessions, check on receive.
- TCP-AO where both sides support it; MD5 is the fallback.
- Disable proxy ARP and ICMP redirects on peering interfaces where appropriate.
- Put the route reflector and border routers on the management network.

### 5. Stop spoofed sources

BCP 38 ingress filtering at the edge, strict uRPF where routing is simple, and
the CAIDA Spoofer test to prove it. MANRS requires the test on two segments and
publication of the result.

### 6. Control blackholes

Use the BLACKHOLE community (0xFFFF029A) only with peers that agreed to honor
it. Announce the longest possible prefix (/32 or /128), keep it inside the local
AS with NO_EXPORT, and make sure RPKI does not mark the blackhole invalid. RFC
7999 also warns that a forged blackhole is a reachability attack.

### 7. Monitor the control plane

- BMP (RFC 7854) gives you the Adj-RIB-In and updates from the router. It is
  read-only from the router side and uses TCP.
- Route collectors such as RIPE RIS and RouteViews give an outside view.
- BGPalerter, ARTEMIS and bgp.tools monitoring alert on new origin, new path,
  more specifics and withdrawals.
- The Hurricane Electric BGP Toolkit and bgp.tools are quick public lookups for
  an ASN, prefix, bogon or RPKI state.

## Public lookup workflow

For a prefix you own, or one you are checking:

1. `https://bgp.he.net/net/203.0.113.0/24` for announcements, origin and
   upstreams.
2. `https://bgp.tools/prefix/203.0.113.0/24` for a second collector and RPKI
   state.
3. `https://stat.ripe.net/` for RIS, routing status and RPKI validity.
4. `https://www.peeringdb.com/asn/64500` for the NOC contact.
5. Your own looking glass and BMP feed.

Two independent collectors are the minimum before calling a hijack. A single
looking glass can be stale or filtered.

## Incident runbook: suspected hijack

1. Confirm on two collectors and your own BMP. Record prefix, false origin,
   first seen, upstream and path.
2. Check RPKI validity. An `invalid` with a valid ROA is strong evidence.
3. Check IRR route objects and PeeringDB for the origin.
4. Find the contact: PeeringDB NOC, RIR abuse contact, WHOIS.
5. Mitigate if the traffic is real:
   - Announce a more specific from your own AS if policy allows.
   - Ask the upstream to filter the false origin.
   - Use an RTBH only if the prefix is under DDoS and reachability is already
     lost.
   - Add a prefix filter or RPKI maxLength fix for the future.
6. Write the timeline and the collector URLs. Keep the BMP or RIS data.
7. Review why monitoring did not alert earlier.

## Tests for your own AS

| Test | Pass |
|---|---|
| ROA coverage | 100% of originated prefixes, correct maxLength |
| Invalid route count | Stable, with a named owner |
| IRR objects | All prefixes and origin AS registered |
| Prefix filters | Generated, dated, refreshed daily |
| Max-prefix | Warning and hard limit set per peer |
| GTSM | Enabled on direct peers |
| Control-plane ACL | Only neighbors to 179, rate limited |
| uRPF or SAV | Enabled at edges, CAIDA result published |
| BMP or collector | Feed up, alerts routed to a person |
| PeeringDB | NOC and abuse contacts current |
| Looking glass | Working and not leaking policy |

## Limits

- RPKI does not protect the path. BGPsec is the path answer and has low
  deployment.
- RPKI depends on RIRs and repositories. A bad object can take a prefix offline.
- IRR data is often stale or wrong. Strict filters need an exception process.
- Public collectors sample and filter. Absence of a route is not proof.
- A blackhole hides the service while it protects the link.
- BGP monitoring is read-only. It does not replace prefix filters.

## Sources

- RFC 7454, BGP Operations and Security: https://www.rfc-editor.org/rfc/rfc7454.html
- RFC 6811, BGP Prefix Origin Validation: https://www.rfc-editor.org/rfc/rfc6811.html
- RFC 6480, RPKI architecture: https://www.rfc-editor.org/rfc/rfc6480.html
- RFC 7854, BGP Monitoring Protocol: https://www.rfc-editor.org/rfc/rfc7854.html
- RFC 7999, BLACKHOLE community: https://www.rfc-editor.org/rfc/rfc7999.html
- NIST SP 800-189, Resilient Interdomain Traffic Exchange: https://csrc.nist.gov/pubs/sp/800/189/final
- MANRS network operator actions: https://manrs.org/netops/actions/
- MANRS Observatory: https://observatory.manrs.org/
- Hurricane Electric BGP Toolkit: https://bgp.he.net/
- bgp.tools: https://bgp.tools/
- Routinator: https://github.com/NLnetLabs/routinator
- ARTEMIS: https://github.com/FORTH-ICS-INSPIRE/artemis
