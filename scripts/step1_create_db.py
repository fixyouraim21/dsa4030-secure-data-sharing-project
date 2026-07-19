"""
STEP 1: Create the SQLite database and one table.
"""

import sqlite3
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from logger_config import logger

conn = sqlite3.connect("db/project.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS file_metadata (
    file_id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    record_count INTEGER
)
""")

conn.commit()
conn.close()

print("Database created successfully at db/project.db")
print("Table 'file_metadata' created successfully.")
logger.info("Database and file_metadata table created (or already existed).")