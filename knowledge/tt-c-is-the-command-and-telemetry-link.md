---
id: tt-c-is-the-command-and-telemetry-link
title: TT&C is the command and telemetry link
tags: sat, ttc, command
confidence: low
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# TT&C is the command and telemetry link

## Claim

The telemetry and command link uses a fixed frame and often a weak or no crypto. A captured frame can be decoded and replayed.

## Test

Find the band and the modulation. Capture a pass. Decode the frame. Replay one command frame.

## Proof

A decoded telemetry frame or a replay.

## Failure modes

A spread spectrum and a Doppler shift need correction. A command counter can block a replay.
