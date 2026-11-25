---
id: jwt-algorithm-confusion-uses-the-public-key-as-an-hmac-secre
title: JWT algorithm confusion uses the public key as an HMAC secret
tags: auth, jwt, crypto
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/web-jwt-signature-trust.md, references/techniques.md
status: active
---
# JWT algorithm confusion uses the public key as an HMAC secret

## Claim

A verifier that trusts the header alg can be switched from RS256 to HS256 and signed with the public key bytes.

## Test

Take the JWKS public key, build an HS256 token with it, set alg to HS256, keep the claims.

## Proof

The API accepts the forged token.

## Failure modes

A verifier pinned to one algorithm rejects it. Key formatting must match the verifier bytes.
