---
id: a-hardcoded-key-in-the-rootfs-is-shared-by-the-fleet
title: A hardcoded key in the rootfs is shared by the fleet
tags: firmware, key, rootfs
confidence: high
updated: 2026-11-26
uses: 0
sources: references/firmware-iot.md
status: active
---
# A hardcoded key in the rootfs is shared by the fleet

## Claim

A key in a firmware image is identical across every device of that build and often across builds.

## Test

Search the rootfs for private keys, tokens and default passwords. Confirm reuse on a second image.

## Proof

The same key or password on two devices or images.

## Failure modes

A per device key generated at first boot is unique. A read only key can be public by design.
