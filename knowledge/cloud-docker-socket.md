---
id: cloud-docker-socket
title: A mounted Docker socket is root on the host
tags: cloud, docker, container
confidence: medium
updated: 2026-11-24
uses: 0
sources: labs/cloud
status: active
---
# A mounted Docker socket is root on the host

## Claim

The container mounts /var/run/docker.sock or runs privileged, so it can create a host-mounted container.

## Test

Check mounts and capabilities. Run a short container with / mounted and read a host file.

## Proof

A host file read or written from a container you control.

## Failure modes

A TCP socket with TLS and auth is weaker. A socket proxy with a narrow API may limit impact.
