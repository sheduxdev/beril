---
id: build-hermetic
title: A hermetic build is reproducible from declared inputs
tags: build, hermetic, reproducible
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A hermetic build is reproducible from declared inputs

## Claim

No network, no clock, no absolute path and a pinned toolchain. Two machines produce the same bytes.

## Test

Build twice in different directories. Compare the hashes.

## Proof

Identical hashes across environments.

## Failure modes

A fetched dependency at build time is not hermetic. A timestamp in the binary breaks reproducibility.
