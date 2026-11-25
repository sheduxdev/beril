---
id: python-deserialization-is-pickle-and-yaml
title: Python deserialization is pickle and YAML
tags: lang, python, deser
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/web-deserialization-gadget.md
status: active
---
# Python deserialization is pickle and YAML

## Claim

`pickle.loads` and `yaml.load` without SafeLoader execute object constructors. JSON is data only.

## Test

Find every load. Check the loader. Send a crafted pickle and a YAML with a tag.

## Proof

A command or a file read from the object.

## Failure modes

A signed pickle can be trusted. A safe loader blocks it.
