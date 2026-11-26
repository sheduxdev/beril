---
id: auth-password-spray
title: Password spraying inverts the loop to dodge lockout
tags: auth, password-spray, detection
confidence: high
updated: 2026-11-26
uses: 0
sources: https://attack.mitre.org/techniques/T1110/003/, https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html, https://pages.nist.gov/800-63-4/sp800-63b.html
status: active
---
# Password spraying inverts the loop to dodge lockout

## Claim

One common password is tried against many accounts, then the next password after a delay. Each account sees one failure, so per-account counters stay quiet while the tenant is under attack.

## Test

Aggregate failed logins by source and by password hash across all accounts in a window, not per account. Look for one source touching many usernames with a low per-account rate.

## Proof

A tenant-wide spike in distinct usernames failing, with few failures each, often low and slow across hours.

## Failure modes

Per-account lockout is the control that misses this. Detection needs tenant-wide aggregation and an impossible-travel or new-ASN signal. Banning common passwords shrinks the usable spray list.
