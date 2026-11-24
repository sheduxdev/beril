---
id: a11y-screenreader
title: A screen reader needs a role, a name and a state
tags: accessibility, screenreader, aria
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A screen reader needs a role, a name and a state

## Claim

Native elements carry semantics. A custom widget needs a role, an accessible name and a state update.

## Test

Navigate with a screen reader. Check the name and the state change.

## Proof

The control announced with the right role and name.

## Failure modes

An aria-label on a div without a role is a label on nothing. A live region without a politeness setting is noisy.
