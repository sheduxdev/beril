---
id: detection-identity
title: Identity detections need a baseline and a token context
tags: detection, identity, logs
confidence: high
updated: 2026-11-25
uses: 0
sources: labs/detection
status: active
---
# Identity detections need a baseline and a token context

## Claim

Impossible travel, a new device, a token replay or a role change is only meaningful against the user's normal pattern.

## Test

Collect sign-in and audit logs. Baseline the user. Alert on a new ASN, device or scope.

## Proof

A rule that catches the anomaly and not a VPN user.

## Failure modes

A travel rule without a baseline is noise. MFA changes the picture.
