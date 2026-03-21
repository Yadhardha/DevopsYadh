import logging
from logging.handlers import RotatingFileHandler
import os
import time
import random
import subprocess
import requests

# -----------------------------
# Setup log file
# -----------------------------
log_folder = "/home/yadhardha45/DevopsYadh/docker/monitor/logs"
os.makedirs(log_folder, exist_ok=True)
log_file = os.path.join(log_folder, "devops.log")

# -----------------------------
# Logger setup
# -----------------------------
logger = logging.getLogger("DevOpsDemoLogger")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# -----------------------------
# Helper functions
# -----------------------------
def log_low(msg): logger.info(f"LOW: {msg}")
def log_high(msg): logger.error(f"HIGH: {msg}")
def log_critical(msg): logger.critical(f"CRITICAL: {msg}")

# -----------------------------
# Fake alert messages
# -----------------------------
fake_alerts = [
    ("Disk usage is high: 65%", "HIGH"),
    ("No Docker containers running!", "CRITICAL"),
    ("Web page not responding at http://localhost:5000", "LOW"),
    ("Service restart required for demo container", "CRITICAL"),
    ("Memory usage is high: 75%", "HIGH")
]

# -----------------------------
# Function to simulate real + fake alerts
# -----------------------------
def generate_logs():
    # 50% chance for a fake alert each iteration
    for i in range(random.randint(1,2)):
        msg, level = random.choice(fake_alerts)
        if level == "LOW": log_low(msg)
        elif level == "HIGH": log_high(msg)
        elif level == "CRITICAL": log_critical(msg)

    # Optional: add some simulated real checks for disk / docker / web
    # Disk usage simulation
    simulated_disk = random.randint(40, 90)
    if simulated_disk > 50:
        log_high(f"Disk usage is high: {simulated_disk}%")
    else:
        log_low(f"Disk usage normal: {simulated_disk}%")

    # Docker containers simulation
    docker_running = random.choice([True, False])
    if not docker_running:
        log_critical("Docker container not running" )
    # Web service simulation
    web_up = random.choice([True, False])
    if not web_up:
        log_low("Web service not responding")

while True:
    generate_logs()
    time.sleep(10)  