---
id: crypto-key-rotation
title: Rotation needs a key id in the ciphertext
tags: cryptography, rotation, key-id
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Rotation needs a key id in the ciphertext

## Claim

The header carries the key version. New writes use the new key; old data decrypts until re-encrypted.

## Test

Rotate the key. Read old and new rows. Check the header and the re-encryption job.

## Proof

A decrypt across two key versions and a drained backfill.

## Failure modes

A rotation without a key id cannot decrypt old data. A retired key with live data loses it.
