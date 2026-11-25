---
id: hypervisor-introspection-reads-the-guest-from-outside
title: Hypervisor introspection reads the guest from outside
tags: hv, introspection, forensics
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/ir-memory.md
status: active
---
# Hypervisor introspection reads the guest from outside

## Claim

The hypervisor sees the guest memory and registers. A debug API or a memory dump can recover a key without the guest OS.

## Test

Check the introspection API. Pause the VM. Read a known guest address. Dump a process.

## Proof

A guest secret from the host view.

## Failure modes

An encrypted guest hides it. An introspection tool needs the symbol map.
