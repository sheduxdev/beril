---
id: supply-lockfile
title: A lockfile is an integrity contract
tags: supply-chain, lockfile, reproducible
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# A lockfile is an integrity contract

## Claim

The lockfile is missing, unpinned, or resolved from a different registry than the source. Builds drift.

## Test

Check lockfile presence and registry URLs. Diff a clean install. Look for git or file dependencies.

## Proof

A dependency source that differs from the intended registry.

## Failure modes

A lockfile with integrity hashes is not automatically safe if the registry is compromised.
