---
id: an-sbom-is-a-compliance-input-not-a-proof
title: An SBOM is a compliance input, not a proof
tags: comp, sbom, supply
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# An SBOM is a compliance input, not a proof

## Claim

The SBOM lists components. It does not prove the build, the version in production or the absence of a component.

## Test

Compare the SBOM with the running image and the lockfile. Find one difference.

## Proof

A component in production absent from the SBOM.

## Failure modes

A generated SBOM can be stale by design. A signed SBOM still needs the compare.
