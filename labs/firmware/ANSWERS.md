# Firmware lab answers

## 1. Format

A ZIP central directory sits behind a fake `BERILFW1` header and padding. `file` may say data; `strings` shows the ZIP names.

## 2. Extraction

`unblob` reports a ZIP chunk, unknown header bytes, and trailing padding. The ZIP is extracted under `out/*_extract/`.

## 3. Rootfs map

- `/etc/init.d/rcS`: network, httpd, telnetd
- `/www/cgi-bin/diagnostic.cgi`: ping CGI
- `/etc/update.conf`: unsigned update config
- `/etc/app.env`: cloud key and telemetry token
- `/etc/shadow`: MD5-crypt hashes

## 4. `VERIFY=0`

The updater does not verify the image signature. Anyone who can reach the update URL or the upload form can push a modified rootfs.

## 5. Services

`httpd` on port 80 and `telnetd` with `/bin/sh`. Telnet is plaintext on the LAN. The CGI runs as the web user, often root on embedded systems.

## 6. Command injection

`/bin/ping -c 1 $HOST` is unquoted. `host=127.0.0.1; id` runs `id`.

```text
Content-Type: text/plain

probing 127.0.0.1; id
PING 127.0.0.1 ...
uid=0(root) gid=0(root)
```

## 7. Key

`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` are in a world-readable env file. The blast radius depends on the IAM policy. A read-only key is still a data breach. Rotate it and move it to a protected store.

## 8. Shadow

`$1$` is MD5-crypt. It is fast to crack. A unique root password and a stronger scheme (`$6$` or yescrypt) are the fix.

## 9. Report shape

```markdown
### Unauthenticated command injection in diagnostic CGI

- Request: GET /cgi-bin/diagnostic.cgi?host=127.0.0.1;id
- Response: uid=0(root)
- Impact: command execution as the web user, often root on the device
- Cause: unquoted $HOST in /bin/ping
- Fix: quote the value, validate with an allowlist, drop privileges
```

## 10. Fixes

CGI: `HOST=$(printf '%s' "$HOST" | tr -d ';&|')` or quote and use `--`. Validate a hostname or IP with a strict regex. Run the CGI as a non-root user.

Update: sign the image, verify before extraction, pin the key in read-only storage, enforce a version floor, and extract with a non-root user.

## Stretch notes

- A Python wrapper can set `QUERY_STRING` and run the CGI. A real device needs `busybox httpd`.
- Repacking: extract, modify, zip, prepend the header, and write to the update path.
- A C CGI with `strcpy` from `QUERY_STRING` gives a stack bug to combine with the RE lab.
