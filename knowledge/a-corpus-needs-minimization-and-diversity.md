---
id: a-corpus-needs-minimization-and-diversity
title: A corpus needs minimization and diversity
tags: fuzz, corpus, minimize
confidence: high
updated: 2026-11-26
uses: 0
sources: references/fuzzing.md
status: active
---
# A corpus needs minimization and diversity

## Claim

A huge corpus slows every run. A minimized set keeps the edges with fewer bytes.

## Test

Run the corpus through the minimizer. Compare edges and size. Keep the seeds that add an edge.

## Proof

The same edge coverage at a fraction of the size.

## Failure modes

A minimizer can drop a rare path. Deep seeds can be needed for a grammar.
