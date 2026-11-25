---
id: a-dnssec-algorithm-downgrade-needs-the-chain
title: A DNSSEC algorithm downgrade needs the chain
tags: dns, dnssec, downgrade
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/detection-dns.md
status: active
---
# A DNSSEC algorithm downgrade needs the chain

## Claim

A validator that accepts an unsigned delegation or a weak algorithm can be walked down from a signed parent.

## Test

Read the DS and the DNSKEY. Check the algorithm. Find an unsigned child under a signed zone.

## Proof

An unsigned name under the signed zone resolves without a validation failure.

## Failure modes

A strict validator and a signed child hold. A local resolver can be permissive.
