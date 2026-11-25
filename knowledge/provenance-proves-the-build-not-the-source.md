---
id: provenance-proves-the-build-not-the-source
title: Provenance proves the build, not the source
tags: supply, slsa, provenance
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/supply-sigstore.md
status: active
---
# Provenance proves the build, not the source

## Claim

A valid provenance attestation says a builder produced the artifact from a repo and commit. It does not say the source was reviewed or pinned.

## Test

Verify the attestation. Read the source repo and commit. Check whether the commit is on a protected branch and matches the tag.

## Proof

A provenance valid artifact from an unprotected or renamed source.

## Failure modes

A hermetic builder and a protected source close the gap. A valid attestation can still be for a malicious commit.
