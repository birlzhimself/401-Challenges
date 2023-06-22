#!/usr/bin/python3

# Script         Ops Challenge: Event Logging Tool Part 2 of 3
# Purpose        Proceeds to ping 8.8.8.8 indefinitely while printing a timestamp and success or failure message to the console and writing it to a log file with a maximum size.
# Why            Learn how to use the logging library.

import os
import time
import logging

# Configure logging settings
logging.basicConfig(filename="ping_log.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
ip_address = "8.8.8.8"
status = ""
logging.info('Starting script... Pinging {}'.format(ip_address))
while True:
    response = os.system("ping -c 1 {}".format(ip_address))
    if response == 0:
        status = "Success"
    else:
        status = "Failure"
    logging.info('Ping status: {}'.format(status))
    print('Ping status: {}'.format(status))
    time.sleep(1)
