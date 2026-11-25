---
id: dom-clobbering-overrides-named-globals
title: DOM clobbering overrides named globals
tags: browser, dom-clobbering, xss
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/web-dom-clobbering.md
status: active
---
# DOM clobbering overrides named globals

## Claim

An element with an id or a name becomes a window property and can replace a config object the script expects.

## Test

Find a global read before a sink. Inject an element with the same id. Observe the changed type or value.

## Proof

The sink uses the clobbered value.

## Failure modes

A nullish check or a scoped variable prevents it. A sanitizer that strips id and name closes it.
