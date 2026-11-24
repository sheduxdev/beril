---
id: eng-data-model
title: Data outlives code
tags: engineering, data, schema
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Data outlives code

## Claim

Names, identifiers, relationships and events survive rewrites. A schema mistake costs more than a code mistake.

## Test

Review the schema before the API. Name the source of truth. Check constraints, nullability and deletion.

## Proof

A model that answers the next three queries without a rewrite.

## Failure modes

A flexible document can hide an unbounded shape. Flexibility is not free.
