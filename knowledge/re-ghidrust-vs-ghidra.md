---
id: re-ghidrust-vs-ghidra
title: GhidRust is a paused Ghidra plugin, not Ghidrust
tags: re, ghidra, rust
confidence: high
updated: 2026-11-24
uses: 0
sources: references/ghidra-ecosystem.md, references/rust-reverse.md
status: active
---
# GhidRust is a paused Ghidra plugin, not Ghidrust

## Claim

DMaroo/GhidRust is a Ghidra extension for Rust binaries. oofz/Ghidrust is a separate Rust-native platform. Ghidra upstream Rust support is now better than the plugin.

## Test

Check the repo. Use GhidRust for its libstd FunctionID only when the Rust version matches. Use Ghidrust when you need a headless CLI/MCP.

## Proof

A function named by FunctionID, or a clean build from source.

## Failure modes

The C-to-Rust view is flaky. Do not present it as source.
