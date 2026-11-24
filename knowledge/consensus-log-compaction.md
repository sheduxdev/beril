---
id: consensus-log-compaction
title: Compaction keeps a snapshot and the suffix after it
tags: distributed, consensus, compaction
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Compaction keeps a snapshot and the suffix after it

## Claim

The log is truncated up to the snapshot index. The suffix stays for lagging followers; a lag beyond it needs install.

## Test

Compact below a follower's index. Restart the follower after a long pause.

## Proof

A follower either catches up from the suffix or installs the snapshot.

## Failure modes

A snapshot without retention bricks a slow follower. Compaction during a snapshot transfer is racy.
