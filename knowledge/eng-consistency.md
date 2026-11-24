---
id: eng-consistency
title: Consistency is a contract about reads
tags: engineering, distributed, consistency
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Consistency is a contract about reads

## Claim

Strong, eventual, read-your-writes and monotonic reads answer different questions. The UI often needs the weaker one.

## Test

Write, then read from two replicas. Check the ordering and the lag.

## Proof

A read model that matches the promise, with the lag stated.

## Failure modes

An eventually consistent read is not a bug if the UI says so.
