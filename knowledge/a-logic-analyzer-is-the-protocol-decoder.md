---
id: a-logic-analyzer-is-the-protocol-decoder
title: A logic analyzer is the protocol decoder
tags: hardware, logic-analyzer, protocol
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# A logic analyzer is the protocol decoder

## Claim

A capture on the right pins decodes SPI, I2C, UART and parallel buses, including the timing and the framing the firmware expects.

## Test

Hook the clock and the data. Set the threshold. Capture a known transaction. Decode by hand first.

## Proof

A decoded transaction that matches the device action.

## Failure modes

A fast bus needs a high sample rate. A differential bus needs the right probe.
