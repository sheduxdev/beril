---
id: a-packer-is-a-section-and-entropy-pattern
title: A packer is a section and entropy pattern
tags: malware, packer, entropy
confidence: high
updated: 2026-11-26
uses: 0
sources: references/reverse-engineering.md
status: active
---
# A packer is a section and entropy pattern

## Claim

A high entropy section with a small import table and a write then execute stub is a packer, not a compiler.

## Test

Read the section entropy and the import count. Compare with a known clean build. Check the entry section.

## Proof

A packer signature and a stub that resolves imports at run time.

## Failure modes

A compressed installer can look the same. A custom loader can hide the stub.
