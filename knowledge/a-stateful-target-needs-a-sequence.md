---
id: a-stateful-target-needs-a-sequence
title: A stateful target needs a sequence
tags: fuzz, stateful, sequence
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/fuzzing.md
status: active
---
# A stateful target needs a sequence

## Claim

A protocol or a session bug needs ordered messages. A one packet harness misses the state machine.

## Test

Model the states. Generate a call sequence. Replay a shortened version after a crash.

## Proof

A minimal message sequence that reproduces.

## Failure modes

A long sequence is hard to minimize. A server with a timeout resets the state.
