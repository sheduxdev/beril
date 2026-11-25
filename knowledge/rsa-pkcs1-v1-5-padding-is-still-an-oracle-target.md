---
id: rsa-pkcs1-v1-5-padding-is-still-an-oracle-target
title: RSA PKCS1 v1.5 padding is still an oracle target
tags: crypto, rsa, padding
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# RSA PKCS1 v1.5 padding is still an oracle target

## Claim

A decryptor that reports padding validity before MAC lets an attacker run Bleichenbacher style queries.

## Test

Send many modified ciphertexts. Classify responses into padding valid, MAC valid and invalid. Measure the split.

## Proof

A recovered plaintext or forged signature.

## Failure modes

Constant time and uniform errors close it. Small messages can hide the oracle.
