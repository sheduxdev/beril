---
id: mobile-swift
title: Swift hooks need mangled names or a bridge
tags: mobile, ios, swift
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/mobile-reverse.md
status: active
---
# Swift hooks need mangled names or a bridge

## Claim

Swift methods are not Objective-C selectors. A hook needs the mangled symbol or a Swift-aware API.

## Test

List classes and methods. Hook a Swift method with Frida's Swift bridge or the mangled name.

## Proof

A logged argument or return from the Swift method.

## Failure modes

A method exposed to Objective-C can be hooked by selector. Pure Swift needs more.
