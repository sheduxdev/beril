---
id: ir-timeline
title: An incident timeline needs three independent clocks
tags: ir, timeline, forensics
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# An incident timeline needs three independent clocks

## Claim

Logs, disk artifacts and memory have different times and retention. One source is not a timeline.

## Test

Collect the three sources. Normalize to UTC. Order events and mark gaps.

## Proof

A sequence with sources and confidence for each event.

## Failure modes

A file mtime can be changed. A log can be incomplete.
