---
id: a-proxy-environment-variable-is-a-trust-boundary
title: A proxy environment variable is a trust boundary
tags: network, proxy, env
confidence: high
updated: 2026-11-26
uses: 0
sources: references/network-toolkit.md
status: active
---
# A proxy environment variable is a trust boundary

## Claim

`HTTP_PROXY` and `NO_PROXY` decide which requests leave and which stay local. A wrong `NO_PROXY` sends internal traffic to the proxy.

## Test

Read the variables in the process environment. Request an internal name and a public one. Watch the proxy log.

## Proof

An internal name appears at the proxy.

## Failure modes

A client that ignores the variable skips it. A transparent proxy makes it moot.
