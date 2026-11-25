---
id: cbc-padding-oracle-needs-only-a-yes-or-no
title: CBC padding oracle needs only a yes or no
tags: crypto, cbc, padding
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# CBC padding oracle needs only a yes or no

## Claim

A distinguishable padding error lets an attacker decrypt and encrypt block by block without the key.

## Test

Flip the last byte of the previous block. Send the same ciphertext many times. Separate padding error from other errors.

## Proof

One byte per block recovers or forges plaintext.

## Failure modes

A generic error hides the oracle. A MAC checked before padding removes it.
