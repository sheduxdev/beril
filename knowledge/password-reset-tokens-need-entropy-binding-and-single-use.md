---
id: password-reset-tokens-need-entropy-binding-and-single-use
title: Password reset tokens need entropy, binding and single use
tags: auth, reset, token
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# Password reset tokens need entropy, binding and single use

## Claim

A short, predictable, long lived or reusable reset token allows account takeover from a leaked link.

## Test

Request two resets and compare length and alphabet. Reuse one token twice. Change the user id in the token body.

## Proof

The second use works, or the token maps to another account.

## Failure modes

A token bound to the session and one use is safe. Email link scanners can consume it first.
