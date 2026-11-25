---
id: php-type-juggling-is-a-comparison-bug
title: PHP type juggling is a comparison bug
tags: lang, php, type
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# PHP type juggling is a comparison bug

## Claim

A loose comparison or an array parameter changes the result. `0e` hashes and null can pass a magic check.

## Test

Find loose comparisons and in_array without strict. Send a type change, an array and a magic hash.

## Proof

A check that passes with the wrong value or type.

## Failure modes

A strict comparison closes it. A cast before the check can hold.
