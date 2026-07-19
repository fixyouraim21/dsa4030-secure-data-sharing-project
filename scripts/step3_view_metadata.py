"""
STEP 3: Read and display everything currently in the file_metadata table.
This is just for checking/verifying - doesn't change any data.
"""

import sqlite3

conn = sqlite3.connect("db/project.db")
cursor = conn.cursor()

# SELECT * means "give me all columns"
# FROM file_metadata means "from this table"
cursor.execute("SELECT * FROM file_metadata")

rows = cursor.fetchall()

print("Current contents of file_metadata table:")
print("-" * 50)
for row in rows:
    print(row)

conn.close()