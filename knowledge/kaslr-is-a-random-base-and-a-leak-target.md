---
id: kaslr-is-a-random-base-and-a-leak-target
title: KASLR is a random base and a leak target
tags: link, kaslr, leak
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/binary-kernel.md
status: active
---
# KASLR is a random base and a leak target

## Claim

The kernel base is randomized at boot. A pointer in a log, a map or an uninitialized structure removes the entropy.

## Test

Read the base from a debug source. Compare two boots. Find a pointer in a user readable path.

## Proof

A leaked pointer and the calculated base.

## Failure modes

A heap leak can be enough. A KASLR off kernel needs no leak.
