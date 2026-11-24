---
id: binary-ebpf
title: The eBPF verifier is the security boundary
tags: binary, ebpf, verifier
confidence: low
updated: 2026-11-25
uses: 0
sources: references/reverse-engineering.md
status: active
---
# The eBPF verifier is the security boundary

## Claim

Programs run in kernel context after verification. Helper calls, maps and pointer arithmetic are the surface.

## Test

Map the program type and helpers. Test map bounds. Check the verifier log.

## Proof

A verifier confusion or an out-of-bounds map access.

## Failure modes

A privileged loader can bypass some checks. CO-RE versions matter.
