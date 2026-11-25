---
id: ecb-leaks-block-structure-and-equality
title: ECB leaks block structure and equality
tags: crypto, ecb, block
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# ECB leaks block structure and equality

## Claim

Identical plaintext blocks produce identical ciphertext blocks, so structure, repetition and some chosen prefix attacks survive.

## Test

Encrypt controlled repeated input. Compare equal blocks. Check whether a block boundary can be shifted with a prefix.

## Proof

Equal plaintext blocks map to equal ciphertext blocks.

## Failure modes

A random IV in CBC hides equality. A single block message leaks nothing.
