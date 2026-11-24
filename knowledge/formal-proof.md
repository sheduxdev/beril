---
id: formal-proof
title: A proof assistant checks every step, at a cost
tags: formal, proof, assistant
confidence: low
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A proof assistant checks every step, at a cost

## Claim

The tool verifies the proof term. The cost is the model, the lemmas and the maintenance.

## Test

Prove a small function. Change the spec. Check what breaks.

## Proof

A checked proof that survives a spec change or a list of broken lemmas.

## Failure modes

A proof of the wrong model is worse than no proof. Maintenance tracks the code.
