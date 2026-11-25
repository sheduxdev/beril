---
id: apf-is-the-authorized-program-list
title: APF is the authorized program list
tags: mf, apf, library
confidence: low
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# APF is the authorized program list

## Claim

A program in an APF library runs with elevated authority. A write to the library is a path to system code.

## Test

List the APF libraries. Check the write rights. Add a test module and call it.

## Proof

A module from the APF list running.

## Failure modes

A library can be protected and a load needs a refresh. A module can fail the signature.
