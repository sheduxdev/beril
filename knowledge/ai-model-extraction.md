---
id: ai-model-extraction
title: Model extraction is a query budget problem
tags: ai, model, extraction
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Model extraction is a query budget problem

## Claim

An API returns enough probability or logit detail to train a substitute model, or leaks the model family.

## Test

Query a grid of inputs. Measure the output detail. Train a small surrogate and compare.

## Proof

A surrogate that matches the target on held-out inputs.

## Failure modes

Top-1 labels alone are weak. Rate limits change the cost.
