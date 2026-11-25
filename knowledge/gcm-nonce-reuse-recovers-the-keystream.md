---
id: gcm-nonce-reuse-recovers-the-keystream
title: GCM nonce reuse recovers the keystream
tags: crypto, nonce, gcm
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/crypto-nonce.md, knowledge/crypto-aead.md
status: active
---
# GCM nonce reuse recovers the keystream

## Claim

Two messages encrypted under the same key and nonce let an attacker XOR the ciphertexts, recover the keystream and forge the tag in some cases.

## Test

Collect many tokens or blobs. Look for a repeated 12 byte nonce. XOR two ciphertexts at the same offset.

## Proof

The XOR yields readable plaintext structure or a known field.

## Failure modes

Random 96 bit nonces rarely collide. A counter with a fixed prefix is visible in the blob.
