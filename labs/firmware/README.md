# Firmware lab

A synthetic firmware image with a ZIP rootfs behind a header. It has a command injection, an unsigned update path, a telnet service, and a key in an env file.

```bash
python3 build_firmware.py
unblob firmware.bin -e out
./tests.sh
```

The image is not a real device. The workflow is the same: extract, mount or inspect, map services, read the update logic.

## Tasks

1. Run `file` and `strings` on `firmware.bin`. What format is inside?
2. Extract with unblob. How many chunks and formats did it report?
3. Map the rootfs: init scripts, web root, config, secrets.
4. Read `etc/update.conf`. What does `VERIFY=0` mean for an attacker?
5. Read `etc/init.d/rcS`. Which services start, and which one is plaintext?
6. Test the CGI with `QUERY_STRING='host=127.0.0.1; id'`. What is unquoted?
7. Find the key in `etc/app.env`. What is the blast radius?
8. Read `etc/shadow`. What hash format is used?
9. Write a finding for the command injection with a request and an impact.
10. Write the fix for the CGI and the update path.

## Evidence

Keep the extraction summary, the script line, and the command output. A rootfs map with paths is the deliverable.

## Stretch

- Emulate the CGI behind `busybox httpd` or a small Python server.
- Repack the rootfs and forge an update image.
- Add a second CGI with a buffer bug in C.
- Run `./beril scan --target ./rootfs --tools` and triage the hits.

Answers are in `ANSWERS.md`.
