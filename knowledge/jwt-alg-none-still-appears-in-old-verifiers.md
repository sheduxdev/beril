---
id: jwt-alg-none-still-appears-in-old-verifiers
title: JWT alg none still appears in old verifiers
tags: crypto, jwt, none
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/web-jwt-signature-trust.md
status: active
---
# JWT alg none still appears in old verifiers

## Claim

A verifier that accepts an empty signature lets the attacker set the claims and the header alg to none.

## Test

Set alg to none, empty the signature, keep the payload. Try none, None and NONE.

## Proof

The token is accepted.

## Failure modes

Modern libraries require a key. A verifier can accept none only for one route.
