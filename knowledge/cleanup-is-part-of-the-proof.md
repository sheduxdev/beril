---
id: cleanup-is-part-of-the-proof
title: Cleanup is part of the proof
tags: red, cleanup, evidence
confidence: high
updated: 2026-11-26
uses: 0
sources: docs/attacking.md
status: active
---
# Cleanup is part of the proof

## Claim

A left user, key or scheduled task corrupts the next engagement and the client's asset count. The cleanup list is written before the action.

## Test

Each action gets a cleanup command. Run the list. Check the user, the key and the task are gone.

## Proof

A clean state check after the list.

## Failure modes

A crashed action leaves a partial artifact. A cleanup can remove evidence the client wanted.
