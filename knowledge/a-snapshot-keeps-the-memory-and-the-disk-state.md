---
id: a-snapshot-keeps-the-memory-and-the-disk-state
title: A snapshot keeps the memory and the disk state
tags: hv, snapshot, forensics
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/ir-memory.md
status: active
---
# A snapshot keeps the memory and the disk state

## Claim

A snapshot file holds RAM, device state and a disk delta. It is a forensic copy and a replay point.

## Test

Read the snapshot files and the chain. Mount a copy read only. Carve one process from the RAM.

## Proof

A process or a key from the snapshot.

## Failure modes

An encrypted snapshot needs the key. A live snapshot can be inconsistent.
