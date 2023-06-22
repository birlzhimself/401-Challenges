#!/usr/bin/python3

# Script         Ops Challenge: Event Logging Tool Part 1 of 3
# Purpose        Proceeds to ping 8.8.8.8 indefinitely while printing a timestamp and success or failure message to the console and writing it to a log file with a maximum size.
# Why            Learn how to use the logging library.

import subprocess
import time
import logging

# Configure logging settings
logging.basicConfig(filename="ping_log.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

ip_address = "8.8.8.8"

logging.info('Starting script... Pinging 8.8.8.8\n')

def ping(ip_address):
    try:
        result = subprocess.run(["ping", "-c", "1", ip_address], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            status = "success"
        else:
            status = "failure"

        log_entry = f"Network {status} to {ip_address}"
        logging.info(log_entry)

    except subprocess.TimeoutExpired:
        logging.error(f"Timeout error occurred while pinging {ip_address}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Main loop
while True:
    ping(ip_address)
    time.sleep(2)
