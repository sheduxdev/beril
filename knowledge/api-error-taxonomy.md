---
id: api-error-taxonomy
title: An error names whether the caller may retry
tags: api-design, errors, retry
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# An error names whether the caller may retry

## Claim

A stable code, a retryable flag and a machine-readable body let the client decide without parsing prose.

## Test

Trigger a validation error, a conflict and a rate limit. Check the codes and the retry hint.

## Proof

A client that retries only the retryable classes.

## Failure modes

A 500 for a validation error retries forever. A prose message cannot be branched on.
