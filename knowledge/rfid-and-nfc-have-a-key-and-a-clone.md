---
id: rfid-and-nfc-have-a-key-and-a-clone
title: RFID and NFC have a key and a clone
tags: hardware, rfid, nfc
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# RFID and NFC have a key and a clone

## Claim

A low frequency card with a static id is cloneable. A sector key on a MIFARE Classic can be recovered from a nested or a darkside attack.

## Test

Read the card type. Try the default keys. Capture a nested authentication. Clone and test.

## Proof

A clone accepted by the reader.

## Failure modes

A DESFire card needs a different attack. A reader with a challenge blocks a plain clone.
