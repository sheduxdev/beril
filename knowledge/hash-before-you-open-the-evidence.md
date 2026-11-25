---
id: hash-before-you-open-the-evidence
title: Hash before you open the evidence
tags: ir, custody, hash
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ir-disk.md, knowledge/ir-memory.md
status: active
---
# Hash before you open the evidence

## Claim

Opening a file or mounting an image changes atime and can change the artifact. The hash and the write blocker come first.

## Test

Hash the image. Mount read only. Hash again and compare. Log every tool and version.

## Proof

Matching hashes before and after and a tool log.

## Failure modes

A live filesystem changes by nature. A hardware write blocker can be missing on a laptop.
