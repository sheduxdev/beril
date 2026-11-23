# Bug hunt line

This line looks for unknown bugs in an open source repository. The target is a
local clone, not the user's production system. It uses a networkless sandbox,
sanitizers and the smallest reproduction. It does not build a working exploit.

## Loop

1. Fingerprint: language, build system, tests, CI, history.
2. Known bug matching: dependencies and OSV.
3. Source rules: TLS, eval, CORS, deserialisation, shell, SQL.
4. History reading: security words in commits, silent patches.
5. Structural risk: fan-in, swallowed error density.
6. Sandbox: networkless build, run with sanitizers.
7. Verification level and dedupe.
8. Maintainer report and coordinated disclosure.

## Command

```bash
./beril hunt --target ./repo
./beril hunt --target ./repo --sandbox --timebox 300
./beril hunt --target ./repo --fuzz --report HUNT.md
```

The output uses the `maintainer` profile: file, line, smallest reproduction,
severity reason and patch suggestion.

## Verification levels

| Level | Evidence | Report |
|---|---|---|
| Candidate | Pattern, line, data flow reading | Yes, low confidence |
| Reproduced | Sandbox output, sanitizer signature | Yes |
| Verified | A human got the same result | Yes, high confidence |

No line without reproduction evidence is ever marked verified. A sanitizer
signature is a real finding. Exploitability is a separate sentence.

## Sandbox

```bash
./scripts/sandbox.sh --target ./repo --lang c --dry-run
./beril hunt --target ./repo --sandbox
```

Rules:

- `--network none`
- Source `:ro`, work copy on tmpfs
- `--cap-drop ALL`, `no-new-privileges`
- 1 GB memory, 1 CPU, 256 pids
- A fixed image per language

A container is not a hypervisor. Keep Docker current and remember that the host
kernel is shared. Use a VM for a suspicious binary.

## Dedupe

The first five frames of the same sanitizer signature are hashed
(`crash-<hash>`). The same hash is not added twice. Different inputs on the same
root cause merge into one finding.

Volume cap: at most 5 reports per project. The rest is kept as an appendix.

## Maintainer report

The `references/maintainer-report.md` template:

- Affected version and file.
- Smallest reproduction (command and input).
- Expected and observed.
- Severity reason, CWE.
- Suggested patch.
- A note that an AI assisted tool found it.

Keep it short. Maintainers are tired of low quality AI reports.

## Coordinated disclosure

1. Look for a channel in `SECURITY.md` or `GOVERNANCE.md`.
2. Use the GitHub private advisory when it exists.
3. Otherwise send a short introductory email and give detail on a private
   channel.
4. Follow the project timeline. Without a policy, 90 days is a common
   assumption, but check the source.
5. Wait for the patch and the maintainer before publishing.

## Fuzzing

`--fuzz` suggests a skeleton per language: libFuzzer, Atheris, Go fuzz, cargo
fuzz, Jazzer. Rule: run without network, keep the crash input, dedupe the
signature.

## Limits

- There is no full call graph. Reachability is a grep.
- Business logic and the authorization model do not fall out of static rules.
- Third party services and database behavior are not tested.
- Build dependencies can be missing in a networkless box. A sandbox failure is
  not a finding.
- Beril does not build a working exploit. A crash and a primitive are enough.

## Ethics

- Local clone and openly licensed code only.
- Touch no production system.
- Do not flood the maintainer.
- Do not send the same finding through two channels.
- Agree the publication date with the maintainer.
