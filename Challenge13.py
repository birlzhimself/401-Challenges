#!/usr/bin/python3

# Script : OpsChallenge13.py
# Purpose: Create custom network tools

from scapy.all import *

def perform_ping_sweep(target_ip_address):
    # Sends an ICMP echo request (ping) to the target IP address
    response = sr1(IP(dst=target_ip_address)/ICMP(), timeout=1, verbose=0)
    
    if response is None:
        print(f"{target_ip_address} is down or unresponsive.")
        return False
    else:
        print(f"{target_ip_address} is online.")
        return True

def perform_port_scan(target_ip_address):
    open_ports = []
    
    for port in range(1, 1001):  # Scan ports 1 to 1000 (adjust as needed)
        packet = IP(dst=target_ip_address)/TCP(sport=RandShort(), dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)
        
        if response is not None:
            if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                open_ports.append(port)
    
    if open_ports:
        print(f"Open ports on {target_ip_address}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {target_ip_address}")

# Prompt the user for an IP address or range
ip_range = input("Enter the target IP address or range: ")

# Split the input into individual IP addresses
ip_addresses = ip_range.split(",")

# Iterate over each IP address and perform scanning
for ip_address in ip_addresses:
    if perform_ping_sweep(ip_address.strip()):
        perform_port_scan(ip_address.strip())
    print("-" * 50)
