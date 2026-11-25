---
id: magisk-is-a-user-space-root-with-a-module-system
title: Magisk is a user space root with a module system
tags: android, magisk, root
confidence: high
updated: 2026-11-26
uses: 0
sources: references/mobile-reverse.md
status: active
---
# Magisk is a user space root with a module system

## Claim

Magisk patches the boot image and mounts a overlay. DenyList and Zygisk hide or inject per process.

## Test

Read the Magisk state and the modules. Add the target to DenyList. Check the process mount and the root view.

## Proof

A hidden root state for the target process.

## Failure modes

A hardware check and an integrity verdict can still fail. A module can break the boot.
