# Mainframe lab

A static z/OS case. RACF profiles, JCL, CICS transactions, console log, DB2 grants, APF list and spool.

```bash
./tests.sh
```

| File | Question |
|---|---|
| `racf-profiles.txt` | Excessive rights and group reach |
| `jcl/backup.jcl` | Dataset access and write |
| `cics-transactions.txt` | Debug and interpreter transactions |
| `console.txt` | Operator authority |
| `db2-grants.txt` | Table rights |
| `apf.txt` | Authorized library write |
| `jes-spool.txt` | Other users' output |

## Tasks

1. Which user has SPECIAL and why does it matter?
2. Which dataset can `DEV01` alter and how did it get the right?
3. Is `PROD.APF.LOAD` writable by `DEV01`? What does a write there mean?
4. Which CICS transaction gives a command interpreter and which gives a debugger?
5. Can `DEV01` start the SVCBACK task? What does the console say?
6. Where does the JCL write and with which rights?
7. Name the three highest impact fixes.

## Constraints

Static only. No z/OS system is attached.

## Evidence

Quote the profile line and the file. A dataset name without the PERMIT line is a guess.

Answers are in `ANSWERS.md`.
