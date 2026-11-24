---
id: web-race-single-packet
title: A race is a check and a write without one lock
tags: web, race, logic
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md, references/claude-bughunter.md
status: active
---
# A race is a check and a write without one lock

## Claim

The invariant is checked before a write, with no transaction or unique constraint. Parallel requests pass the same check.

## Test

Identify the invariant. Send parallel requests, ideally in one packet on HTTP/2. Compare successes with the intended limit.

## Proof

Two successes where one was allowed, with timestamps and request ids.

## Failure modes

A retry looks like a race. Server deduplication may hide it on a later request.
