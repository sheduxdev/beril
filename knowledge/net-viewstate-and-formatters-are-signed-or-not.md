---
id: net-viewstate-and-formatters-are-signed-or-not
title: .NET viewstate and formatters are signed or not
tags: lang, dotnet, deser
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/re-dotnet-aot.md
status: active
---
# .NET viewstate and formatters are signed or not

## Claim

ViewState without MAC or with a known machine key accepts a crafted object. BinaryFormatter is the same class.

## Test

Decode the ViewState. Check the MAC flag. Test a known machine key and a formatter payload.

## Proof

A callback or a command from the object.

## Failure modes

A random machine key and MAC on hold. A signed viewstate can still have a gadget.
