---
id: can-frames-are-broadcast-with-an-arbitration-id
title: CAN frames are broadcast with an arbitration id
tags: ot, can, automotive
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# CAN frames are broadcast with an arbitration id

## Claim

On a CAN bus every node sees every frame. The arbitration id names the message, and a write can impersonate a sensor or a command.

## Test

Capture the bus in a lab. Identify the periodic ids. Replay one frame and watch the dashboard or the log.

## Proof

A reaction to the replayed frame.

## Failure modes

A gateway isolates the bus. A counter or a checksum in the payload blocks a plain replay.
