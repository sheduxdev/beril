---
id: a-pcb-trace-is-a-test-point
title: A PCB trace is a test point
tags: hardware, pcb, trace
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/firmware-iot.md
status: active
---
# A PCB trace is a test point

## Claim

A labeled test pad or a via on a trace carries the signal without a connector. The label and the net are the map.

## Test

Photograph both sides. Follow the net with a continuity test. Solder a fine wire to the via.

## Proof

A stable signal on the analyzer.

## Failure modes

A buried trace needs a via. A ground plane can make continuity ambiguous.
