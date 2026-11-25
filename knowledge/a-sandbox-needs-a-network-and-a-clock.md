---
id: a-sandbox-needs-a-network-and-a-clock
title: A sandbox needs a network and a clock
tags: malware, sandbox, dynamic
confidence: high
updated: 2026-11-26
uses: 0
sources: references/reverse-engineering.md
status: active
---
# A sandbox needs a network and a clock

## Claim

A sample that waits, checks the clock or needs a network stays quiet in a bare sandbox. The environment is part of the verdict.

## Test

Run in a sandbox with a fake internet and a shifted clock. Compare with a bare run. Read the API calls and the network.

## Proof

New behavior with the clock or the network present.

## Failure modes

A sample can detect the sandbox. A long sleep needs a time shift.
