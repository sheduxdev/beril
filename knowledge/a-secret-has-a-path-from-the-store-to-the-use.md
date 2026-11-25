---
id: a-secret-has-a-path-from-the-store-to-the-use
title: A secret has a path from the store to the use
tags: design, secret, flow
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-secrets.md
status: active
---
# A secret has a path from the store to the use

## Claim

The store is only one point. The secret crosses an environment, a file, a memory and a log. Every hop is a copy.

## Test

Trace one secret from the store to the call. List every hop and the access right. Find one hop with a broader reader.

## Proof

A hop where a process outside the owner can read the value.

## Failure modes

An injected sidecar can narrow the path. A short lived token lowers the value of a copy.
