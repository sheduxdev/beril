---
id: eng-errors
title: An error is a value with a caller decision
tags: engineering, errors, api
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# An error is a value with a caller decision

## Claim

The caller needs to know whether to retry, fix input or alert. A generic error hides that choice.

## Test

List the failure modes. Map each to a code and a retry policy.

## Proof

A caller can decide without parsing a message.

## Failure modes

A stack trace in a user response leaks internals.
