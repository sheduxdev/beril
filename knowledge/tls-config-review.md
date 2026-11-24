---
id: tls-config-review
title: TLS is a version, a chain and a policy
tags: crypto, tls, certificate
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/tooling.md
status: active
---
# TLS is a version, a chain and a policy

## Claim

Old protocols, weak ciphers, an incomplete chain or a hostname mismatch. A padlock is not a policy.

## Test

Use openssl s_client with each version. Check the chain, SAN and expiry. Test a wrong hostname.

## Proof

A protocol or chain failure with a clear client impact.

## Failure modes

A modern browser may hide the chain issue. A self-signed cert in a lab is expected.
