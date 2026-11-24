---
id: test-chaos-suite
title: Deterministic simulation finds bugs a real cluster hides
tags: testing, simulation, determinism
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Deterministic simulation finds bugs a real cluster hides

## Claim

A simulated network with a seeded clock and scheduler replays the same interleaving. Failures become reproducible.

## Test

Run a partition scenario with a seed. Replay the seed. Compare the trace.

## Proof

A reproducible failure trace from one seed.

## Failure modes

A simulation that omits fsync proves a different system. A random seed that is not logged cannot replay.
