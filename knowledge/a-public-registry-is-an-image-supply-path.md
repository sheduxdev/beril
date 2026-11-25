---
id: a-public-registry-is-an-image-supply-path
title: A public registry is an image supply path
tags: cloud, registry, image
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/supply-sigstore.md
status: active
---
# A public registry is an image supply path

## Claim

A writable or public registry tag can be replaced with a new image and pulled by the cluster on the next deploy.

## Test

Read the registry policy. Pull the image by tag. Push a marker layer. Check the digest change.

## Proof

The cluster runs your layer.

## Failure modes

A digest pin blocks tag replacement. A signed image policy can catch it.
