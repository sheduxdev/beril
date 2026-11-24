---
id: data-ownership
title: Every field has one writer
tags: data-modeling, ownership, source-of-truth
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Every field has one writer

## Claim

Two writers to one field create a last-write-wins race. The owner is the service that validates it.

## Test

Find a field written by two services. Check the conflict.

## Proof

One writer and a documented read path for others.

## Failure modes

A shared table with two writers drifts. A derived field without a rebuild is a second truth.
