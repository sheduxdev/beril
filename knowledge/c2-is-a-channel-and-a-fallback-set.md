---
id: c2-is-a-channel-and-a-fallback-set
title: C2 is a channel and a fallback set
tags: malware, c2, network
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/detection-beacon.md
status: active
---
# C2 is a channel and a fallback set

## Claim

A loader tries several channels and sleeps on failure. One blocked domain is not a dead sample.

## Test

Read the strings and the config. Watch DNS and TLS over a long run. Block one channel and record the next.

## Proof

A fallback channel after the first is blocked.

## Failure modes

A single channel sample has no fallback. A domain generation algorithm changes the name.
