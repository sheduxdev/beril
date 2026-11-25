---
id: a-hypervisor-escape-is-a-chain-not-a-bug
title: A hypervisor escape is a chain, not a bug
tags: hv, escape, chain
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-hypervisor.md, references/exploit-development.md
status: active
---
# A hypervisor escape is a chain, not a bug

## Claim

The path needs a guest primitive, a device or an exit bug, a host address leak and a control target in the host process.

## Test

Map the chain steps. Prove the guest primitive first. Then the host read. Then the control.

## Proof

A host process control from the guest.

## Failure modes

A host process sandbox contains the escape. A bug can give a read without control.
