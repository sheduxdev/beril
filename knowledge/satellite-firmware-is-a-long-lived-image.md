---
id: satellite-firmware-is-a-long-lived-image
title: Satellite firmware is a long lived image
tags: sat, firmware, update
confidence: low
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-update-sign.md
status: active
---
# Satellite firmware is a long lived image

## Claim

A flight image is hard to patch. A bug can stay for the mission life, and the update path is rare and risky.

## Test

Read the image version and the update plan. Check the signature and the fallback slot.

## Proof

A version and an update plan with a fallback.

## Failure modes

A single image without a fallback raises the risk. A vendor can hold the source.
