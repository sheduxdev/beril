---
id: a-kprobe-is-a-runtime-hook
title: A kprobe is a runtime hook
tags: link, kprobe, trace
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/binary-ebpf.md
status: active
---
# A kprobe is a runtime hook

## Claim

A kprobe attaches to a symbol and runs a handler. It reads registers and memory at the address without a module.

## Test

List the symbols. Attach a probe. Trigger the path and read the trace.

## Proof

A trace line with the register and the call.

## Failure modes

An inlined symbol has no probe point. A static key can skip the call.
