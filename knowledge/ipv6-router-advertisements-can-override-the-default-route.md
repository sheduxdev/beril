---
id: ipv6-router-advertisements-can-override-the-default-route
title: IPv6 router advertisements can override the default route
tags: network, ipv6, ra
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/network-visibility.md
status: active
---
# IPv6 router advertisements can override the default route

## Claim

A rogue RA can add a default route or a prefix and move traffic through the attacker host.

## Test

Capture RAs on the segment. Compare the prefix and the route with the expected config. Send traffic after the RA.

## Proof

The host route points at the rogue link local address.

## Failure modes

RA guard blocks it. A static config ignores the RA.
