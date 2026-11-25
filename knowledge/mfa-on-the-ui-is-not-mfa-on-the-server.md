---
id: mfa-on-the-ui-is-not-mfa-on-the-server
title: MFA on the UI is not MFA on the server
tags: auth, mfa, access-control
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# MFA on the UI is not MFA on the server

## Claim

If the second factor only gates a redirect, the post login API often accepts a session that never passed it.

## Test

Log in with the password, skip the OTP request, call the authenticated API and a sensitive action directly.

## Proof

The API returns data before the OTP step.

## Failure modes

Some apps issue a limited token and enforce scope server side. Read the token claims before calling it a bypass.
