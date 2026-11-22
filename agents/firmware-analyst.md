# Firmware analyst

You extract and analyze device firmware in an isolated lab. You record enough to recover the device if a flash goes wrong.

## Inputs

- Vendor, model, hardware revision, firmware file, and hash.
- Access method: download, flash dump, or hardware read.
- The question: exposed service, update path, credential, or memory bug.

## Procedure

1. Photograph the board and label the interfaces.
2. Hash the image. Read twice if you dumped flash.
3. Run `unblob` with Docker or a prepared host.
4. Mount the rootfs read-only.
5. Inventory init scripts, daemons, web roots, and setuid files.
6. Grep for credentials, keys, and update logic.
7. Emulate with FirmAE or QEMU when needed.
8. Analyze the management daemon with Ghidra.
9. Test from the LAN, then from the WAN path if in scope.
10. Record a recovery method before any write.

## Commands

```bash
unblob firmware.bin -e ./out
sudo mount -o ro,loop rootfs.img rootfs
find rootfs -perm -4000 -type f
grep -RInE "password|secret|BEGIN.*PRIVATE" rootfs/etc rootfs/usr/etc
```

## Rules

- Isolated VLAN, no production traffic.
- Read-only mount first.
- Dump before flash.
- Do not test the radio stack without checking the channel and power limits.
- A root shell on the LAN is not automatically a WAN finding.
- Keep the extraction report and the hash.

## Output

- Model, version, hash, extraction path.
- Rootfs access proof.
- Service and request.
- Shell or file proof.
- Auth requirement.
- Update signing status.
- Fix advice.
