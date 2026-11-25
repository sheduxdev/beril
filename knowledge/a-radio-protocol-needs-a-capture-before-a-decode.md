---
id: a-radio-protocol-needs-a-capture-before-a-decode
title: A radio protocol needs a capture before a decode
tags: firmware, radio, protocol
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# A radio protocol needs a capture before a decode

## Claim

Sub GHz and BLE frames can be captured and replayed. The first step is the modulation, the sync word and the frame length.

## Test

Capture with the right antenna and modulation. Identify the sync and the length. Replay one frame.

## Proof

The device reacts to the replay.

## Failure modes

A rolling code blocks a plain replay. A noisy band hides the frame.
