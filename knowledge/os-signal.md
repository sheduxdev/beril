---
id: os-signal
title: A signal handler runs on an arbitrary stack point
tags: os, signal, async
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A signal handler runs on an arbitrary stack point

## Claim

Only async-signal-safe calls are allowed. A handler must be short and restart interrupted calls.

## Test

Send a signal during a blocking call. Check the handler and the restart.

## Proof

A safe handler with a restart or a clean exit.

## Failure modes

A malloc in a handler can deadlock. SA_RESTART hides the interruption.
