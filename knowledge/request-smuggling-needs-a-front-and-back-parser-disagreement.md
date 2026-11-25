---
id: request-smuggling-needs-a-front-and-back-parser-disagreement
title: Request smuggling needs a front and back parser disagreement
tags: web, desync, smuggling
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/web-desync-parser-disagreement.md, references/techniques.md
status: active
---
# Request smuggling needs a front and back parser disagreement

## Claim

CL.TE or TE.CL disagreement lets a second request ride inside the first and reach the wrong user or the admin path.

## Test

Send the four timing probes with CL and TE combinations. Confirm with a queued request to a canary path.

## Proof

The smuggled request executes on the next connection.

## Failure modes

A single proxy or HTTP/2 end to end can hide it. Timeout based proof is noisy.
