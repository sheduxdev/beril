---
id: proto-security
title: A handshake binds the transcript
tags: protocol, handshake, replay
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A handshake binds the transcript

## Claim

Authentication must cover the version, the nonce and the key exchange. An unbound field can be rewritten.

## Test

Capture a handshake. Change an unauthenticated field. Replay it.

## Proof

A rejection or a different derived key.

## Failure modes

A signature over only the public key leaves the parameters free. A nonce reuse breaks freshness.
