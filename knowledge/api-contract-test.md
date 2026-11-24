---
id: api-contract-test
title: A consumer contract catches a break before deploy
tags: api-design, contract, testing
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A consumer contract catches a break before deploy

## Claim

The consumer records the requests it makes; the provider verifies them in its pipeline.

## Test

Change a response field. Run the provider verification.

## Proof

A failing contract test before the deploy.

## Failure modes

A contract that pins every field blocks evolution. A contract with no provider run is a document.
