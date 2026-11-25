---
id: a-medical-device-update-is-a-signed-package
title: A medical device update is a signed package
tags: med, update, signature
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-update-sign.md
status: active
---
# A medical device update is a signed package

## Claim

The update package and the verify path are the safety boundary. A missing signature allows a wrong firmware.

## Test

Read the update flow and the signature. Try an unsigned package. Check the rollback.

## Proof

A rejected unsigned package.

## Failure modes

A vendor tool can bypass the check. A recovery partition can accept a signed only image.
