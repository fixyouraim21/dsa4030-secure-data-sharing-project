"""
STEP 4: Add more columns to file_metadata so the table can track
the full secure-transfer process (hash, encryption, signing, transfer status).
"""

import sqlite3
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from logger_config import logger

conn = sqlite3.connect("db/project.db")
cursor = conn.cursor()

new_columns = [
    ("sha256_hash", "TEXT"),
    ("encrypted", "TEXT"),
    ("signed", "TEXT"),
    ("sender_org", "TEXT"),
    ("receiver_org", "TEXT"),
    ("transfer_status", "TEXT"),
    ("created_at", "TEXT"),
]

for column_name, column_type in new_columns:
    try:
        cursor.execute(f"ALTER TABLE file_metadata ADD COLUMN {column_name} {column_type}")
        print(f"Added column: {column_name}")
        logger.info(f"Added column '{column_name}' to file_metadata.")
    except sqlite3.OperationalError as e:
        print(f"Skipped '{column_name}': {e}")
        logger.info(f"Skipped column '{column_name}' (already exists).")

conn.commit()
conn.close()

print("\nTable expansion complete.")