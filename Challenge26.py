#!/usr/bin/python3

# Script         Ops Challenge: Event Logging Tool Part 1 of 3
# Purpose        Proceeds to ping 8.8.8.8 indefinitely while printing a timestamp and success or failure message to the console and writing it to a log file with a maximum size.
# Why            Learn how to use the logging library.

import os
import time
import logging

# Configure logging settings
logging.basicConfig(filename="ping_log.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define the IP address to ping
ip_address = "8.8.8.8"

# Start the ping loop
while True:
    # Send a ping to the IP address
    response = os.system("ping -c 1 " + ip_address)
    # Check the response code
    if response == 0:
        status = "Success"
    else:
        status = "Failure"
    # Print the timestamp and status message to the console
    print(time.strftime("%Y-%m-%d %H:%M:%S"), status)
    # Write the timestamp and status message to the log file
    logging.info(time.strftime("%Y-%m-%d %H:%M:%S"), status)
    # Sleep for 1 second
    time.sleep(1)
