---
id: auth-credential-stuffing
title: Credential stuffing is a reuse bug, not a guessing bug
tags: auth, credential-stuffing, account-takeover
confidence: high
updated: 2026-11-26
uses: 0
sources: https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html, https://owasp.org/www-community/attacks/Credential_stuffing, https://attack.mitre.org/techniques/T1110/004/
status: active
---
# Credential stuffing is a reuse bug, not a guessing bug

## Claim

An attacker replays username and password pairs leaked from another site. Each pair can be valid on the first try, so per-account lockout never fires. Reported success rate is roughly 0.2 to 2 percent, enough at scale.

## Test

Replay a small set of known-breached pairs against a staging login. Watch whether one failure counter per account is the only control, and whether a valid pair sails through without a second factor.

## Proof

A login that accepts a breached pair with no step-up, from a fresh IP, under the lockout threshold.

## Failure modes

A CAPTCHA alone is bypassed by solver services and residential proxies. The real fix is MFA, breached-password checks and device or behavior signals, not a lower lockout count.
