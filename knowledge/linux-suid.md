---
id: linux-suid
title: A SUID binary is a path, not a finding
tags: linux, privesc, suid
confidence: high
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# A SUID binary is a path, not a finding

## Claim

A SUID binary has a feature that reads or writes a file as its owner, or a GTFOBins entry.

## Test

Find SUID files. Check the version and GTFOBins. Run the escape with a harmless file.

## Proof

A root read or shell from the binary.

## Failure modes

A SUID binary with no useful feature is noise. Mount options can disable SUID.
