---
id: detection-lolbins
title: LOLBins hide in parent-child and arguments
tags: detection, lolbins, process
confidence: high
updated: 2026-11-24
uses: 0
sources: labs/detection
status: active
---
# LOLBins hide in parent-child and arguments

## Claim

A signed system binary runs with unusual arguments or an unusual parent, avoiding a malware signature.

## Test

Map binaries, parents and arguments. Baseline the environment. Alert on the combination, not the name.

## Proof

A rule that catches the chain and not normal admin use.

## Failure modes

A binary name rule is weak. An argument-only rule is noisy.
