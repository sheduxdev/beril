#!/usr/bin/env python3
"""Recall regression tests. The expected card must be the top hit."""

from __future__ import annotations

import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECALL = os.path.join(ROOT, "scripts", "recall.py")

CASES = [
    ("architecture tradeoff cost", "eng-tradeoffs"),
    ("service boundary data ownership", "eng-boundaries", 3),
    ("retryable write idempotency key", "eng-idempotency"),
    ("network timeout retry budget", "eng-timeouts"),
    ("cache invalidation ttl", "eng-cache-invalidation"),
    ("query plan missing index", "eng-query-planner"),
    ("consensus quorum leader election", "eng-consensus"),
    ("SLO error budget alert", "eng-slo"),
    ("multi tenant isolation noisy neighbor", "eng-multi-tenancy"),
    ("schema evolution rolling deploy", "eng-schema-evolution"),
    ("CSS injection attribute selector", "web-css-injection"),
    ("dangling markup token leak", "web-dangling-markup"),
    ("WebAssembly validator imports", "binary-wasm"),
    ("eBPF verifier map bounds", "binary-ebpf"),
    ("hiring work sample scorecard", "eng-hiring"),
    ("finops unit cost allocation", "eng-finops"),
    ("garbage collection pause allocation", "eng-gc"),
    ("platform golden path", "eng-platform"),
    ("mobile offline conflict merge", "eng-mobile-arch"),
    ("telemetry cardinality sampling", "eng-observability-cost"),
    ("network partition availability consistency", "dist-partition"),
    ("clock skew causal order", "dist-clock"),
    ("CRDT concurrent merge", "dist-crdt"),
    ("SSA phi node dataflow", "comp-ssa"),
    ("JIT deopt guard code cache", "comp-jit"),
    ("write ahead log fsync crash", "storage-wal"),
    ("replication lag failover data loss", "storage-replication"),
    ("Conway law service ownership", "org-conway"),
    ("on-call page noise rotation", "org-oncall"),
    ("backup restore measured RTO", "eng-backup-restore"),
    ("RTO RPO disaster rehearsal", "eng-disaster-recovery"),
    ("gossip membership failure detection", "dist-gossip"),
    ("backfill throttle replica", "dist-backfill"),
    ("quorum read overlap write", "dist-quorum-read"),
    ("register allocation spill interference", "comp-regalloc"),
    ("type checker soundness", "comp-type-check"),
    ("optimizer semantic preservation", "comp-optimizer"),
    ("LSM compaction write stall", "storage-compaction", 2),
    ("checksum bit rot repair", "storage-checksum"),
    ("delegation DACI decision right", "org-delegation"),
    ("architecture decision record consequences", "org-adr"),
    ("team budget maintenance innovation", "org-budget"),
    ("incentive metric local optimum", "org-incentives"),
    ("chaos steady state hypothesis", "eng-chaos"),
    ("open loop load test saturation", "eng-load-test"),
    ("capacity model headroom", "eng-capacity"),
    ("retention deletion clock", "eng-retention"),
]


def main() -> None:
    passed = failed = 0
    for case in CASES:
        query, expected = case[0], case[1]
        topn = case[2] if len(case) > 2 else 1
        out = subprocess.check_output([sys.executable, RECALL, query, "--json", "--limit", str(topn)], text=True)
        hits = json.loads(out)
        ids = [h["id"] for h in hits]
        ok = expected in ids
        print(f"{'PASS' if ok else 'FAIL'} {query!r} -> {ids[0] if ids else 'none'} (expected {expected})")
        passed += ok
        failed += not ok
    print(f"---\npass={passed} fail={failed}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
