---
id: a-crypto-decision-needs-the-threat-and-the-key-owner
title: A crypto decision needs the threat and the key owner
tags: design, crypto, key
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/crypto-aead.md, knowledge/crypto-kdf.md
status: active
---
# A crypto decision needs the threat and the key owner

## Claim

The algorithm is the last choice. The threat, the data lifetime and who holds the key decide the primitive and the mode.

## Test

Write the threat, the data lifetime and the key owner. Compare the design with the three. Find the mismatch.

## Proof

A design table with the three inputs and the chosen primitive.

## Failure modes

A compliance rule can force an algorithm. A key can move after the design.
