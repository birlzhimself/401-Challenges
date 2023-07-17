#!/usr/bin/python3

# Script : OpsChallenge36.py
# Purpose: Gather intelligence on a target such as a web server.
# Why    : Do reconnaissance for next steps of attack.

import os

# Prompt the user for a URL/IP address and port
target = input("Enter the target URL or IP address: ")
port = input("Enter the target port: ")

# Perform a banner grab with netcat 
print("\nPerforming banner grab with netcat...")
os.system(f"echo -en \"GET / HTTP/1.0\n\n\n\"|nc -v -n {target} {port}|grep Server")

# Perform a banner grab with telnet
print("\nPerforming banner grab with telnet...")  
os.system(f"echo | echo GET / HTTP/1.1 | telnet {target} {port}") 

# Perform a banner grab with whatweb 
print("\nPerforming banner grab with whatweb...")
os.system(f"whatweb {target}")

# Perform a banner grab with curl
print("\nPerforming banner grab with curl...")
os.system(f"curl -s --dump-header - {target} | grep Server")

# Perform a nmap scan only on the specified port  
print(f"\nPerforming nmap scan on port {port}...")
os.system(f"nmap -p{port} --version-intensity 5 -sV {target}")
