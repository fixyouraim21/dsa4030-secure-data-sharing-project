"""
Shared logging configuration.
Every script in this project (yours, Member 2's, Member 3's) can import
this to write timestamped log entries to the same file: logs/activity.log
"""

import logging
import os

# Make sure the logs folder exists
os.makedirs("logs", exist_ok=True)

# Configure logging: write to file, include timestamp, level, and message
logging.basicConfig(
    filename="logs/activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("group12")