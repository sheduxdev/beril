---
id: eng-event-sourcing
title: Events are the source of truth, state is a projection
tags: engineering, event-sourcing, events
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Events are the source of truth, state is a projection

## Claim

Append-only events rebuild state. Schema evolution and replay are the hard parts.

## Test

Replay a stream into a new projection. Compare it with the current state.

## Proof

A rebuilt projection that matches.

## Failure modes

An event schema change breaks old replays. A snapshot hides the cost.
