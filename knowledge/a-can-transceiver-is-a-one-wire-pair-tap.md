---
id: a-can-transceiver-is-a-one-wire-pair-tap
title: A CAN transceiver is a one wire pair tap
tags: hardware, can, automotive
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# A CAN transceiver is a one wire pair tap

## Claim

CAN H and L are a differential pair. A transceiver and an analyzer read every frame, and a write can inject one.

## Test

Find the OBD or the bus pair. Measure the differential idle. Capture with the right bit rate. Inject one frame.

## Proof

A captured frame and a reaction to an injected one.

## Failure modes

A gateway isolates the bus. A checksum or a counter blocks a plain frame.
