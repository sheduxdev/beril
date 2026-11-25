---
id: otp-verification-needs-a-race-and-a-reuse-check
title: OTP verification needs a race and a reuse check
tags: auth, otp, race
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/techniques.md, knowledge/web-race-single-packet.md
status: active
---
# OTP verification needs a race and a reuse check

## Claim

If the code is checked before it is consumed, parallel requests accept the same OTP more than once.

## Test

Send the same valid OTP in ten parallel requests to the verify endpoint.

## Proof

More than one request succeeds.

## Failure modes

A database unique constraint prevents the race. A per second limit hides it.
