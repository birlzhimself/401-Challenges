#!/usr/bin/python3

# Script : OpsChallenge26.py
# Purpose: Create
# Why

import logging

def start_logging():
    # Step 1: Configure the logging settings
    logging.basicConfig(
        filename='app.log',  # Specify the log file name
        level=logging.DEBUG,  # Set the logging level to DEBUG (you can change it as needed)
        format='%(asctime)s - %(levelname)s - %(message)s'  # Specify the log message format
    )

    # Step 2: Log messages
    logging.debug('This is a debug message')
    logging.info('This is an informational message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

    # Step 3: Add error handling and induce errors
    try:
        # Code that may cause an error
        num1 = 10
        num2 = 0
        result = num1 / num2
    except Exception as e:
        logging.exception('An error occurred: %s', str(e))

if __name__ == '__main__':
    start_logging()
