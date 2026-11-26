---
id: defense-rce-blast-radius
title: RCE impact is the rights of the process that runs it
tags: defense, rce, hardening, least-privilege
confidence: high
updated: 2026-11-26
uses: 0
sources: https://attack.mitre.org/techniques/T1190/, https://d3fend.mitre.org/, https://docs.docker.com/engine/security/seccomp/
status: active
---
# RCE impact is the rights of the process that runs it

## Claim

Code execution inherits the user, filesystem, secrets, network and syscalls of the service. Hardening limits what the next step can do.

## Test

For each internet-facing service, record the user, writable paths, mounted secrets, egress rules and seccomp or AppArmor profile.

## Proof

A non-root user, a read-only root filesystem, no default egress and a syscall filter, checked from inside the service.

## Failure modes

A container with the Docker socket or host mounts is not isolated. Blocking egress does not stop data reaching a writable web root.
