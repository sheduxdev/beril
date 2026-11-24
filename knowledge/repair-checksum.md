---
id: repair-checksum
title: A scrub finds bit rot before a read does
tags: distributed-storage, checksum, scrub
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A scrub finds bit rot before a read does

## Claim

Block checksums verify on read and on a scheduled scrub. A failing block is rebuilt from a peer.

## Test

Corrupt a block on disk. Wait for the scrub. Read the key.

## Proof

A repaired read and a scrub log entry.

## Failure modes

A checksum stored on the same failing sector is useless. An unscrubbed cold range rots silently.
