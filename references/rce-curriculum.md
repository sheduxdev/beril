# RCE curriculum, six weeks

A focused track for a tester who already knows HTTP, a proxy and one scripting
language. Ten hours a week, two hours a day. Each day ends with an artifact.
Each week ends with a reproduction that someone else can rerun.

Read `references/rce-mastery.md` first. Use `labs/rce` for the local target.
Use PortSwigger labs for the classes the local lab does not cover.

Rules.

1. One class at a time. No class hopping inside a day.
2. Every payload has a hypothesis before it is sent.
3. The first proof is read only.
4. Record the request, the response and the time.
5. Repeat every blind proof once.
6. Stop at the agreed rung of the proof ladder.
7. Publish one writeup at the end of weeks 3 and 6.

## Week 1, how execution happens

Outcome. You can name the sink, the transform and the missing check in four
languages.

| Day | Work | Artifact |
|---|---|---|
| 1 | Read the source to sink section. List 20 sinks across Python, Node, PHP and Java | Sink sheet |
| 2 | Trace three sinks in an open source app. Mark the transform on each path | Three traces |
| 3 | Run `labs/rce` command endpoint. Send the arithmetic marker, then `id` | Request pair |
| 4 | Break the concat sink four ways. Quote, no quote, space, slash | Four payloads and the fix |
| 5 | Write the source to sink checklist. Review it with a peer | Checklist v1 |

Checkpoint. A peer picks one trace and you explain the transform without the
notes.

## Week 2, command injection

Outcome. You can prove and report a shell expansion without a reverse shell.

| Day | Work | Artifact |
|---|---|---|
| 1 | PortSwigger OS command injection, first three labs | Lab notes |
| 2 | Blind endpoint in `labs/rce`. Prove with time, then with a file write | Timing table, file path |
| 3 | Build a DNS callback. Send one token per request | Resolver log |
| 4 | Filter drill. Blocked space, blocked slash, blocked separator | Bypass table |
| 5 | Write the report for the lab command injection | One page report |

Checkpoint. Report has a request pair, the sink, the missing check and a code
level fix.

## Week 3, templates and expressions

Outcome. You can fingerprint a template family and reach a command in a
sandboxed engine.

| Day | Work | Artifact |
|---|---|---|
| 1 | Fingerprint six engines with arithmetic only | Engine table |
| 2 | Jinja2 sandbox escape in a local app. Reach `os.popen` | Payload and output |
| 3 | Twig escape. Reach a filter chain, then a command | Payload and output |
| 4 | SpEL and OGNL class reference. One lab each | Request pairs |
| 5 | Write the SSTI writeup. Include the version and the sandbox limit | Public writeup draft |

Checkpoint. You can explain why rung 1 is not RCE and show rung 2.

## Week 4, deserialization and file include

Outcome. You can identify a format, build a gadget and turn a read into
execution.

| Day | Work | Artifact |
|---|---|---|
| 1 | Format identification drill. Java, PHP, Python, .NET blobs | Format sheet |
| 2 | Pickle payload by hand. Explain `__reduce__` | Payload and note |
| 3 | Java gadget with ysoserial. DNS callback first, command second | Callback log |
| 4 | LFI in `labs/rce`. Read a file, poison a log, execute | Request chain |
| 5 | Upload plus LFI chain. Prove execution from the stored file | Chain diagram |

Checkpoint. Every step has a request and a response. The chain has no assumed
path.

## Week 5, database, SSRF and dependencies

Outcome. You can judge whether a lower severity primitive can become execution.

| Day | Work | Artifact |
|---|---|---|
| 1 | MSSQL `xp_cmdshell` lab. Check the disabled state first | State evidence |
| 2 | PostgreSQL `COPY FROM PROGRAM` and MySQL `INTO OUTFILE` | Two payloads |
| 3 | SSRF to Redis and to Docker API in a local compose stack | Two chains |
| 4 | Pick one recent CVE. Reduce the PoC to a one line check | One line check |
| 5 | Write a decision table for primitive to execution | Decision table |

Checkpoint. For each primitive you can say the precondition that fails and the
precondition that succeeds.

## Week 6, blind proof, tooling and capstone

Outcome. A complete RCE report on a target you have not seen.

| Day | Work | Artifact |
|---|---|---|
| 1 | Blind proof drill. DNS, HTTP and file channel | Three proofs |
| 2 | Build a small encoder. URL, base64, `IFS`, brace expansion | Tool and tests |
| 3 | Audit one Java app. Keep every sink trace | Trace bundle |
| 4 | Capstone. Fresh target, full chain, time box four hours | Report draft |
| 5 | Peer review. Fix the weakest proof and the weakest sentence | Final report |

Checkpoint. A reviewer reruns the chain from the report alone.

## Assessment

Score reach, proof, safety and report from 0 to 3. Nine or more means pass.
Five to eight means repeat the week with a new target. Below five means return
to week 1.

## Reading by week

| Week | Primary |
|---|---|
| 1 | OWASP WSTG injection sections, language sink docs |
| 2 | PortSwigger command injection, `PayloadsAllTheThings` |
| 3 | PortSwigger SSTI, engine sandbox docs |
| 4 | ysoserial and phpggc READMEs, LFI to RCE writeups |
| 5 | DB docs, `InternalAllTheThings`, vendor advisories |
| 6 | Project Zero, Assetnote, disclosed RCE reports |

## After the track

Keep one RCE lab per month. Diff one patched app per month. Add every new sink
to the checklist. The field moves through dependencies and parsers, not through
new separators.
