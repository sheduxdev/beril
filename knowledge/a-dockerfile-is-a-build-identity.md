---
id: a-dockerfile-is-a-build-identity
title: A Dockerfile is a build identity
tags: lang, dockerfile, supply
confidence: high
updated: 2026-11-26
uses: 0
sources: docs/scan-artifacts.md, knowledge/cloud-docker-socket.md
status: active
---
# A Dockerfile is a build identity

## Claim

A mutable base tag, a root user and a secret in a layer define the image trust and the runtime rights.

## Test

Read the base, the user and the copy order. Check the history for a secret. Scan the final image.

## Proof

A secret in a layer or a root runtime user.

## Failure modes

A digest and a distroless base close it. A build secret mount keeps the value out of layers.
