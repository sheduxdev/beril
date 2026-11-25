---
id: play-integrity-is-a-signed-verdict
title: Play Integrity is a signed verdict
tags: android, integrity, play
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Play Integrity is a signed verdict

## Claim

The verdict is a signed token about the device, the app and the account. A local root hide does not change the verdict.

## Test

Request a verdict on a clean and a rooted device. Decode the payload. Compare the device integrity field.

## Proof

A verdict change with the root state.

## Failure modes

A strong verdict can still pass with a good hide. A cached verdict delays the change.
