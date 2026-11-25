---
id: a-suid-binary-is-only-useful-with-a-path
title: A SUID binary is only useful with a path
tags: linux, suid, privilege
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# A SUID binary is only useful with a path

## Claim

A SUID binary that runs another program, reads a config or loads a library can be turned into root if the path is controllable.

## Test

List SUID files. Check GTFOBins and the linked libraries. Run the file with a controlled PATH or config.

## Proof

A root shell or a root file read.

## Failure modes

A static binary with no external call is harder. NoNewPrivs can block a shell.
