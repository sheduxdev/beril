---
id: crypto-postquantum
title: PQC migration is a hybrid, not a flag
tags: crypto, pqc, hybrid
confidence: low
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# PQC migration is a hybrid, not a flag

## Claim

A hybrid handshake combines a classical and a post-quantum exchange. A stored transcript can be broken later if only classical is used.

## Test

Read the TLS groups. Check the library and version. Test whether a hybrid group is offered.

## Proof

A negotiated hybrid group in the handshake.

## Failure modes

A PQ-only deployment can break old clients. A signature algorithm is a separate migration.
