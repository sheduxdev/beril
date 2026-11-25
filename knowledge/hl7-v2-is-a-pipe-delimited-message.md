---
id: hl7-v2-is-a-pipe-delimited-message
title: HL7 v2 is a pipe delimited message
tags: med, hl7, interface
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/network-protection.md
status: active
---
# HL7 v2 is a pipe delimited message

## Claim

The message has segments and fields over MLLP. A raw interface often has no auth and no schema check.

## Test

Find the MLLP port. Send a minimal ADT message. Read the ACK.

## Proof

An ACK from the interface.

## Failure modes

A TLS wrapper or an allowlist blocks it. A vendor can require a header.
