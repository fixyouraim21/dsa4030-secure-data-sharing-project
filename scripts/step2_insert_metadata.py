"""
STEP 2: Insert a row of real metadata about our dataset file
into the file_metadata table.
"""

import sqlite3

# Connect to the same database file we created in Step 1
conn = sqlite3.connect("db/project.db")
cursor = conn.cursor()

# The real values we just measured from the terminal
filename = "employee_dataset.csv"
record_count = 100000  # 100,001 lines minus 1 header row

# This SQL command inserts a new row into the table.
# The ? marks are placeholders - Python safely fills them in with the values below.
# (This is the correct/safe way to insert data - never paste values directly into SQL text)
cursor.execute("""
INSERT INTO file_metadata (filename, record_count)
VALUES (?, ?)
""", (filename, record_count))

# Save the change
conn.commit()
conn.close()

print(f"Inserted metadata for '{filename}' with {record_count} records.")