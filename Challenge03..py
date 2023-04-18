#!/usr/bin/python3

#Script:   Ops Challenge: Class 03 - 401 Python Collections 
#Purpose:  Ask the user for an email address and password to use for sending notifications.
#Why:      Send an email to the administrator if a host status changes 

import os
import time
import smtplib
from email.message import EmailMessage


# Define the email sender and recipient addresses
sender_email = input("example@example.com")
sender_password = input("1234567890")
recipient_email = input("example2@example")

# Define the hosts to monitor
hosts = ["8.8.8.8"]

# Define the initial status of the hosts
status = {host: None for host in hosts}

def send_email(host, status_before, status_after, timestamp):
    # Define the email subject and message
    subject = f"Uptime sensor alert: {host} status changed"
    message = f"Host {host} status changed from {status_before} to {status_after} at {timestamp}"

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, f"Subject: {subject}\n\n{message}")

while True:
    # Check the status of each host
    for host in hosts:
        try:
            # Ping the host to check its status
            response = socket.create_connection((host, 80), timeout=1)
            response.close()
            new_status = "up"
        except OSError:
            new_status = "down"

        # If the status has changed, send an email notification
        if new_status != status[host] and status[host] is not None:
            send_email(host, status[host], new_status, datetime.datetime.now())

        # Update the status of the host
        status[host] = new_status

    # Wait for 5 minutes before checking the status again
    time.sleep(300)
