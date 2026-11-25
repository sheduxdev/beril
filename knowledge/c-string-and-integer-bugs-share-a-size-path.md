---
id: c-string-and-integer-bugs-share-a-size-path
title: C string and integer bugs share a size path
tags: lang, c, memory
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/re-crash-triage-primitive.md
status: active
---
# C string and integer bugs share a size path

## Claim

A length from the input reaches an allocation and a copy. The bug is the missing bound or the wrong type on that path.

## Test

Trace the length from the parser to the copy. Check the type, the cast and the bound. Send the edge value.

## Proof

An overflow or a truncation.

## Failure modes

A checked library function closes the copy. A second bound can hold.
