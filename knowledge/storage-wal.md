---
id: storage-wal
title: A write-ahead log makes the write durable before the page
tags: storage, wal, durability
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A write-ahead log makes the write durable before the page

## Claim

The log record is appended and fsynced before the data page changes. Recovery replays the log.

## Test

Kill the process between log and page. Restart. Check the replay.

## Proof

The committed record survives the crash.

## Failure modes

A log without fsync is not durable. A checkpoint that outruns the log loses data.
