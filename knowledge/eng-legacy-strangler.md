---
id: eng-legacy-strangler
title: Do not rewrite the legacy system; strangle it
tags: engineering, legacy, refactor
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Do not rewrite the legacy system; strangle it

## Claim

A seam, a wrapper and a behavior-by-behavior move keep the old path alive until the new one is proven.

## Test

Find a seam. Add a facade. Move one behavior. Compare outputs.

## Proof

One behavior on the new path with the old path still available.

## Failure modes

A big-bang rewrite loses the edge cases the old code encodes.
