---
id: the-docker-socket-is-host-root
title: The Docker socket is host root
tags: linux, docker, socket
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-docker-socket.md
status: active
---
# The Docker socket is host root

## Claim

Write access to `/var/run/docker.sock` lets a user run a privileged container with a host mount.

## Test

Check the socket owner and group. Run a container with `-v /:/host` and chroot.

## Proof

A host file read or a host shell.

## Failure modes

A rootless daemon changes the path. A socket proxy can restrict calls.
