---
id: a-payload-needs-a-loader-and-a-fallback
title: A payload needs a loader and a fallback
tags: red, payload, loader
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/mal-loader.md
status: active
---
# A payload needs a loader and a fallback

## Claim

A raw payload fails on a missing runtime or a blocked path. The loader and the fallback are part of the payload.

## Test

Run the payload on the target build. Remove one dependency and retry. Check the fallback.

## Proof

A run through the fallback after the first path fails.

## Failure modes

A single path can be enough in a lab. A fallback can add noise.
