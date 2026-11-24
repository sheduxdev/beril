---
id: hardware-sidechannel
title: Side channels leak through power, timing or EM
tags: hardware, sidechannel
confidence: low
updated: 2026-11-24
uses: 0
sources: references/firmware-iot.md
status: active
---
# Side channels leak through power, timing or EM

## Claim

A secret-dependent branch or memory access produces a measurable difference.

## Test

Collect traces with a known input. Align. Compare the difference between hypotheses.

## Proof

A correlation peak that reveals a key byte.

## Failure modes

Noise and misalignment can hide the signal. A lab bench is required.
