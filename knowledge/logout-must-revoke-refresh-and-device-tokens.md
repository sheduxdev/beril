---
id: logout-must-revoke-refresh-and-device-tokens
title: Logout must revoke refresh and device tokens
tags: auth, session, logout
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Logout must revoke refresh and device tokens

## Claim

Clearing the browser cookie leaves refresh tokens and other devices valid. A stolen token survives logout.

## Test

Capture a refresh token and a second device session. Log out on the first. Replay both.

## Proof

The refresh token or the second device still works.

## Failure modes

Short lived access tokens are expected to survive. The refresh token is the real test.
