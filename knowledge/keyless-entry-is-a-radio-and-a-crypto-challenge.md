---
id: keyless-entry-is-a-radio-and-a-crypto-challenge
title: Keyless entry is a radio and a crypto challenge
tags: auto, keyless, radio
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# Keyless entry is a radio and a crypto challenge

## Claim

The fob and the car exchange a challenge. A relay extends the range and a replay works only without a rolling counter.

## Test

Capture the exchange with an SDR. Try a relay with two devices. Replay one frame.

## Proof

A door unlock or a start without the fob nearby.

## Failure modes

A motion sensor in the fob blocks a relay. A rolling code blocks a replay.
