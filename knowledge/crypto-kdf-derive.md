---
id: crypto-kdf-derive
title: A KDF separates keys by label and context
tags: cryptography, kdf, hkdf
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A KDF separates keys by label and context

## Claim

HKDF extracts entropy then expands with an info string. Distinct info gives independent keys.

## Test

Derive two keys with different info. Check that they differ and that the same inputs reproduce.

## Proof

A derived key per purpose with a documented info string.

## Failure modes

Reusing one key for encryption and MAC couples the proofs. A missing salt weakens extraction.
