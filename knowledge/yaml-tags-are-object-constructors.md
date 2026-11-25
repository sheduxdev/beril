---
id: yaml-tags-are-object-constructors
title: YAML tags are object constructors
tags: lang, yaml, deser
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/web-deserialization-gadget.md
status: active
---
# YAML tags are object constructors

## Claim

A YAML tag names a class. A loader that resolves tags can build an object with side effects.

## Test

Find the loader. Send `!!python/object` or a language tag. Check the loader and the result.

## Proof

An object or a command from the document.

## Failure modes

A safe loader blocks the tags. A custom constructor can add them back.
