---
id: eng-testing-pyramid
title: Test at the lowest level that can catch the bug
tags: engineering, testing, pyramid
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Test at the lowest level that can catch the bug

## Claim

Many unit tests, fewer integration tests, a small number of end-to-end tests. The pyramid is about feedback speed.

## Test

Classify the suite. Move a slow test down a level. Keep one end-to-end happy path.

## Proof

A faster suite with the same defect detection.

## Failure modes

A test that mocks the thing under test proves little.
