---
id: cargo-build-scripts-run-before-the-crate
title: Cargo build scripts run before the crate
tags: pkg, cargo, build-script
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Cargo build scripts run before the crate

## Claim

A `build.rs` runs with the user rights and can read the environment, the files and the network.

## Test

Read the build script and the crate. Build in a clean container. Watch the network and the file access.

## Proof

A build script side effect.

## Failure modes

A vendored crate and a review block it. A build script can be conditional.
