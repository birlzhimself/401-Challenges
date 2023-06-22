#!/bin/python

# Script         Ops Challenge: Event Logging Tool Part 2 of 3
# Purpose        Proceeds to ping 8.8.8.8 indefinitely while printing a timestamp and success or failure message to the console and writing it to a log file with a maximum size.
# Why            Learn how to use the logging library.

import os
import time
import logging
from logging.handlers import RotatingFileHandler

# Configure logging settings
log_file_name = "ping_log.log"
log_handler = RotatingFileHandler(filename=log_file_name, maxBytes=1024*1024, backupCount=5)
log_handler.setLevel(logging.INFO)
log_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logging.getLogger().addHandler(log_handler)

destination_ip = "8.8.8.8"
status = ""

logging.info('Starting script... Pinging 8.8.8.8\n')

def ping_ip(destination_ip):
    response = os.system(f"ping -c 1 {destination_ip} > ping_log.txt 2>&1")
    if response == 0:
        status = "success"
    else:
        status = "failure"

    log_entry = f"Network {status} to {destination_ip}"
    logging.info(log_entry)

# Main loop
while True:
    try:
        ping_ip(destination_ip)
    except Exception as error:
        logging.error(f"An error occurred: {error}")

    time.sleep(2)
