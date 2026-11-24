---
id: net-quic
title: QUIC moves reliability into user space per stream
tags: network, quic, streams
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# QUIC moves reliability into user space per stream

## Claim

Streams are independent so one loss does not block another. 0-RTT reuses a ticket and can replay.

## Test

Lose a packet on one stream. Check the other stream and the handshake RTT.

## Proof

A stream that continues while another recovers.

## Failure modes

0-RTT data is replayable, so it must be idempotent. A UDP-blocked network needs a fallback.
