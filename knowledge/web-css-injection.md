---
id: web-css-injection
title: CSS injection exfiltrates attributes without script
tags: web, css, injection
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/techniques.md
status: active
---
# CSS injection exfiltrates attributes without script

## Claim

A style sink accepts user CSS. Attribute selectors plus background requests leak token characters one at a time.

## Test

Inject a selector for an input value prefix. Point the background at a listener. Brute the next character.

## Proof

A request whose path contains the guessed value.

## Failure modes

CSS cannot read arbitrary DOM text. It needs an attribute selector and a stable prefix.
