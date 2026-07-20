# DSA4030 – Secure Data Sharing Project

## Group 12 – Secure Data Sharing

---

# Project Overview

This project demonstrates a secure data-sharing environment where two organizations exchange datasets while ensuring confidentiality, integrity, authentication, and non-repudiation.

The system uses open-source security tools including **GPG (GNU Privacy Guard)** and **SQLite** to encrypt files, digitally sign datasets, verify signatures, detect file modifications, and securely transfer encrypted files between organizations.

---

# Project Objectives

The project aims to:

- Encrypt sensitive datasets before sharing.
- Digitally sign files to verify sender authenticity.
- Verify digital signatures upon receipt.
- Detect unauthorized file modifications.
- Demonstrate secure file transfer.
- Maintain audit logs for accountability.

---

# Team Responsibilities

| Member | Responsibility |
|---------|----------------|
| Member 1 | Environment setup, dataset generation, SQLite database, logging |
| Member 2 | Encryption, digital signatures, hash generation, signature verification, secure transfer implementation |
| Member 3 | Security testing, evidence collection, documentation, final report, presentation |

---

# Project Structure

```
group12-secure-data-sharing/
│
├── data/               # Employee dataset
├── db/                 # SQLite database
├── encrypted/          # Encrypted datasets (.gpg)
├── hashes/             # SHA-256 hash files
├── keys/               # Public keys and signature files
├── logs/               # Application logs
├── received/           # Simulated receiving organization
├── screenshots/        # Evidence for security tests
├── scripts/            # Python scripts
├── signatures/         # Public key files
├── README.md
```

---

# Environment Setup

## Requirements

- Python 3.x
- Git
- GPG (GnuPG)
- SQLite
- OpenSSL

## 1.Clone Repository

```powershell
git clone https://github.com/Amy/group12-secure-data-sharing.git
cd group12-secure-data-sharing
```

## 2.Create Virtual Environment

```powershell
python -m venv venv
```

Activate:

```powershell
venv\Scripts\activate
```

## 3. Install Dependencies

```powershell
pip install pandas faker
```

---

# Dataset

**Dataset**

```
employee_dataset.csv
```

**Records**

```
100,000
```

**Format**

```
CSV
```

The dataset contains synthetic employee records generated using Python and the Faker library. No real personal information is included.

---

# Storage Platform

SQLite is used to store metadata related to the shared dataset.

Database:

```
db/project.db
```

The metadata table stores:

- File name
- Record count
- SHA-256 hash
- Encryption status
- Signature status
- Sender organization
- Receiver organization
- Transfer status
- Timestamp

---

# Security Controls Implemented

The following security controls were implemented:

- File Encryption using GPG
- Digital Signatures
- Signature Verification
- SHA-256 Integrity Verification
- Activity Logging
- Secure File Transfer Simulation

---

# Security Testing

Six security tests were successfully completed.

| Test | Description |
|------|-------------|
| Test 1 | Encryption Verification |
| Test 2 | Digital Signature Verification |
| Test 3 | Modified File Detection |
| Test 4 | SHA-256 Hash Verification |
| Test 5 | Logging Verification |
| Test 6 | Secure Transfer Verification |

Evidence for each test is available in the `screenshots/` folder and documented in the final project report.

---

# Logging

Application activities are recorded in:

```
logs/activity.log
```

The log records database operations and system events to support auditing and troubleshooting.

To view the logs:

```powershell
Get-Content logs\activity.log
```

---

# Security Tools Used

- GPG (GNU Privacy Guard)
- OpenSSL
- SQLite
- Python
- PowerShell

---

# Notes

- The dataset is entirely synthetic.
- Private GPG keys are excluded from the repository for security purposes.
- Only public keys are shared within the project repository.