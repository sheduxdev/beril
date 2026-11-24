---
id: hw-endian
title: Byte order is part of the wire format
tags: hardware, endian, layout
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Byte order is part of the wire format

## Claim

The protocol fixes an order; the host may differ. A struct written raw depends on padding and endianness.

## Test

Serialize a struct on both endians. Compare the bytes and the size.

## Proof

A byte-identical encoding across hosts.

## Failure modes

A raw struct write includes padding. A missing byteswap corrupts a field.
