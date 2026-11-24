---
id: hw-firmware-update
title: A firmware update needs A/B slots and a rollback
tags: hardware, firmware, rollback
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A firmware update needs A/B slots and a rollback

## Claim

The new image boots in a trial slot; a watchdog or a health check confirms it. A failed boot reverts.

## Test

Cut power during the update. Boot. Check the slot and the version.

## Proof

A device that recovers to a working image from any interruption.

## Failure modes

An in-place update that loses power bricks the device. A trial without a revert keeps a bad image.
