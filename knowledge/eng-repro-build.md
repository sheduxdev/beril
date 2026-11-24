---
id: eng-repro-build
title: A build should be reproducible from a clean checkout
tags: engineering, build, reproducible
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A build should be reproducible from a clean checkout

## Claim

Pinned toolchain, lockfile, deterministic inputs and no local state. A build that depends on a laptop is not a build.

## Test

Clean clone, build, compare the artifact hash.

## Proof

The same hash on two machines.

## Failure modes

A timestamp or path in the artifact breaks reproducibility.
