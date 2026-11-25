---
id: an-sbom-without-transitive-components-is-a-file-list
title: An SBOM without transitive components is a file list
tags: supply, sbom, coverage
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# An SBOM without transitive components is a file list

## Claim

A useful SBOM covers transitive and vendored components with versions and purls. A top level list misses the vulnerable depth.

## Test

Compare the SBOM component count with the lockfile. Check transitive and bundled entries. Match a few to OSV.

## Proof

A transitive or vendored component present in the build is absent from the SBOM.

## Failure modes

A runtime only SBOM can be narrower by design. A generated file can be stale.
