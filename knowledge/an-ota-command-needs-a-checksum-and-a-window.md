---
id: an-ota-command-needs-a-checksum-and-a-window
title: An OTA command needs a checksum and a window
tags: sat, ota, window
confidence: low
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-update-sign.md
status: active
---
# An OTA command needs a checksum and a window

## Claim

A command is sent in a pass window with a checksum and an acknowledgement. A lost ack can duplicate the command.

## Test

Read the command and the ack. Drop the ack in a lab. Send the same command twice.

## Proof

A duplicated action or an idempotent ack.

## Failure modes

A sequence counter can dedupe. A short window can expire.
