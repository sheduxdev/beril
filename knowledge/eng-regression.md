---
id: eng-regression
title: A bug fix needs a test that failed before it
tags: engineering, testing, regression
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A bug fix needs a test that failed before it

## Claim

The regression test proves the bug existed and the fix holds. Without it, the bug returns.

## Test

Reproduce the bug in a test. Fix it. Run the test forward and backward.

## Proof

A test that fails on the old code and passes on the new.

## Failure modes

A test that asserts the new implementation, not the behavior.
