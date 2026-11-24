---
id: eng-i18n
title: Text, time and money are not strings
tags: engineering, i18n, locale
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Text, time and money are not strings

## Claim

Pluralization, direction, timezone and currency need a model. Concatenated strings break.

## Test

Test a long translation, a right-to-left locale and a different timezone.

## Proof

A layout and a value that remain correct.

## Failure modes

A date without a timezone is ambiguous.
