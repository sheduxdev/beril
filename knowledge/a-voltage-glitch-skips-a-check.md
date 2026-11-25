---
id: a-voltage-glitch-skips-a-check
title: A voltage glitch skips a check
tags: hardware, glitch, fault
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/firmware-iot.md
status: active
---
# A voltage glitch skips a check

## Claim

A short dip on the core rail at the right offset skips an instruction or corrupts a read, which can bypass a signature or a password check.

## Test

Find the check trigger. Sweep the offset and the width. Watch the output for a pass or a different fault.

## Proof

A repeatable pass with a fixed offset and width.

## Failure modes

A brownout reset hides the effect. A glitch can corrupt the state in a different way.
