---
id: the-ebpf-verifier-is-the-program-contract
title: The eBPF verifier is the program contract
tags: link, ebpf, verifier
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-ebpf.md
status: active
---
# The eBPF verifier is the program contract

## Claim

The verifier proves bounds, stack and helper use before load. A bug is a gap between the proof and the runtime.

## Test

Read the program type and the helpers. Try a bound the verifier accepts. Run it and compare the runtime.

## Proof

A load accepted with a runtime out of bounds.

## Failure modes

A strict verifier closes it. A map value can change after the check.
