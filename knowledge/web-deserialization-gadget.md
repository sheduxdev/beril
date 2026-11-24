---
id: web-deserialization-gadget
title: Native deserialization is RCE when a gadget chain exists
tags: web, deserialization, rce
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Native deserialization is RCE when a gadget chain exists

## Claim

Untrusted bytes reach pickle, unserialize, ObjectInputStream or a .NET formatter, with a gadget on the classpath.

## Test

Identify the format and a magic prefix. Send a minimal object. Build a chain only after the format is confirmed.

## Proof

A callback or command from a crafted object.

## Failure modes

Base64 is not a format check. A serialized object with no gadget may only be a DoS.
