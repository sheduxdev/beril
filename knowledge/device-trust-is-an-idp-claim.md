---
id: device-trust-is-an-idp-claim
title: Device trust is an IdP claim
tags: idp, device-trust, claim
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Device trust is an IdP claim

## Claim

A compliant or hybrid joined device is a claim in the token. A policy that trusts the claim without the device check is spoofable in a lab.

## Test

Read the device claim and the policy. Compare a managed and an unmanaged device. Try a token replay from another device.

## Proof

A policy pass from an unmanaged device.

## Failure modes

A token binding and a device certificate close it. A short token life limits the replay.
