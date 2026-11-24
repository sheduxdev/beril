---
id: data-temporal
title: Bitemporal data separates valid time from recorded time
tags: data-modeling, temporal, history
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Bitemporal data separates valid time from recorded time

## Claim

Valid time is when the fact is true; transaction time is when it was stored. A correction changes transaction time only.

## Test

Correct a past record. Query as-of the old transaction time and the new one.

## Proof

Two answers that match the two timelines.

## Failure modes

A single timestamp conflates the two. An update in place erases the correction.
