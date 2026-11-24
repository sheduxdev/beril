---
id: detection-dns
title: DNS tunneling is a length and entropy pattern
tags: detection, dns, tunnel
confidence: medium
updated: 2026-11-25
uses: 0
sources: labs/detection
status: active
---
# DNS tunneling is a length and entropy pattern

## Claim

Long, random subdomains to one domain, high query volume, or TXT-heavy responses.

## Test

Group queries by parent domain. Measure label length, entropy and response size. Compare with a baseline.

## Proof

A domain with a repeatable anomalous pattern.

## Failure modes

A CDN or analytics domain is also long. Check the destination reputation.
