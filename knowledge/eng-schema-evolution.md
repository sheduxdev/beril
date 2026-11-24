---
id: eng-schema-evolution
title: Schema changes must be compatible in both directions
tags: engineering, schema, evolution
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Schema changes must be compatible in both directions

## Claim

Old readers and new writers coexist during a deploy. Add fields as optional, never rename in one step.

## Test

Deploy old and new together. Read and write with both.

## Proof

A rolling deploy with no error.

## Failure modes

A required field added in one step breaks old readers.
