---
id: stream-watermark
title: A watermark is a promise about event time
tags: data, streaming, watermark
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A watermark is a promise about event time

## Claim

The watermark says no event earlier than it will arrive. Late events beyond it are dropped or side-output.

## Test

Delay an event past the watermark. Check the window result and the side output.

## Proof

A window that closes once and reports the late data.

## Failure modes

A watermark based on processing time is wrong after a backlog. A late event silently disappears.
