---
id: as-rep-roast-needs-preauthentication-off
title: AS-REP roast needs preauthentication off
tags: ad, kerberos, asrep
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# AS-REP roast needs preauthentication off

## Claim

An account with Kerberos preauthentication disabled returns an AS-REP encrypted with its password hash to any user.

## Test

Enumerate accounts with Do not require Kerberos preauthentication. Request an AS-REP and save the hash.

## Proof

The hash cracks offline.

## Failure modes

Preauth is on by default. A long random password holds.
