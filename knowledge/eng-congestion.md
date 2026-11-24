---
id: eng-congestion
title: Congestion control is a queue management problem
tags: engineering, network, congestion
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Congestion control is a queue management problem

## Claim

Loss, delay and buffer size decide throughput. A deep buffer adds latency before it drops.

## Test

Measure RTT under load. Check the queue and the congestion algorithm.

## Proof

A latency curve that stays flat until the link is full.

## Failure modes

A bandwidth test alone hides bufferbloat. AQM changes the curve.
