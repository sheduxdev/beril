---
id: sev-and-tdx-encrypt-the-guest-memory
title: SEV and TDX encrypt the guest memory
tags: hv, sev, tdx
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-hypervisor.md
status: active
---
# SEV and TDX encrypt the guest memory

## Claim

The host cannot read the encrypted guest memory. The attestation report and the trust in the CPU replace the host trust.

## Test

Read the guest state. Check the attestation report and the key. Dump the memory from the host and compare.

## Proof

An encrypted page unreadable from the host.

## Failure modes

A debug mode can decrypt it. An attestation verification can be weak.
