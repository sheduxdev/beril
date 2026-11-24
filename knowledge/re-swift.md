---
id: re-swift
title: Swift uses witness tables and value types
tags: re, swift, ios
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/mobile-reverse.md
status: active
---
# Swift uses witness tables and value types

## Claim

Methods dispatch through witness tables; structs and enums have layouts that differ from Objective-C.

## Test

Demangle symbols. Find witness tables. Map the value layout before reading a method.

## Proof

A recovered protocol method and a correct field layout.

## Failure modes

Objective-C bridging hides some calls. Swift name mangling changes by version.
