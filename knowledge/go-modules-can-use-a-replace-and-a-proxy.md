---
id: go-modules-can-use-a-replace-and-a-proxy
title: Go modules can use a replace and a proxy
tags: pkg, gomod, proxy
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Go modules can use a replace and a proxy

## Claim

A `replace` points a module to a local or a fork. A proxy can serve a different zip for the same version.

## Test

Read the go.mod and the replace. Check the sumdb and the proxy. Build with a clean cache.

## Proof

A replaced module path in the build.

## Failure modes

A sumdb pin catches a changed zip. A private proxy can be the only source.
