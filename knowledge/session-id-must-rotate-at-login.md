---
id: session-id-must-rotate-at-login
title: Session id must rotate at login
tags: auth, session, fixation
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# Session id must rotate at login

## Claim

A session id that survives authentication allows an attacker who planted it to share the victim session.

## Test

Set a known session cookie, log in, compare the cookie before and after.

## Proof

The same id is authenticated after login.

## Failure modes

A stateless JWT can keep the same id by design. Check whether the token carries a new auth time and scope.
