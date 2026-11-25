---
id: seimpersonate-is-the-service-account-ladder
title: SeImpersonate is the service account ladder
tags: win, impersonate, potato
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/win-token-privileges.md
status: active
---
# SeImpersonate is the service account ladder

## Claim

A service account with SeImpersonate can impersonate a token from a coerced local authentication and become SYSTEM.

## Test

Check the privilege. Run a Potato variant or a named pipe relay. Capture the token.

## Proof

A SYSTEM shell.

## Failure modes

A local service account can be restricted. A patched coercion path blocks it.
