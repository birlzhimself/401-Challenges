#!/usr/bin/python3

# Script         Ops Challenge: Signature-based Malware Detection Part 1 of 3
# Purpose        Detection and remediation of malware is the core function
# Why            Learn how to use the import sys

import sys
# Get the file name to search for.
filename = input("Enter the file name to search for: ")
# Get the directory to search in.
directory = input("Enter the directory to search in: ")
# Check if the directory exists.
if not os.path.exists(directory):
    print("The directory does not exist.")
    sys.exit(1)
# Get a list of all the files in the directory.
files = os.listdir(directory)
# Search each file in the directory by name.
for file in files:
    # Check if the file name matches the file name to search for.
    if file == filename:
        # Print the file name and location.
        print(os.path.join(directory, file))
# Print how many files were searched and how many hits were found.
print("Number of files searched:", len(files))
print("Number of hits found:", len([file for file in files if file == filename]))
