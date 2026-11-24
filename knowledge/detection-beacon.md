---
id: detection-beacon
title: A beacon is a timing pattern, not a single request
tags: detection, beacon, network
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# A beacon is a timing pattern, not a single request

## Claim

Periodic connections with jitter and a stable destination. One request looks normal; the series does not.

## Test

Group flows by destination and interval. Compute the gaps. Compare with a baseline.

## Proof

A repeatable interval or jitter pattern to the same endpoint.

## Failure modes

A CDN or update check is periodic too. Exclude known services.
