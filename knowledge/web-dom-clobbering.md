---
id: web-dom-clobbering
title: DOM clobbering turns an id into a variable
tags: web, dom, clobbering
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# DOM clobbering turns an id into a variable

## Claim

A named element or form overrides a global property that the script trusts, such as config or a function.

## Test

Look for document.getElementById fallbacks, window.name, and unqualified globals. Inject an element with the expected id.

## Proof

A script reads attacker-controlled markup as a config or a URL.

## Failure modes

A unique id that is never read as a variable is not clobberable. Modules reduce the surface.
