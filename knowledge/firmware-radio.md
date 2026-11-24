---
id: firmware-radio
title: Radio protocols are state machines with replay windows
tags: firmware, radio, ble
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/firmware-iot.md
status: active
---
# Radio protocols are state machines with replay windows

## Claim

A BLE, Zigbee or sub-GHz command can be captured and replayed, or the pairing lacks freshness.

## Test

Capture pairing and command frames. Replay. Change a counter or nonce. Compare the device state.

## Proof

A replayed command that changes state.

## Failure modes

A replay that works once may be a race. A rolling code needs a fresh capture.
