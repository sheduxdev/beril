---
id: spf-breaks-at-the-lookup-limit
title: SPF breaks at the lookup limit
tags: mail, spf, dns
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/email-spf.md, docs/defending.md
status: active
---
# SPF breaks at the lookup limit

## Claim

SPF allows at most 10 DNS resolving lookups. A record over the limit returns permerror and the policy is not applied.

## Test

Count include, a, mx, ptr and exists mechanisms. Follow each include. Check the final count with an SPF checker.

## Proof

A permerror at delivery or a count over 10.

## Failure modes

A flattening service removes the includes. A short chain stays under the limit.
