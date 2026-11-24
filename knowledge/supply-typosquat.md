---
id: supply-typosquat
title: A package name one character off is a supply-chain bug
tags: supply-chain, package, typosquat
confidence: high
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# A package name one character off is a supply-chain bug

## Claim

A dependency resolves to a name that resembles a popular package, or an internal name resolves from the public registry.

## Test

Compare the name with the popular package. Check the publisher, age, install count and install scripts.

## Proof

The resolved tarball differs from the intended package.

## Failure modes

A fork with the same name can be legitimate. Check the lockfile hash.
