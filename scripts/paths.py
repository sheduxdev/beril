#!/usr/bin/env python3
"""Resolve data, references and docs in a checkout or an installed wheel.

Beril runs from a git checkout and from a pip or pipx install. In a checkout
the files sit at the repository root. A wheel installs them under
``$PREFIX/share/beril``. Environment variables win over both for unusual
deployments.

    from paths import DATA, REFERENCES
"""

from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def locate(name: str, variable: str) -> str:
    override = os.environ.get(variable, "")
    if override:
        return override
    beside = os.path.join(HERE, name)
    if os.path.isdir(beside):
        return beside
    share = os.path.join(sys.prefix, "share", "beril", name)
    if os.path.isdir(share):
        return share
    return os.path.join(ROOT, name)


DATA = locate("data", "BERIL_DATA")
REFERENCES = locate("references", "BERIL_REFERENCES")
DOCS = locate("docs", "BERIL_DOCS")
BENCHMARKS = locate("benchmarks", "BERIL_BENCHMARKS")
LABS = locate("labs", "BERIL_LABS")
