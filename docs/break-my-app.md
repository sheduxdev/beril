# Break my app

A runbook for the common request: "I have X on my machine, find the hole and report it."

The agent confirms scope, runs the read-only pass, picks one class, proves it, and writes the report. It does not spray.

## Direct phrases

If the target is in the sentence, the first tool call is a command. These mean
the same thing:

```text
selam beril, şunu kırar mısın: https://app.example
bunu bir kır
açık var mı, bak: https://app.example
break this, find a bug
```

Passive starts immediately. "Benim" or "my app" allows `--owned`. Without an
ownership signal, the agent runs passive, returns the leads and asks one
permission question before a payload. Behavior file: `agents/front-desk.md`.

## Intake

Ask four questions:

1. What is the artifact and where is it?
2. Do you own it, or is it in a bounty scope?
3. Read-only, or may I send payloads?
4. What proof do you need: note, report, PoC, or fix?

If the user says "just break it", default to read-only and one narrow active test on the same target. Stop at the first reproducible proof.

## Gate

An active test needs a record:

```bash
./beril verify --new app.example     # publish the token, then:
./beril verify --verify app.example
```

or an explicit `--owned` acknowledgement. A scope file narrows hosts and paths:

```bash
./beril scan --target https://app.example --active --scope scope.txt
```

Without a record the active scan exits before the first payload. Details:
`docs/verification.md`.

## Reader

Pick a profile before writing:

- `engineer`: the person who fixes it.
- `bugbounty`: program triage, CVSS and request pair.
- `smb`: one-page SMB report, traffic light, KVKK note.
- `maintainer`: open source disclosure.

Never mix two profiles in one report.

## Web app

```bash
./beril scan --target https://app.example
```

Read the scan. Open `references/techniques.md` and pick one class that fits the stack: auth, IDOR, injection, logic, upload, SSRF. For an execution path, use the ladder and the class shelf in `references/rce-mastery.md`.

Then:

1. Create two accounts.
2. Capture one normal request.
3. Change one field or object id.
4. Compare the response with a clean baseline.
5. Prove the impact with the smallest request pair.

Do not brute force. Do not dump a database.

## APK

```bash
./beril scan --target ./app.apk --deep
```

Then:

1. Read the manifest and list exported components.
2. Test the deep link with `adb shell am start`.
3. Check `allowBackup`, cleartext, and the JS bridge.
4. Hook one method with `scripts/frida_hook.js` on an emulator.
5. Prove data access or an action another app can trigger.

## EXE or ELF

```bash
./beril scan --target ./sample --deep
```

Then:

1. Map imports, strings, and mitigations.
2. Open the file in Ghidra or rizin.
3. Pick one input source and follow it to a sink.
4. Confirm in a debugger with a minimal input.
5. Name the primitive and the blocked mitigation.

Do not run the sample on the host unless you have a snapshot.

## Source tree

```bash
./beril scan --target ./source --tools
```

Then:

1. Triage the scanner hits by reachability.
2. Trace one source to one sink by hand.
3. Write a failing test or a request.
4. Fix the check at the right layer.
5. Add a regression test.

## Firmware

```bash
./beril scan --target ./firmware.bin --deep
```

Then:

1. Extract with unblob.
2. Map init, web root, config, and secrets.
3. Read the update path.
4. Test the management daemon from the LAN.
5. Record a recovery method before any write.

## Report

```bash
./beril report --input scans/app.json --profile engineer --out rapor.md
```

Manual block when the renderer is not used:

```markdown
## Title
<primitive> in <asset>

## Attacker position
No account / one account / LAN

## Precondition
Version, role, config

## Reproduction
1. ...
2. ...

## Result
The exact response, crash, or file

## Impact
Data, money, account, code execution

## Root cause
The missing check and the line

## Fix
The smallest correct change

## Evidence
Path to request log, screenshot, crash input

## Confidence
Confirmed / inferred
```

## Stop conditions

- The agreed proof exists.
- The next test needs a write or a restart and the user has not approved it.
- The target is shared hosting and a scan could affect neighbors.
- A finding is already a duplicate and the user only needs the note.
- The budget is spent or the WAF returns 429 twice.
- Active work lost its ownership record and the user has not renewed it.

## Quality gate

Before sending:

- Every claim has a link or a path.
- The request is minimal.
- The root cause names the missing check.
- The impact is business language, not only CVSS.
- The report says what was not tested.
