---
id: oauth-state-must-be-bound-to-the-session
title: OAuth state must be bound to the session
tags: auth, oauth, csrf
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md, references/specialist-program.md
status: active
---
# OAuth state must be bound to the session

## Claim

A state value that is not tied to the browser session and not single use allows login CSRF and code injection into another account.

## Test

Start two flows in two browsers. Swap the state and code between them. Replay one state twice.

## Proof

The victim browser lands in the attacker account, or a replayed state still completes.

## Failure modes

A state that is random but stored server side per flow is fine. A same site cookie can hide the swap.
