---
id: window-name-survives-navigation
title: window.name survives navigation
tags: browser, window-name, state
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# window.name survives navigation

## Claim

A frame can write a large string to `window.name`, navigate the frame and read it back, which carries data across origins.

## Test

Open a cross site page in an iframe. Set name and navigate. Read name from the parent.

## Proof

The string survives the origin change.

## Failure modes

A page that resets name clears it. Browser partitioning can isolate the frame.
