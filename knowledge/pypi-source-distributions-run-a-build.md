---
id: pypi-source-distributions-run-a-build
title: PyPI source distributions run a build
tags: pkg, pypi, build
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# PyPI source distributions run a build

## Claim

A source distribution executes `setup.py` or a build backend on install. A wheel can still run a script.

## Test

Download the sdist. Read `setup.py` and `pyproject.toml`. Install in a clean container and watch the process tree.

## Proof

A build time command.

## Failure modes

A wheel with no script skips the build. A hash pin catches a changed file.
