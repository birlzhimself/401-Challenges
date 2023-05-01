#!/usr/bin/python3

# Script : OpsChallenge07.py
# Purpose: Recursively encrypt a single folder and all its contents. Recursively decrypt a single folder that was encrypted by this tool
# Why    : Improves efficiency to encrypt or decrypt files/directories

from cryptography.fernet import Fernet  # Import Fernet from cryptography module to perform encryption and decryption
import os  # Import os module to interact with the file system

def encrypt_file(file_path):
    with open(file_path, 'rb') as f:  # Open the file in read-binary mode
        data = f.read()  # Read the data from the file
    key = Fernet.generate_key()  # Generate a unique key
    cipher = Fernet(key)  # Create a Fernet instance with the generated key
    encrypted_data = cipher.encrypt(data)  # Encrypt the data
    with open(file_path + '.encrypted', 'wb') as f:  # Create a new file with a .encrypted extension to write the encrypted data
        f.write(encrypted_data)  # Write the encrypted data to the file
    os.remove(file_path)  # Remove the original file
    print('File encrypted successfully!')
    
    # Write the key to a separate file
    key_path = file_path + ".key"  # Generate a key file path
    with open(key_path, "wb") as f:  # Open the key file in write-binary mode
        f.write(key)  # Write the key to the key file

def decrypt_file(file_path):
    # Read the key from the separate file
    key_path = file_path.replace(".encrypted", "") + ".key"  # Generate the key file path
    with open(key_path, "rb") as f:  # Open the key file in read-binary mode
        key = f.read()  # Read the key

    # Decrypt the file
    with open(file_path, "rb") as f:  # Open the encrypted file in read-binary mode
        encrypted_data = f.read()  # Read the encrypted data
    fernet = Fernet(key)  # Create a Fernet instance with the key
    decrypted_data = fernet.decrypt(encrypted_data)  # Decrypt the data

    # Write the decrypted data to the file
    with open(file_path.replace(".encrypted", ""), "wb") as f:  # Open the file in write-binary mode
        f.write(decrypted_data)  # Write the decrypted data to the file

    # Delete the encrypted and the key file
    os.remove(key_path)  # Remove the key file
    os.remove(file_path)  # Remove the encrypted file

    print("File decrypted successfully.")

def encrypt_message(message):
    key = Fernet.generate_key()  # Generate a unique key
    cipher = Fernet(key)  # Create a Fernet instance with the generated key
    encrypted_message = cipher.encrypt(message.encode())  # Encrypt the message
    print('Encrypted message:', encrypted_message.decode())  # Print the encrypted message
    print('Key:', key.decode())  # Print the key

def decrypt_message(message):
    key = input('Enter the key: ').encode()  # Take the key as input and encode it
    cipher = Fernet(key)  # Create a Fernet instance with the entered key
    decrypted_message = cipher.decrypt(message.encode())  # Decrypt the message
    print('Decrypted message:', decrypted_message.decode())  # Print the decrypted message

def encrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder
