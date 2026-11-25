---
id: a-more-specific-bgp-prefix-wins-the-route
title: A more specific BGP prefix wins the route
tags: network, bgp, hijack
confidence: high
updated: 2026-11-26
uses: 0
sources: references/network-curriculum.md, docs/bgp-runbook.md
status: active
---
# A more specific BGP prefix wins the route

## Claim

Longest prefix match sends traffic to the more specific announcement even when the origin AS is wrong.

## Test

Compare the announced prefix length with the legitimate one. Check the origin AS in the update and in a looking glass.

## Proof

The more specific route carries the traffic to the wrong origin.

## Failure modes

An RPKI invalid route can still be preferred by local policy. A provider filter can drop it.
