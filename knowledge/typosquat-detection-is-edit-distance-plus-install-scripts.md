---
id: typosquat-detection-is-edit-distance-plus-install-scripts
title: Typosquat detection is edit distance plus install scripts
tags: supply, typosquat, registry
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/supply-typosquat.md
status: active
---
# Typosquat detection is edit distance plus install scripts

## Claim

A one edit neighbor of a popular name is a candidate, and the ones with lifecycle scripts or recent publishes are the live risk.

## Test

Generate one and two edit neighbors of the top dependencies. Filter by downloads, publish date and scripts.

## Proof

A neighbor with a script or a suspicious maintainer is found.

## Failure modes

A popular neighbor can be legitimate. Scope changes the name space.
