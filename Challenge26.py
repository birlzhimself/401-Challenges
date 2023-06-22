#!/usr/bin/python3

# Script : OpsChallenge26.py
# Purpose: Create
# Why

import os
import time
import logging

# Configure logging settings
logging.basicConfig(filename="ping_log.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

ip_address = "8.8.8.8"
status = ""

logging.info('Starting script... Pinging 8.8.8.8\n')

def ping(ip_address):
    response = os.system(f"ping -c 1 {ip_address} > ping_log.txt 2>&1")
    if response == 0:
        status = "success"
    else:
        status = "failure"

    log_entry = f"Network {status} to {ip_address}"
    logging.info(log_entry)

# Main loop
while True:
    try:
        ping(ip_address)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    time.sleep(2)
