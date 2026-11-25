---
id: strongbox-is-a-separate-secure-cpu
title: StrongBox is a separate secure CPU
tags: android, strongbox, hardware
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# StrongBox is a separate secure CPU

## Claim

A StrongBox key lives in a discrete secure element with its own constraints. The feature flag and the key attestation are checkable.

## Test

Check the feature flag. Generate a key with StrongBox. Read the attestation certificate and the security level.

## Proof

An attestation with the StrongBox level.

## Failure modes

A device without the element falls back. An OEM can disable it.
