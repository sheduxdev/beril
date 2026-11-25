---
id: a-timeline-is-only-as-good-as-the-clock
title: A timeline is only as good as the clock
tags: ir, timeline, clock
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ir-timeline.md
status: active
---
# A timeline is only as good as the clock

## Claim

Clock skew and timezone mix ups reorder events. The timeline needs the source offset and the sync state per host.

## Test

Compare the host clock with a known source. Record offsets before merging. Flag the skewed entries.

## Proof

A timeline with offsets and a confidence note per row.

## Failure modes

A domain controller can push a wrong time. A VM snapshot can freeze the clock.
