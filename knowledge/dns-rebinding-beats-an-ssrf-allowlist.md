---
id: dns-rebinding-beats-an-ssrf-allowlist
title: DNS rebinding beats an SSRF allowlist
tags: web, ssrf, dns
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/web-ssrf-parser-differential.md, references/techniques.md
status: active
---
# DNS rebinding beats an SSRF allowlist

## Claim

If the app resolves the host once and fetches later, a low TTL name can resolve to a public IP at check time and to internal at fetch time.

## Test

Use a rebinding service with a short TTL. Watch the first resolution and the second. Point the second at metadata.

## Proof

The fetch reaches the internal address after the allowlist check.

## Failure modes

A resolver that pins the IP prevents it. A proxy with its own DNS can differ.
