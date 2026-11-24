---
id: detection-tls
title: TLS fingerprints identify a client stack, not a person
tags: detection, tls, ja3
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/techniques.md
status: active
---
# TLS fingerprints identify a client stack, not a person

## Claim

JA3/JA4 hashes group clients by version, ciphers and extensions. A mismatch with the claimed user agent is a signal.

## Test

Extract JA3/JA4 from flows. Compare with the User-Agent. Baseline the top clients.

## Proof

A client fingerprint that does not match the expected stack.

## Failure modes

A proxy or library changes the fingerprint. A match is not proof of malware.
