# Testing Artifacts

This folder contains files created during security testing.

## employee_dataset_tampered.csv

This file was intentionally modified to demonstrate **Security Test 3 – Detection of Modified Files**.

### Purpose

The dataset was altered after it had been digitally signed to verify that GPG detects unauthorized modifications.

### Modification Performed

The employee surname:

```
Johnson
```

was changed to:

```
Johnsn
```

### Expected Result

Running:

```powershell
gpg --verify keys/employee_dataset.csv.asc testing/employee_dataset_tampered.csv
```

produces:

```
gpg: BAD signature from "Organization A <...>"
```

confirming that the file integrity has been compromised.

> **Note:** This file is for testing and demonstration purposes only. It should not be used as the official dataset.