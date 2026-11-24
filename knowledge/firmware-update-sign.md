---
id: firmware-update-sign
title: A signed update is useless if verification is off
tags: firmware, update, signature
confidence: high
updated: 2026-11-24
uses: 0
sources: labs/firmware
status: active
---
# A signed update is useless if verification is off

## Claim

The updater parses an unsigned manifest, skips signature verification, or accepts a downgrade.

## Test

Read the updater. Check the verify flag. Rebuild a modified image. Try an older version.

## Proof

A modified rootfs accepted by the update path.

## Failure modes

A signature that covers only the header is bypassable. A version floor may block downgrade.
