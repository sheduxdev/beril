# BGP incident runbook

Use this for a suspected hijack, route leak or unexpected path change. It
assumes you operate the affected AS and have a looking glass and a BMP feed.

## 0. Prepare before an incident

- A ROA for every originated prefix, with the right maxLength.
- Prefix and AS path filters on every external session.
- BMP or an equivalent feed to a collector you control.
- Alerts on new origin, new more-specific, path length jump and withdrawal.
- PeeringDB and RIR contacts current.
- An out-of-band channel to the NOC and to the upstream.
- A written policy for more-specific announcements and RTBH.

## 1. Confirm

A single collector is not enough. Check at least two:

- Your BMP feed or looking glass.
- RIPE RIS or RouteViews.
- Hurricane Electric BGP Toolkit or bgp.tools.

Record prefix, observed origin, first seen, collector, path and upstream. `./beril bgp --prefix <cidr>` prints the RIS view, RPKI state and two second-collector links.
Check RPKI validity for the prefix and origin. Check the IRR route object.

## 2. Classify

| Observation | Likely | Confidence |
|---|---|---|
| False origin, RPKI invalid, two collectors | Hijack | High |
| More specific from a foreign AS, no ROA coverage | Sub-prefix hijack | Medium |
| Customer announces a full table to a peer | Route leak | High if path shows it |
| Same prefix, path much longer, no origin change | Leak or traffic engineering | Medium |
| Prefix withdrawn everywhere | Session or policy failure | High |
| Only one collector shows it | Stale or filtered view | Low |

## 3. Contact

Order: PeeringDB NOC, RIR abuse contact, WHOIS, IXP contact, then the upstream.
Use email with a short subject and the evidence. Call if the traffic loss is
large and the NOC lists a phone.

Template:

```text
Subject: Prefix 203.0.113.0/24 announced by AS64501, expected AS64500

At 14:02 UTC we see 203.0.113.0/24 originated by AS64501 at RIS and bgp.tools.
RPKI state: invalid (ROA origin AS64500, maxLength 24).
Our own BMP feed confirms the path.
Can you filter the false origin or tell us who operates AS64501?

Evidence:
- RIS: <url>
- bgp.tools: <url>
- RPKI: <url>
Our NOC: <phone>
```

## 4. Mitigate

Choose the smallest action that restores reachability:

1. If you are the legitimate origin, announce a more specific from your own AS
   where policy allows. A /25 or /24+1 wins longest match.
2. Ask the upstream to filter the false origin.
3. Ask the peer or IXP to apply an RPKI invalid policy.
4. For an active DDoS on the same prefix, RTBH with the BLACKHOLE community, but
   only with peers that honor it and only on the longest prefix.
5. Do not announce a more specific of someone else's prefix unless you are
   authorized and the ROA allows it.

Record the time and the change ID of each action.

## 5. Preserve

- Export the BMP or RIS records for the window.
- Save the collector URLs and the RPKI and IRR state.
- Keep the email thread.
- Do not clear the session or reset the router before capture.

## 6. Eradicate

- Fix the filter gap that allowed the announcement.
- Fix the ROA maxLength if it was wrong.
- Add the false origin to a watch list for 30 days.
- If a customer caused a leak, add an AS path filter and a max-prefix limit.
- Review whether the more-specific policy is documented.

## 7. Recover and close

- Confirm the correct route wins on two collectors.
- Watch withdrawals and path changes for 24 hours.
- Write the timeline, the root cause and the detection gap.
- Update the runbook and the alert thresholds.

## Small operator version

Without BMP:

- A free RIPEstat and bgp.tools check, plus the upstream NOC.
- A local looking glass on the border router.
- A daily prefix report.
- A written more-specific policy.
- Two contacts per upstream, tested quarterly.

## Stop conditions

- The change would affect a live customer SLA. Confirm with the account owner.
- The route is anycast and the change may shift a region. Check the map first.
- The upstream has no 24 hour NOC. Wait for a written reply.
- RPKI state is inconsistent between validators. Do not block on one.

## Sources

- RFC 7454 and RFC 6811 in `references/bgp-security.md`.
- MANRS actions: https://manrs.org/netops/actions/
- NIST SP 800-189: https://csrc.nist.gov/pubs/sp/800/189/final
- ARTEMIS: https://github.com/FORTH-ICS-INSPIRE/artemis
