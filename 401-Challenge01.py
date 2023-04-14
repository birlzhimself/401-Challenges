#!/usr/bin/python3

#Script:   Ops Challenge: Class 02 - 401 Python Collections 
#Purpose:  Transmit a single ICMP (ping) packet to a specific IP
#Why:      Learn how to write an uptime sensor tool that checks systems are responding

import time
from pythonping import ping

destination = '8.8.8.8'  

while True:
    try:
        response = ping(destination, count=1)
        if response.success():
            status = 'Network Active'
        else:
            status = 'Network Error'
    except Exception as e:
        status = 'Network Error'
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print(f"{timestamp} {status} to {destination}")
    time.sleep(2) 
