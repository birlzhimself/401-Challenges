import smtplib

#Ask the user for an email address and password:

graphql
Copy code
email = input("Enter your email address: ")
password = input("Enter your email password: ")

#Create a function that sends an email with the necessary information when a host status changes. This function should take the previous status, current status, and host name as arguments:

python
Copy code
def send_email(previous_status, current_status, host_name):
    subject = f"Host status changed: {host_name}"
    body = f"The status of {host_name} changed from {previous_status} to {current_status} at {datetime.datetime.now()}"
    message = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email, password)
        server.sendmail(email, email, message)
        
#Modify the check_host function to call the send_email function if the status has changed:

lua
Copy code
def check_host(host):
    previous_status = host.status
    response = os.system("ping -c 1 " + host.address)
    if response == 0:
        host.status = "up"
    else:
        host.status = "down"
    if host.status != previous_status:
        send_email(previous_status, host.status, host.name)
