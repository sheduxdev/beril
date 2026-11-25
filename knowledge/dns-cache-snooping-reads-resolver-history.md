---
id: dns-cache-snooping-reads-resolver-history
title: DNS cache snooping reads resolver history
tags: network, dns, cache
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# DNS cache snooping reads resolver history

## Claim

A non recursive query to a resolver answers from cache, so a fast reply reveals that someone recently looked up the name.

## Test

Pick a random name and the target name. Query both with the recursion flag off. Compare the response code and time.

## Proof

The target name is answered from cache while the random name is not.

## Failure modes

A resolver that always recurses hides it. A negative cache entry answers the random name too.
