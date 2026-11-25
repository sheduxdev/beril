---
id: ruby-marshal-is-code-with-a-gadget
title: Ruby Marshal is code with a gadget
tags: lang, ruby, deser
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/web-deserialization-gadget.md
status: active
---
# Ruby Marshal is code with a gadget

## Claim

`Marshal.load` on untrusted bytes instantiates objects and can call a gadget on the loaded classes.

## Test

Find Marshal load. Enumerate the gems. Build a chain with a known gadget and a callback.

## Proof

A callback or a command.

## Failure modes

A signed cookie can be trusted. A JSON path removes the risk.
