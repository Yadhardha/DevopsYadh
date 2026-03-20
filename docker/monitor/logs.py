import time
import logging
from datetime import datetime
import os

# Ensure logs folder exists
log_folder = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(log_folder, exist_ok=True)

# Log file path
log_file = os.path.join(log_folder, "devops.log")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Sample log messages
for i in range(10):
    logging.info(f"Test log message{i+1}")
    print(f"Logged: Test log message{i+1}")
    time.sleep(2)
