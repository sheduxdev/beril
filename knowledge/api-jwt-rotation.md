---
id: api-jwt-rotation
title: Key rotation is a cache and trust problem
tags: api, jwt, jwks
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Key rotation is a cache and trust problem

## Claim

A verifier caches a JWKS, trusts a kid without lookup, or accepts a key from the token itself.

## Test

Read the header. Try an unknown kid, a remote jku, a stale key and a key removed from JWKS.

## Proof

A token signed with an attacker or retired key is accepted.

## Failure modes

A cache with a short TTL is safer. A jku fetch needs an allowlist.
