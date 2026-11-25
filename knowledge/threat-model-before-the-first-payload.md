---
id: threat-model-before-the-first-payload
title: Threat model before the first payload
tags: senior, threat-model, method
confidence: high
updated: 2026-11-26
uses: 0
sources: references/senior-bar.md, references/techniques.md
status: active
---
# Threat model before the first payload

## Claim

A named actor, asset, boundary and missing control turn payload guessing into a test. Write the expected failure before sending.

## Test

Write one page with the path from input to boundary, the transform and the one check that would settle it. Send only the matching payload.

## Proof

A one page model and a request that tests the named boundary.

## Failure modes

Every boundary mapped is a diagram. Pick the one that matters. A model can be stale after one response.
