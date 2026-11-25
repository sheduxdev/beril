---
id: an-s3-acl-is-a-separate-grant-from-the-bucket-policy
title: An S3 ACL is a separate grant from the bucket policy
tags: aws, s3, acl
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-iam-wildcard.md
status: active
---
# An S3 ACL is a separate grant from the bucket policy

## Claim

Object and bucket ACLs can grant public read or write even when the bucket policy is private, and Block Public Access can be partial.

## Test

Read the ACL and the public access block. Fetch the object anonymously. Try a public write ACL.

## Proof

An anonymous read or write.

## Failure modes

A full public access block overrides the ACL. An ACL disabled bucket ignores it.
