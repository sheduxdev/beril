---
id: re-dotnet-aot
title: Native AOT is not IL
tags: re, dotnet, aot
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/reverse-engineering.md
status: active
---
# Native AOT is not IL

## Claim

The binary is native code with metadata tables and method pointers. IL tools see little.

## Test

Find the metadata and method table. Use a NativeAOT-aware plugin. Map the method pointer table.

## Proof

A method name and a body address.

## Failure modes

A trimmed AOT image may drop names. Check the runtime version.
