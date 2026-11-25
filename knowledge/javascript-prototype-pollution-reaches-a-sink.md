---
id: javascript-prototype-pollution-reaches-a-sink
title: JavaScript prototype pollution reaches a sink
tags: lang, javascript, prototype
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/web-prototype-pollution.md
status: active
---
# JavaScript prototype pollution reaches a sink

## Claim

A recursive merge on a key like `__proto__` changes Object.prototype. The bug matters only when a later sink reads the polluted key.

## Test

Send the key through every merge. Read a property the sink uses. Trace the polluted value to the sink.

## Proof

A changed behavior from the polluted property.

## Failure modes

A null prototype object blocks it. A later assignment overwrites the value.
