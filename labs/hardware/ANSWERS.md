# Hardware lab answers

## 1. UART

The log says 115200 and 3.3V is on TP2. TX is TP3 and RX is TP4. Connect the adapter RX to TP3 and the adapter TX to TP4, with a common ground on TP1.

## 2. Console

The log reaches `sample shell#` and runs `cat`, so it is an interactive root shell. The `login: root` line and the command output prove it. It is not read only.

## 3. Flash strings

`API_KEY=hw-flash-9a7c` and `UPDATE_URL=http://updates.legacy.example/feed`. The update URL is clear text, so an active attacker can serve a feed or read the request. The key is a static shared secret.

## 4. Fuses

Secure boot is blown, so the ROM checks a signed image. JTAG is open, so the debug port still halts the core and reads memory. Secure boot alone does not close the debug path.

## 5. Rollback

Counter 7 is current. A signed 1.1 image with counter 5 is refused unless the bootloader accepts a lower counter. A signed image with a counter above 7 is the only forward path.

## 6. Fixes

1. Close JTAG or fuse the debug lock in production.
2. Move the update feed to HTTPS and pin the CA.
3. Move the API key out of the flash string or rotate it per device.

## 7. Chain

TP3 and TP4 give the console. The console gives root and `/etc/device.key`. The flash dump gives the API key and the update URL without a shell. The open JTAG is a second path if the console is locked.

## Note

The two keys differ on purpose. A lab that repeats one key hides the difference between the runtime secret and the flash secret.
