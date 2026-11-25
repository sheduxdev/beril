---
id: caa-limits-who-can-issue-for-a-name
title: CAA limits who can issue for a name
tags: dns, caa, certificate
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/detection-tls.md
status: active
---
# CAA limits who can issue for a name

## Claim

A CAA record names the allowed CAs. A missing record allows any CA, and a wildcard issue can be claimed elsewhere.

## Test

Query CAA for the apex and the subdomain. Compare with the issuer. Try an issuance from a CA outside the set.

## Proof

A certificate from a CA not in the CAA set.

## Failure modes

A CA that ignores CAA can still issue. A CAA on the parent covers the child.
