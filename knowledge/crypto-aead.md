---
id: crypto-aead
title: AEAD authenticates ciphertext and associated data together
tags: cryptography, aead, nonce
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# AEAD authenticates ciphertext and associated data together

## Claim

The tag binds the ciphertext and the AAD. Reusing a nonce with the same key breaks confidentiality and the tag.

## Test

Encrypt two messages with the same nonce. Compare the keystream and verify the tag.

## Proof

A unique nonce per key and an AAD that names the context.

## Failure modes

A random nonce without collision analysis is a risk. A missing AAD lets a field be swapped between messages.
