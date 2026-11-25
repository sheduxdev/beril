---
id: ld-preload-needs-a-trusted-launcher-and-a-writable-library
title: LD_PRELOAD needs a trusted launcher and a writable library
tags: linux, ld-preload, library
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# LD_PRELOAD needs a trusted launcher and a writable library

## Claim

A root process that keeps LD_PRELOAD or reads a config with it loads the attacker library into its address space.

## Test

Check the environment and the sudo secure path. Build a library with a constructor. Run the launcher.

## Proof

The constructor runs as root.

## Failure modes

A setuid binary ignores LD_PRELOAD unless the library is in a trusted path. A static binary ignores it.
