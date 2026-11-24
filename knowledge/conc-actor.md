---
id: conc-actor
title: An actor owns its state and processes one message at a time
tags: concurrency, actor, supervision
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# An actor owns its state and processes one message at a time

## Claim

Mailboxes decouple senders; supervision restarts a failed actor. An unbounded mailbox is a memory leak with backpressure missing.

## Test

Send a burst to one actor. Check the mailbox depth and the restart.

## Proof

A bounded mailbox with a supervision policy.

## Failure modes

A blocking call inside an actor stalls the mailbox. A fire-and-forget send hides failure.
