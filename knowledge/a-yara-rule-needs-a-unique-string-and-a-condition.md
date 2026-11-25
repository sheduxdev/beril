---
id: a-yara-rule-needs-a-unique-string-and-a-condition
title: A YARA rule needs a unique string and a condition
tags: malware, yara, detection
confidence: high
updated: 2026-11-26
uses: 0
sources: references/reverse-engineering.md, knowledge/detection-sigma.md
status: active
---
# A YARA rule needs a unique string and a condition

## Claim

A rule with a common string and a bare match fires everywhere. The condition needs the count, the offset or the file type.

## Test

Run the rule on a clean corpus and on the sample. Count the false hits. Tighten the condition.

## Proof

The sample hits and the clean corpus stays quiet.

## Failure modes

A unique string can be packed away. A narrow rule can miss a variant.
