---
id: jcl-is-a-batch-program-and-a-dataset-list
title: JCL is a batch program and a dataset list
tags: mf, jcl, batch
confidence: low
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# JCL is a batch program and a dataset list

## Claim

A JCL job names a program and the datasets. A write to a PROCLIB or a job card can run a program.

## Test

Read a sample job. Check the dataset rights. Submit a job with a test program.

## Proof

A job output with the program result.

## Failure modes

A job class or a queue can delay it. A PROCLIB can be protected.
