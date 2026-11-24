---
id: data-normalization
title: Normalize for writes, denormalize for reads, and name the owner
tags: data-modeling, normalization, read-model
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Normalize for writes, denormalize for reads, and name the owner

## Claim

Normal form removes update anomalies. A read model duplicates data with a rebuild path.

## Test

Update a duplicated field. Check the source and the read model.

## Proof

A read model rebuilt from the source without drift.

## Failure modes

A denormalized field without a rebuild job drifts. A join-heavy schema at scale stalls.
