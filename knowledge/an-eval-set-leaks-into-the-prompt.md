---
id: an-eval-set-leaks-into-the-prompt
title: An eval set leaks into the prompt
tags: ai, eval, leak
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# An eval set leaks into the prompt

## Claim

A few shot prompt or a demo carries eval examples. A model can score well by memorizing them and fail on a new shape.

## Test

Take three prompt examples. Change the names and the order. Compare the score with the original set.

## Proof

A large score drop on a renamed set.

## Failure modes

A robust prompt holds. A tiny eval cannot show the gap.
