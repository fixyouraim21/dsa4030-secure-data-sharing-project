"""
STEP 4: Add more columns to file_metadata so the table can track
the full secure-transfer process (hash, encryption, signing, transfer status).
This will be filled in later by Member 2's scripts.
"""

import sqlite3

conn = sqlite3.connect("db/project.db")
cursor = conn.cursor()

# ALTER TABLE lets us add new columns to an existing table.
# We add them one at a time - SQLite requires this.
# Each new column will be empty (NULL) for existing rows until updated.

new_columns = [
    ("sha256_hash", "TEXT"),
    ("encrypted", "TEXT"),          # will store 'Yes' or 'No'
    ("signed", "TEXT"),             # will store 'Yes' or 'No'
    ("sender_org", "TEXT"),
    ("receiver_org", "TEXT"),
    ("transfer_status", "TEXT"),    # e.g. 'Pending', 'Sent', 'Verified'
    ("created_at", "TEXT"),
]

for column_name, column_type in new_columns:
    try:
        cursor.execute(f"ALTER TABLE file_metadata ADD COLUMN {column_name} {column_type}")
        print(f"Added column: {column_name}")
    except sqlite3.OperationalError as e:
        # This happens if the column already exists - safe to ignore
        print(f"Skipped '{column_name}': {e}")

conn.commit()
conn.close()

print("\nTable expansion complete.")