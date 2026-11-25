---
id: sqli-to-rce-needs-a-file-or-execution-right
title: SQLi to RCE needs a file or execution right
tags: rce, sqli, database
confidence: high
updated: 2026-11-26
uses: 0
sources: references/rce-mastery.md
status: active
---
# SQLi to RCE needs a file or execution right

## Claim

Stacked queries are not enough. MSSQL needs xp_cmdshell or OLE, PostgreSQL needs COPY FROM PROGRAM or an untrusted language, MySQL needs a writable web root or a UDF.

## Test

Check the DB version, the current user and the relevant setting before a payload. Prefer a command output over a file write.

## Proof

Command output, callback, or a written file that executes.

## Failure modes

secure_file_priv blocks writes. xp_cmdshell is disabled. The DB host cannot write to the app host.
