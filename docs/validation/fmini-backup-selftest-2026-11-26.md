# Backup audit execution — 2026-11-26

Source commit: `4e1b61db641422106ad07d6c702edceee385333f`.
The fetched Python source was reproduced locally and `git hash-object` matched the repository blob `206fb3dd99ed9cc964aa81e4c0d58afe33c7207c`.

```text
$ python /tmp/audit_fmini_backup.py --self-test
9 synthetic cases passed
$ python --version
Python 3.13.5
```

One valid synthetic 200-slot JSON roundtrip and eight malformed-input rejection cases passed. This verifies the auditor's current structural rules only; the synthetic two-byte records are not actual keyboard patches. SHA-256 fingerprints detect differences when compared against a trusted baseline, not semantic patch validity. No real device backup, restoration, MIDI transmission, or firmware compilation was performed. Keep original backups offline; do not publish personal patch banks by default.
