"""
STEP 1: Create the SQLite database and one table.
This is the simplest possible version - just to see it work.
"""

import sqlite3

# This line creates the file db/project.db if it doesn't exist yet,
# and opens a "connection" to it (like opening a door to talk to the file).
conn = sqlite3.connect("db/project.db")

# A "cursor" is what we use to actually run commands against the database.
cursor = conn.cursor()

# This SQL command creates a table called "file_metadata" with some columns.
cursor.execute("""
CREATE TABLE IF NOT EXISTS file_metadata (
    file_id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    record_count INTEGER
)
""")

# This saves (commits) the change to the file
conn.commit()

# This closes the connection, like closing the door
conn.close()

print("Database created successfully at db/project.db")
print("Table 'file_metadata' created successfully.")