---
id: storage-checksum
title: A checksum detects corruption, it does not repair it
tags: storage, checksum, corruption
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A checksum detects corruption, it does not repair it

## Claim

Per-block checksums catch bit rot on read. Repair needs a replica or a parity block.

## Test

Corrupt a block. Read it. Check the checksum and the repair source.

## Proof

A detected corruption and a repaired read.

## Failure modes

A checksum over the wrong range misses the corruption. A scrub finds it before a read.
