---
id: eng-mobile-arch
title: Offline-first is a merge problem
tags: engineering, mobile, offline
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Offline-first is a merge problem

## Claim

Local writes need a queue, conflict resolution and a sync boundary. A spinner is not a strategy.

## Test

Write offline. Reconnect. Check the merge and the conflict UI.

## Proof

A deterministic merge with a conflict path.

## Failure modes

Last-write-wins loses data. A queue without a limit grows.
