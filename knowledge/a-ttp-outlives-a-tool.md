---
id: a-ttp-outlives-a-tool
title: A TTP outlives a tool
tags: ti, ttp, attack
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/detection-threatintel.md
status: active
---
# A TTP outlives a tool

## Claim

An actor changes the binary, not the behavior. The technique and the parent child relation survive a rebuild.

## Test

Map the behavior to ATT&CK. Remove the tool name. Check the rule on a renamed sample.

## Proof

A detection that fires on the behavior without the name.

## Failure modes

A generic behavior is noisy. A unique command line is a tool signature.
