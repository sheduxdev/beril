---
id: re-macho
title: Mach-O is a set of load commands, not a PE
tags: re, macho, macos
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/reverse-engineering.md
status: active
---
# Mach-O is a set of load commands, not a PE

## Claim

Sections, segments, fat slices and entitlements carry the structure. Objective-C metadata is in dedicated sections.

## Test

Parse load commands and slices. Map __TEXT, __DATA and Objective-C sections. Check the entitlements.

## Proof

A recovered class or method and a correct segment map.

## Failure modes

A fat binary needs the right slice. Stripping symbols keeps Objective-C metadata.
