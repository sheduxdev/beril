---
id: iboot-verifies-the-next-stage
title: iBoot verifies the next stage
tags: ios, iboot, boot
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-secureboot.md
status: active
---
# iBoot verifies the next stage

## Claim

The boot chain verifies each image against the Apple signature. A bootrom bug is needed below iBoot.

## Test

Read the boot log. Check the image signature and the nonce. Try a signed older image and watch the refusal.

## Proof

A rejected image and the signature state.

## Failure modes

A signed shsh blob can allow a downgrade. A bootrom exploit bypasses the chain.
