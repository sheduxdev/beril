# Mobile lab

A static Android fixture with several common weaknesses. It does not need a full Android build to review.

```bash
./tests.sh
```

## Tasks

1. Read the manifest. List every exported component and its intent filter.
2. Why is `DebugActivity` exported, and what does it do with `dump`?
3. Follow the `beril://open?url=` deep link. What reaches `WebView.loadUrl`?
4. The WebView exposes `BerilBridge`. Which methods can a loaded page call?
5. What does `token()` return, and what is the impact if a page is attacker controlled?
6. Read the network security config. Which domain allows cleartext?
7. Find the API base URL and the embedded key in `strings.xml`.
8. What does `allowBackup="true"` expose on a non-rooted device?
9. The file provider allows `external-path` with `path="."`. What is the risk?
10. Write three findings with severity and fix.

## Evidence

Quote the manifest attribute or the Java line, give the `am start` or `adb` command, and name the impact. A component is not a bug until an attacker can reach something valuable.

## Stretch

- Build the app with Gradle and inspect the APK with `./beril scan --target app-debug.apk`.
- Use `adb shell am start -a com.beril.lab.PUSH_TOKEN --es token X` against the receiver.
- Hook `BerilBridge.token` with Frida.
- Add a custom scheme handler and test path traversal.

Answers are in `ANSWERS.md`.
