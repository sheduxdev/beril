---
id: beacon-jitter-is-measured-not-guessed
title: Beacon jitter is measured, not guessed
tags: detection, beacon, jitter
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/detection-beacon.md
status: active
---
# Beacon jitter is measured, not guessed

## Claim

A beacon is a periodic connection with a low variance. Jitter moves it, but the interval distribution still separates it from browsing.

## Test

Group connections by destination and delta. Compute the spread. Compare with a known user pattern.

## Proof

A low variance interval series with a repeating size pattern.

## Failure modes

A long sleep and high jitter hide it. A busy shared CDN adds noise.
