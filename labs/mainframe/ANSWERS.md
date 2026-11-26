# Mainframe lab answers

## 1. SPECIAL

`SVCBACK` has SPECIAL, which bypasses most RACF checks and can change profiles. Any compromise of that service account is close to full control of the lab partition.

## 2. Dataset rights

`DEV01` can UPDATE `PROD.**` because of the `PERMIT PROD.**` line through the group. It can ALTER `PROD.BACKUP.**` through `PRODGRP`. The second right is wider than the job needs.

## 3. APF library

`PROD.APF.LOAD` is `WRITE=YES`. A module placed there runs with APF authority, so a write is a path to system code. `DEV01` also has UPDATE on `SYS1.APF.**`.

## 4. CICS

`CECI` is the command interpreter. `CEDF` is the debugger. Both are enabled for the lab user. `CECI` can issue CICS commands, and `CEDF` steps a transaction.

## 5. Console

The log shows `IEE122I START COMMAND DEV01 NOT AUTHORIZED FOR SVCBACK`. So `DEV01` can display but cannot start the service task.

## 6. JCL

The job reads `PROD.BACKUP.PARMLIB` with `DISP=SHR` and writes `PROD.BACKUP.NEW` with `CATLG`. The rights come from the `PROD.BACKUP.**` ALTER permit. The job can overwrite the backup member set.

## 7. Fixes

1. Remove SPECIAL from `SVCBACK` or split the duties.
2. Narrow `PROD.BACKUP.**` from ALTER to UPDATE.
3. Restrict the APF library write and review every member.

## Chain

`DEV01` has UPDATE on `PROD.**` and ALTER on the backup set. It edits a backup parameter member and waits for the SVCBACK job to read it. The service account runs with SPECIAL, so the edited member reaches a privileged path.

## Note

A mainframe lab is mostly a rights graph. The static case teaches the graph before a live system.
