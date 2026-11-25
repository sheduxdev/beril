---
id: an-action-pinned-by-tag-can-move
title: An action pinned by tag can move
tags: supply, ci, action
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cicd-pr-target.md
status: active
---
# An action pinned by tag can move

## Claim

A mutable tag such as v3 can be retagged to a malicious commit. Only a full SHA pins the code.

## Test

List the workflow uses lines. Check for a SHA. Resolve a tag and compare the commit over time.

## Proof

A tag resolves to a different commit than the one reviewed.

## Failure modes

A digest pin in a lock or a verified marketplace action helps. SHA alone still trusts the writer.
