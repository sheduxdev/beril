---
id: api-cursor
title: Cursor pagination keys on the last seen tuple, not an offset
tags: api-design, pagination, paging, cursor, stability
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Cursor pagination keys on the last seen tuple, not an offset

## Claim

An offset shifts when rows are inserted; a cursor keys on the last seen tuple. The snapshot must be consistent.

## Test

Insert a row while paging with an offset and with a cursor. Compare duplicates.

## Proof

A cursor page with no duplicate and no gap.

## Failure modes

A cursor on a mutable column skips rows. A signed cursor prevents tampering but not drift.
