---
id: dist-quorum-read
title: A quorum read must overlap the write quorum
tags: distributed, quorum, read
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A quorum read must overlap the write quorum

## Claim

R + W > N gives overlap. A read from fewer nodes can miss the latest write.

## Test

Write with a quorum. Read with different R values. Compare the value and the version.

## Proof

The latest value at the documented quorum.

## Failure modes

A sticky read hides a weak quorum. A repair without a version is a guess.
