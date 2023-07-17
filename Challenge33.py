#!/usr/bin/python3

# Script : OpsChallenge33.py - Signature-based Malware Detection Part 3 of 3
# Purpose: Perform signature-based malware detection by calculating the MD5 hash of all files in a specified directory and then run them against virustotal api.
# Why    : Signature-based malware detection is a commonly used technique to identify known malware based on their hash values.

import os
import hashlib
import glob
from datetime import datetime, timedelta
import time
import virustotal as vt
from dotenv import load_dotenv

load_dotenv()

def md5_hash(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Prompt the user for the directory to search
search_dir = input("Enter the directory to search in: ")

# Normalize the directory path by resolving relative path, removing '.' and '..'
search_dir = os.path.normpath(search_dir)

# Build the search pattern by joining the directory path, '**', and '*' to match any file recursively
search_pattern = os.path.join(search_dir, "**", "*")

# Perform the recursive glob search and save the matches
matches = glob.glob(search_pattern, recursive=True)

files_count = 0
process_time=datetime.now()
positive_count=0
total_files_scanned = 0

# Print the results
print("\nResults:\n")
for match in matches:
    if os.path.isfile(match):
        try:
            file_hash = md5_hash(match)
            file_size = os.path.getsize(match)
            abs_path = os.path.abspath(match)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            files_count+=1
            output= f"test-{process_time}.txt"
            positive=""

            if files_count < 4 and datetime.now() < datetime.now()+timedelta(minutes=4):
                print(f"Checking {abs_path} for virus")
                vt.VT_Request({os.getenv("VIRUSTOTAL_API_KEY")}, file_hash, output)
                total_files_scanned+=1
            else:
                print(f"Request rate exceeded - 4 requests / min... Going to sleep...")
                time.sleep(240)
                print(f"Resuming...")
                files_count=0
            
            file = open(output, "r")
            lines = file.readlines()
            positive = lines[positive_count][32:].strip()
            positive_count+=1

            print(f"Timestamp: {timestamp}\nFile Name: {os.path.basename(match)}\nFile Size: {file_size} bytes\nFile Path: {abs_path}\nMD5 Hash: {file_hash}\nPositives: {positive}\n")
            

        except Exception as e:
            print(f"Error processing {match}: {e}")

print(f"Total Files Scanned: {total_files_scanned}\n")
