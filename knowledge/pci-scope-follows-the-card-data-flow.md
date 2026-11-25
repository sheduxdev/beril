---
id: pci-scope-follows-the-card-data-flow
title: PCI scope follows the card data flow
tags: comp, pci, scope
confidence: medium
updated: 2026-11-26
uses: 0
sources: docs/legal.md
status: active
---
# PCI scope follows the card data flow

## Claim

The cardholder data environment is every system that stores, processes or transmits the number, and every system that can reach one.

## Test

Draw the card data flow. Mark the stores and the reachable hosts. Compare with the stated scope.

## Proof

A host in the flow outside the stated scope.

## Failure modes

A tokenization service shrinks the scope. A segmentation test can remove a host.
