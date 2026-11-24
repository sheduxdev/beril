---
id: binary-hypervisor
title: A hypervisor exposes synthetic MSRs and VTL boundaries
tags: binary, hypervisor, virtualization
confidence: low
updated: 2026-11-24
uses: 0
sources: references/reverse-engineering.md
status: active
---
# A hypervisor exposes synthetic MSRs and VTL boundaries

## Claim

Hyper-V interfaces, synthetic MSRs and VTL1 calls parse structures from a less privileged partition.

## Test

Map the hypercall and MSR surface. Check VTL and partition trust. Test a malformed input in a VM.

## Proof

A host crash or a VTL boundary bypass.

## Failure modes

A hypervisor crash can be a DoS only. VBS must be enabled for VTL1.
