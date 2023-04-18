#!/usr/bin/python3

#Script:   Ops Challenge: Class 03 - 401 Python Collections 
#Purpose:  Ask the user for an email address and password to use for sending notifications.
#Why:      Send an email to the administrator if a host status changes 

import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# User input for email address and password
email_address = input("Example@example.com: ")
email_password = input("1234657900: ")

# Email message details
sender_email = email_address
receiver_email = "qfxhqkwdxfgbarqegb@bbitf.com"
email_subject = "Uptime status changed"

destination_ip = input("8.8.8.8")
status = ""
counter = 0

while True:
    response = os.system(f"ping -c 1 {destination_ip} > /dev/null 2>&1")
    if response == 0:
        new_status = "up"
    else:
        new_status = "down"

    if new_status != status:
        # Send email notification if status has changed
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = email_subject
        message_body = f"The status of {destination_ip} has changed from {status} to {new_status} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}"
        message.attach(MIMEText(message_body, 'plain'))

        # Add log file as attachment
        with open("ping_log.txt", "rb") as file:
            log_attachment = MIMEBase('application', 'octet-stream')
            log_attachment.set_payload(file.read())
        encoders.encode_base64(log_attachment)
        log_attachment.add_header('Content-Disposition', 'attachment', filename="ping_log.txt")
        message.attach(log_attachment)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_address, email_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    log_entry = f"{timestamp} Network {new_status} to {destination_ip}"
    print(log_entry)

    with open("ping_log.txt", "a") as file:
        file.write(log_entry + "\n")

    status = new_status
    time.sleep(2)
