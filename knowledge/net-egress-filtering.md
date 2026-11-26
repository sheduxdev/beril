---
id: net-egress-filtering
title: Egress filtering is allowlist outbound, deny and log the rest
tags: net, egress, c2, exfiltration
confidence: high
updated: 2026-11-26
uses: 0
sources: https://attack.mitre.org/mitigations/M1037/, https://isc.sans.edu/diary/18379, https://attack.mitre.org/techniques/T1071/
status: active
---
# Egress filtering is allowlist outbound, deny and log the rest

## Claim

C2 and exfiltration hide in permitted outbound traffic over 443, 53 and cloud APIs. Enumerating bad destinations lags; allowing known-good egress per host and denying the rest removes most channels.

## Test

For each server, list the destinations and protocols it legitimately needs. Write a per-host outbound stanza that permits those and ends in deny-and-log. Watch the logs for what hits the deny line.

## Proof

A beacon or data transfer blocked at the deny line, with the normal app still working, from a host that had no business reaching that destination.

## Failure modes

DNS to any resolver is a tunnel; force internal or protective resolvers. Allowing all 443 outbound from servers defeats the control. Not logging the deny line means you never learn what you stopped.
