---
id: conc-csp
title: A channel is a rendezvous with a buffer policy
tags: concurrency, csp, channels
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A channel is a rendezvous with a buffer policy

## Claim

An unbuffered channel blocks until both sides meet. A closed channel signals completion; a send on it panics.

## Test

Send on an unbuffered channel with no reader. Close it with a pending sender.

## Proof

A pipeline that drains and exits cleanly.

## Failure modes

A goroutine leak hides a missing reader. A close from the receiver side races with senders.
