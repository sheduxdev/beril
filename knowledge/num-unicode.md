---
id: num-unicode
title: A string is bytes plus an encoding; a character is a grapheme
tags: numerics, unicode, encoding
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A string is bytes plus an encoding; a character is a grapheme

## Claim

UTF-8 is a byte encoding. Normalization unifies equivalent sequences; a grapheme cluster is what a user sees.

## Test

Reverse a string with an emoji and a combining mark. Compare by code point and by grapheme.

## Proof

A length and a reversal that match user perception.

## Failure modes

A byte length is not a character count. Comparing without normalization misses equality.
