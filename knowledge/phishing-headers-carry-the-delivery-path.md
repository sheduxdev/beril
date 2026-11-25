---
id: phishing-headers-carry-the-delivery-path
title: Phishing headers carry the delivery path
tags: ir, phishing, headers
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ir-phishing.md
status: active
---
# Phishing headers carry the delivery path

## Claim

Received, Message-ID, Return-Path and auth results show the sending infrastructure and the failing checks.

## Test

Copy the full headers. Parse the Received chain from the bottom. Check SPF, DKIM and DMARC results and the Return-Path domain.

## Proof

A delivery path and an auth failure tied to the message.

## Failure modes

A forwarder rewrites the chain. A compromised legitimate account passes auth.
