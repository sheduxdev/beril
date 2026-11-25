---
id: integer-truncation-breaks-the-size-check
title: Integer truncation breaks the size check
tags: binary, integer, size
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/re-crash-triage-primitive.md
status: active
---
# Integer truncation breaks the size check

## Claim

A large length narrowed to 16 or 32 bits can pass a check and then allocate or copy a smaller size.

## Test

Send a length just over the type maximum. Compare the checked value with the allocation and the copy length.

## Proof

The copy writes past the allocation.

## Failure modes

A checked cast and a second bound close it. A signed type can behave the other way.
