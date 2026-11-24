---
id: proto-backpressure
title: Flow control is a window the receiver grants
tags: protocol, backpressure, window
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Flow control is a window the receiver grants

## Claim

The receiver advertises capacity; the sender may not exceed it. A zero window pauses the stream.

## Test

Fill the window. Check the send behavior and the zero-window probe.

## Proof

A sender that pauses and resumes.

## Failure modes

A window update lost without a probe stalls. A window too large buffers too much.
