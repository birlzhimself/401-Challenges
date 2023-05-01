1
#!/usr/bin/python3

#Script:   Ops Challenge: Class 06 - 401 Python Collections 
#Purpose:  Encrypt and Decrypt Files
#Why:      Learn how to run a basic script to Encrypt and Decrypt file or files or whole directories

from cryptography.fernet import Fernet
import os

def encrypt_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)
    with open(file_path + '.encrypted', 'wb') as f:
        f.write(encrypted_data)
    os.remove(file_path)
    print('File encrypted successfully!')

    # Write the key to a separate file
    key_path = file_path + ".key"
    with open(key_path, "wb") as f:
        f.write(key)

def decrypt_file(file_path):
    # Read the key from the separate file
    key_path = file_path.replace(".encrypted", "") + ".key"
    with open(key_path.replace(".encrypted", ""), "rb") as f:
        key = f.read()

    # Decrypt the file
    with open(file_path, "rb") as f:
        encrypted_data = f.read()
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    # Write the decrypted data to the file
    with open(file_path.replace(".encrypted", ""), "wb") as f:
        f.write(decrypted_data)

    # Delete the encrypted and the key file
    os.remove(key_path)
    os.remove(file_path)

    print("File decrypted successfully.")

def encrypt_message(message):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    print('Encrypted message:', encrypted_message.decode())
    print('Key:', key.decode())

def decrypt_message(message):
    key = input('Enter the key: ').encode()
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(message.encode())
    print('Decrypted message:', decrypted_message.decode())

def main():
    mode = input('Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n')
    if mode == '1':
        file_path = input('Enter file path: ')
        encrypt_file(file_path)
    elif mode == '2':
        file_path = input('Enter file path: ')
        decrypt_file(file_path)
    elif mode == '3':
        message = input('Enter message: ')
        encrypt_message(message)
    elif mode == '4':
        message = input('Enter message: ')
        decrypt_message(message)
    else:
        print('Invalid mode selected.')

if __name__ == '__main__':
    main()
