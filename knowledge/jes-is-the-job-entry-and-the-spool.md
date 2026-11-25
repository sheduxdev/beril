---
id: jes-is-the-job-entry-and-the-spool
title: JES is the job entry and the spool
tags: mf, jes, spool
confidence: low
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# JES is the job entry and the spool

## Claim

The spool holds the job output and the input. A readable spool can leak data from other users.

## Test

List the spool with the current id. Try another user's job. Read the output.

## Proof

A job output outside the user.

## Failure modes

A spool can be purged quickly. A class can restrict the view.
