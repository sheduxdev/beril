---
id: web-jwt-signature-trust
title: JWT bugs are claim trust, not base64
tags: web, jwt, identity
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md, references/claude-bughunter.md
status: active
---
# JWT bugs are claim trust, not base64

## Claim

The verifier trusts an algorithm, key or claim it should not. Decoding is not verification.

## Test

Test alg none, algorithm confusion, weak HMAC keys, kid injection, jku/x5u, claim type confusion and expiry handling.

## Proof

A forged token accepted by a protected endpoint.

## Failure modes

A decoded payload is not a finding. A 401 with a different body can still be a bypass on a sibling route.
