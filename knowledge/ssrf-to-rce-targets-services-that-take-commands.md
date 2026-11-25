---
id: ssrf-to-rce-targets-services-that-take-commands
title: SSRF to RCE targets services that take commands
tags: rce, ssrf, redis
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/rce-mastery.md
status: active
---
# SSRF to RCE targets services that take commands

## Claim

Redis with CONFIG SET, Docker API, kubelet, Consul and Jenkins turn a fetch into execution. Gopher is the strongest protocol when available.

## Test

Confirm a read from the internal service first. Then send one state change. Use a host header or a gopher payload only after the protocol is known.

## Proof

A read, then an action, then command output or a callback.

## Failure modes

A fetch error is not SSRF. Egress can be one host only. DNS rebinding is blocked.
