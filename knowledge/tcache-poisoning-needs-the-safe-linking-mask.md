---
id: tcache-poisoning-needs-the-safe-linking-mask
title: Tcache poisoning needs the safe linking mask
tags: binary, heap, tcache
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# Tcache poisoning needs the safe linking mask

## Claim

Since glibc 2.32 the tcache next pointer is XORed with the chunk address shifted by 12, so a plain address write fails.

## Test

Read the glibc version. Inspect a freed tcache chunk. Compute the mask and write the target with it.

## Proof

The second allocation returns the target address.

## Failure modes

An older glibc has no safe linking. A heap leak is needed for the mask.
