# Engineering mastery

Forty years of engineering is not a list of tools. It is a set of judgments about scope, failure, data, people and time. This file is the working model behind the engineering cards.

## What senior means

A senior engineer:

- Finds the real problem before choosing a solution.
- Names the tradeoff in one sentence.
- Designs for the failure, not the happy path.
- Leaves the system easier to change than they found it.
- Writes for the next person, not for the compiler.
- Knows what not to build.
- Says "I do not know" before inventing a fact.
- Makes the smallest change that resolves the risk.

## Twenty laws

1. **Essential vs accidental.** Most complexity is introduced by the solution, not the problem. Remove accidental complexity first.
2. **Data outlives code.** The schema, identifiers and event names survive rewrites. Spend time there.
3. **Boundaries beat layers.** A good boundary hides a decision. A layer that only forwards calls adds cost.
4. **Contracts are promises.** Inputs, outputs, errors and timing are part of the API. Version them.
5. **Failure is the normal path.** Networks drop, disks fill, clocks skew, users retry. Design the failure mode.
6. **Idempotency is a feature.** Every write that can be retried needs a key or a natural unique constraint.
7. **Backpressure is kindness.** A queue without a limit is a memory leak with a schedule.
8. **Timeouts are part of correctness.** A call without a deadline can hang a pool.
9. **Observability is a product.** Logs, metrics and traces answer questions a user will ask at 3 a.m.
10. **Tests are a design tool.** Hard-to-test code is usually hard-to-use code.
11. **Simplicity is a budget.** Every abstraction costs a reader. Make it earn the cost.
12. **Deletion is a feature.** Dead code, flags and services are liabilities.
13. **Reversibility reduces risk.** A small deploy, a flag, a migration that can roll back.
14. **Migrations are a sequence, not a switch.** Expand, backfill, switch, contract.
15. **Coupling is the enemy.** A change should not require a tour of the system.
16. **Performance is a budget.** Name the p95, the payload and the cost before optimizing.
17. **Security is a property of the design.** A check at the edge is not a boundary if another path exists.
18. **Communication is engineering.** A decision nobody understands is a future incident.
19. **Estimates are ranges.** A point estimate hides the uncertainty that matters.
20. **Mentoring is leverage.** A team that learns faster ships safer.

## Decision tables

### Monolith or service

| Signal | Monolith | Service |
|---|---|---|
| One team, one deploy | Yes | No |
| Clear domain boundary | Optional | Yes |
| Independent scaling | No | Yes |
| Strong transactional consistency | Yes | Hard |
| Small team, early product | Yes | Usually no |

Default to a modular monolith. Split when a boundary, a team or a scaling need is real.

### SQL or document store

| Need | SQL | Document |
|---|---|---|
| Joins and ad hoc queries | Yes | Weak |
| Flexible nested documents | Weak | Yes |
| Strict schema and constraints | Yes | Optional |
| Horizontal write scale | Hard | Easier |
| Reporting | Yes | Usually no |

Use a relational database until the access pattern proves otherwise.

### Sync or async

| Condition | Sync | Async |
|---|---|---|
| User waits for the result | Yes | No |
| Work is slow or retryable | No | Yes |
| Strong immediate consistency | Yes | No |
| Fan-out to many consumers | No | Yes |
| Failure needs a durable retry | No | Yes |

### Cache

Cache when the read is hot, the source is slow, and staleness is acceptable. Name the key, the TTL, the invalidation path and the miss cost. A cache without an invalidation story is a bug factory.

### Queue or direct call

Use a queue when the producer should not wait, the work can be retried, or the consumer scales separately. Use a direct call when the caller needs the result or the failure must be immediate.

## Design review questions

1. What is the one sentence problem?
2. Who is the user and what do they do today?
3. What is the smallest useful version?
4. What are the inputs, outputs and errors?
5. Where is the source of truth?
6. What happens on retry, timeout, duplicate and partial failure?
7. What is the data model, and what is the migration path?
8. What is the boundary, and what does each side own?
9. What is the failure mode when a dependency is down?
10. How will we know it works in production?
11. What is the rollback?
12. What are we deliberately not doing?

## Debugging method

1. Reproduce. Write the smallest failing case.
2. State the expected and actual behavior.
3. Form one hypothesis. Predict the observation.
4. Test the hypothesis with the least invasive probe.
5. Bisect the space: commits, inputs, configuration, layers.
6. Fix the cause, not the symptom.
7. Add a regression test that fails before the fix.
8. Remove the debug scaffolding.

Do not change two variables at once. Do not trust a cache without clearing it.

## Performance method

1. Define the budget: p50, p95, payload, memory, cost.
2. Measure before changing.
3. Find the dominant term, not the most familiar one.
4. Optimize the algorithm before the constant.
5. Re-measure with the same workload.
6. Keep a benchmark in CI for the critical path.
7. Stop when the budget is met.

## Incident method

1. Stabilize first: rollback, flag off, drain, fail over.
2. Assign one incident commander and one scribe.
3. Keep a timestamped log with decisions.
4. Communicate a short status at a fixed cadence.
5. Fix the cause after stability, not during.
6. Write a blameless postmortem with actions and owners.
7. Verify each action closed.

## Code review checklist

- The change does what the description says.
- The smallest change was chosen.
- Errors, retries and partial failures are handled.
- Inputs are validated at the boundary.
- The data model and migration are safe.
- Tests cover the new behavior and the regression.
- Logging and metrics answer the next question.
- Naming and structure match the codebase.
- No secret, debug artifact or dead flag.
- The rollback is clear.

## Estimation

Give a range and the assumptions. Separate known work, unknown work and coordination. A good estimate names the risk that could double it.

## Legacy

Do not rewrite the whole system. Find a seam, wrap it, test it, move one behavior, repeat. The strangler pattern works because it leaves the old path alive until the new one is proven.

## Mentoring

Ask, do not tell, until the blocker is clear. Give the smallest hint that unblocks. Make the learner produce the evidence. Review the work, not the person.

## Engineering gaps

The knowledge cards cover the durable judgment. The gaps list tracks what is still missing: distributed consensus, query planning, type systems, compilers, operating systems, networking, ML systems, SRE, accessibility, i18n and cost engineering.
