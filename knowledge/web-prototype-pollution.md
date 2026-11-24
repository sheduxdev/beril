---
id: web-prototype-pollution
title: Prototype pollution needs a merge sink and a gadget
tags: web, javascript, prototype
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Prototype pollution needs a merge sink and a gadget

## Claim

A recursive merge writes __proto__ or constructor.prototype, and a later lookup reads an inherited property.

## Test

Send __proto__ and constructor.prototype objects to JSON merge endpoints. Look for a gadget in config or auth.

## Proof

An inherited property changes behavior, such as a role or a header.

## Failure modes

A polluted Object.prototype without a gadget has no impact. JSON.parse alone does not pollute.
