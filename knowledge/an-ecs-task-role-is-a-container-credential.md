---
id: an-ecs-task-role-is-a-container-credential
title: An ECS task role is a container credential
tags: aws, ecs, role
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-metadata-role.md
status: active
---
# An ECS task role is a container credential

## Claim

The task metadata endpoint returns the task role credentials to any process in the container.

## Test

Request `169.254.170.2` from the task. Read the role name and the credentials path. Call STS.

## Proof

Temporary credentials for the task role.

## Failure modes

A restricted network policy can block the endpoint. A read only role limits the use.
