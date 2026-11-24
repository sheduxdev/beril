---
id: supply-sigstore
title: Signatures are only useful when verified
tags: supply-chain, sigstore, provenance
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Signatures are only useful when verified

## Claim

Artifacts are signed but the consumer does not verify, or verifies identity without policy.

## Test

Check the signature, the certificate identity and the transparency entry. Test a tampered artifact.

## Proof

The verifier rejects a modified artifact and accepts the expected identity.

## Failure modes

A signature from an unexpected identity is not trust. A self-signed artifact proves nothing.
