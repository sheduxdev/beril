---
id: sdr-demodulates-a-nearby-radio
title: SDR demodulates a nearby radio
tags: hardware, sdr, radio
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# SDR demodulates a nearby radio

## Claim

A cheap SDR receives the modulation and the frames when the frequency and the bandwidth are known, which is the first step to a replay.

## Test

Find the frequency from the FCC ID or a scan. Set the modulation and the sample rate. Capture and decode.

## Proof

A decoded frame with a valid checksum.

## Failure modes

A hopping or a spread spectrum signal needs more work. A strong nearby transmitter can desensitize the receiver.
