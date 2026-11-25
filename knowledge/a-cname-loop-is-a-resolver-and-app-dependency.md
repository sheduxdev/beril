---
id: a-cname-loop-is-a-resolver-and-app-dependency
title: A CNAME loop is a resolver and app dependency
tags: dns, cname, loop
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/detection-dns.md
status: active
---
# A CNAME loop is a resolver and app dependency

## Claim

A loop or a long chain hits resolver limits and fails, which takes down a name that looks configured.

## Test

Follow the CNAME chain. Count the hops. Check the resolver limit and the TTL.

## Proof

A resolution failure at the hop limit.

## Failure modes

A short chain is fine. A cached answer hides it until the TTL.
