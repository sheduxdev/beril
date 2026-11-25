---
id: template-sandbox-escape-starts-at-the-object-graph
title: Template sandbox escape starts at the object graph
tags: rce, ssti, sandbox
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/rce-mastery.md
status: active
---
# Template sandbox escape starts at the object graph

## Claim

A confirmed SSTI is not RCE until an object path reaches import, process or a class loader. The path differs by engine and version.

## Test

Enumerate config, self, cycler, lipsum or app.request. Walk to a module loader, then call a process function with a read only command.

## Proof

Command output or callback from the escaped template.

## Failure modes

The sandbox exposes values but blocks callables. The version backport changes the gadget. Output is truncated.
