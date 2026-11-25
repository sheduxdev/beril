---
id: a-historian-is-a-copy-of-the-process
title: A historian is a copy of the process
tags: ot, historian, data
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/network-visibility.md
status: active
---
# A historian is a copy of the process

## Claim

The historian stores tags and often connects to many PLCs. Read access is process data and a pivot path.

## Test

Find the historian endpoint and the tag list. Read one tag series. Check the write path back to the PLC.

## Proof

A tag series and a reachable PLC from the historian.

## Failure modes

A one way diode blocks the write back. A read only account limits it.
