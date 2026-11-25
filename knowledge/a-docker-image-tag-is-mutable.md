---
id: a-docker-image-tag-is-mutable
title: A Docker image tag is mutable
tags: pkg, docker, tag
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/supply-sigstore.md
status: active
---
# A Docker image tag is mutable

## Claim

A tag can be repointed to a new digest. A pull by tag takes the new image without a code change.

## Test

Read the tag and the digest. Pull again after a rebuild. Compare the digest.

## Proof

A changed digest for the same tag.

## Failure modes

A digest pin blocks it. A signed image policy can catch it.
