#!/usr/bin/python3

# Script : OpsChallenge11.py
# Purpose: Create a popup window on a Windows PC with a ransomware message
# Why    : Learn how ransomware works

import random
from scapy.all import *

def check_port_status(ip_address, port_number):
    """
    This function checks the status of a specified port on a given IP address.
    
    Args:
    ip_address (str): The IP address to check.
    port_number (int): The port number to check.
    
    Returns:
    None
    
    Prints:
    A message indicating whether the port is open, closed, or filtered.
    """
    # Randomize the source port
    source_port = random.randint(1024, 65535)
    
    # Send a SYN packet to the specified IP address and port number
    response = sr1(IP(dst=ip_address)/TCP(sport=source_port, dport=port_number, flags="S"), timeout=1, verbose=0)
    
    # Check the response
    if response is None:
        print(f"Port {port_number} is filtered (silently dropped).")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        # If the response has a TCP layer and the SYN-ACK flag is set, the port is open
        send(IP(dst=ip_address)/TCP(sport=source_port, dport=port_number, flags="R"), verbose=0)
        print(f"Port {port_number} is open.")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
        # If the response has a TCP layer and the RST flag is set, the port is closed
        print(f"Port {port_number} is closed.")

def check_ports(ip_address, port_range):
    """
    This function checks the status of a range of ports on a given IP address.
    
    Args:
    ip_address (str): The IP address to check.
    port_range (range): The range of port numbers to check.
    
    Returns:
    None
    
    Prints:
    A message indicating whether each port is open, closed, or filtered.
    """
    for port_number in port_range:
        check_port_status(ip_address, port_number)

# Define the IP address and port range to check
ip_address = "127.0.0.1"
port_range = range(1, 100)

# Check the ports
check_ports(ip_address, port_range)
