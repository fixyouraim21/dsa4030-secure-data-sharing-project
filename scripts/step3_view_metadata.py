"""
STEP 3: Read and display everything currently in the file_metadata table.
Now also logs this action using our shared logger.
"""

import sqlite3
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from logger_config import logger

conn = sqlite3.connect("db/project.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM file_metadata")
rows = cursor.fetchall()

print("Current contents of file_metadata table:")
print("-" * 50)
for row in rows:
    print(row)

logger.info(f"Viewed file_metadata table - {len(rows)} row(s) found.")

conn.close()