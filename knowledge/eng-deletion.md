---
id: eng-deletion
title: Deletion is a feature
tags: engineering, deletion, maintenance
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Deletion is a feature

## Claim

Dead code, flags and services are liabilities. Removal needs a check that nothing depends on it.

## Test

Find unused code. Check callers and metrics. Remove it. Watch the error rate.

## Proof

A smaller system with no regression.

## Failure modes

A flag kept for a rollback can stay forever.
