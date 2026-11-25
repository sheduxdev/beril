---
id: vex-not-affected-needs-a-justification
title: VEX not affected needs a justification
tags: supply, vex, triage
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# VEX not affected needs a justification

## Claim

A not affected VEX entry without a reason is a suppression. The reason must name the vulnerable code path or the build flag.

## Test

Read the VEX entry. Check the justification field. Verify it against the package source and the build.

## Proof

A justification that names the missing function or the disabled feature.

## Failure modes

A generic not affected from a vendor can be wrong for your build. A reachability tool can disagree.
