---
id: eng-ml-systems
title: Training and serving must share the same features
tags: engineering, ml, features
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Training and serving must share the same features

## Claim

A feature computed differently in training and serving creates skew. A model is only as good as its pipeline.

## Test

Log the serving features. Recompute them offline. Compare distributions.

## Proof

A feature parity check in CI.

## Failure modes

A model metric without a pipeline check is a demo.
