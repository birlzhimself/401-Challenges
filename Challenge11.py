#!/usr/bin/python3

# Script : OpsChallenge11.py
# Purpose: Create a popup window on a Windows PC with a ransomware message
# Why    : Learn how ransomware works

import random
from scapy.all import *

def scan_port(host, port):
    src_port = random.randint(1024, 65535)  # Randomize source port
    response = sr1(IP(dst=host)/TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)
    
    if response is None:
        print(f"Port {port} is filtered (silently dropped).")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        send(IP(dst=host)/TCP(sport=src_port, dport=port, flags="R"), verbose=0)
        print(f"Port {port} is open.")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
        print(f"Port {port} is closed.")

def scan_ports(host, port_range):
    for port in port_range:
        scan_port(host, port)

# Define host IP and port range
host = "127.0.0.1"
port_range = range(1, 100)

# Scan the ports
scan_ports(host, port_range)
