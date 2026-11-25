---
id: a-tpm-is-a-measured-boot-and-a-sealed-secret
title: A TPM is a measured boot and a sealed secret
tags: hardware, tpm, boot
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-secureboot.md
status: active
---
# A TPM is a measured boot and a sealed secret

## Claim

PCR values record the boot path. A secret sealed to the PCRs opens only on the expected path, and a different path fails.

## Test

Read the PCR values after a normal boot. Seal a test secret. Change one boot component and unseal.

## Proof

A failed unseal on the changed path.

## Failure modes

A TPM clear resets the state. A measured but not enforced path is only a log.
