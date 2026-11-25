---
id: house-of-force-needs-a-top-chunk-size-overwrite
title: House of Force needs a top chunk size overwrite
tags: pwn, heap, house-of-force
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# House of Force needs a top chunk size overwrite

## Claim

Overwriting the top chunk size with a huge value lets the next malloc return an arbitrary address.

## Test

Overflow into the top size. Request a size that walks to the target. Check the returned pointer.

## Proof

malloc returns the chosen address.

## Failure modes

A top size check or a large request guard blocks it. Modern glibc adds checks.
