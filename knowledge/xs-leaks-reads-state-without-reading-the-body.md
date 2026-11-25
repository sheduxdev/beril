---
id: xs-leaks-reads-state-without-reading-the-body
title: XS-Leaks reads state without reading the body
tags: browser, xsleaks, side-channel
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# XS-Leaks reads state without reading the body

## Claim

Cache, frame count, timing, error events and size can leak whether a cross site response matches a condition.

## Test

Pick a state dependent endpoint. Measure a cache probe, an onload event or a timing difference in a cross site page.

## Proof

A yes or no bit about the victim state from another origin.

## Failure modes

SameSite, CORP and partitioning close the channel. A noisy network hides timing.
