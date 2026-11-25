---
id: map-the-technique-not-the-tool
title: Map the technique, not the tool
tags: detection, attack, mapping
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/detection-lolbins.md
status: active
---
# Map the technique, not the tool

## Claim

A rule for one binary name dies when the actor renames it. The technique and the parent child relation survive.

## Test

Map the behavior to an ATT&CK technique. Remove the tool name from the logic. Run both a renamed and a normal sample.

## Proof

The rule fires on the renamed binary.

## Failure modes

A generic technique can be noisy. A unique command line can justify the tool name.
