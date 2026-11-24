---
id: eng-refactor-small
title: Refactor in small, behavior-preserving steps
tags: engineering, refactor, testing
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Refactor in small, behavior-preserving steps

## Claim

A refactor changes structure without changing behavior. A test suite proves the behavior stayed.

## Test

Name the behavior. Make one structural change. Run tests. Repeat.

## Proof

A sequence of green commits.

## Failure modes

A refactor mixed with a feature hides both.
