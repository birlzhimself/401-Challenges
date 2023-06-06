#!/usr/bin/python3

# Script : OpsChallenge16.py
# Purpose: Create a Brute Foce attack tool Part1

import time

def iterate_word_list():
    path_to_word_list = input("Enter the path to the word list file: ")
    delay_between_words = float(input("Enter the delay between words (in seconds): "))
    
    with open(path_to_word_list, 'r') as file:
        for word in file:
            word = word.strip()
            print(word)
            time.sleep(delay_between_words)

def recognize_password():
    user_string = input("Enter a string to search in the word list: ")
    path_to_word_list = input("Enter the path to the word list file: ")
    
    with open(path_to_word_list, 'r') as file:
        word_list = [line.strip() for line in file]
    
    if user_string in word_list:
        print("String found in the word list.")
    else:
        print("String not found in the word list.")

def evaluate_password_complexity():
    user_password = input("Enter a password to evaluate its complexity: ")
    length_requirement = int(input("Minimum password length: "))
    capital_letter_requirement = int(input("Minimum number of capital letters: "))
    number_requirement = int(input("Minimum number of digits: "))
    symbol_requirement = int(input("Minimum number of symbols: "))
    
    complexity = 0
    
    if len(user_password) >= length_requirement:
        complexity += 1
    
    capital_letters = sum(1 for char in user_password if char.isupper())
    if capital_letters >= capital_letter_requirement:
        complexity += 1
    
    numbers = sum(1 for char in user_password if char.isdigit())
    if numbers >= number_requirement:
        complexity += 1
    
    symbols = sum(1 for char in user_password if not char.isalnum())
    if symbols >= symbol_requirement:
        complexity += 1
    
    print("Password Complexity:")
    print(f"Length: {'✓' if len(user_password) >= length_requirement else '✗'}")
    print(f"Capital Letters: {'✓' if capital_letters >= capital_letter_requirement else '✗'}")
    print(f"Numbers: {'✓' if numbers >= number_requirement else '✗'}")
    print(f"Symbols: {'✓' if symbols >= symbol_requirement else '✗'}")
    
    if complexity == 4:
        print("SUCCESS: Password meets all complexity requirements!")

def main():
    print("Select a mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    print("3. Defensive; Password Complexity")
    
    mode = int(input("Enter the mode number: "))
    
    if mode == 1:
        iterate_word_list()
    elif mode == 2:
        recognize_password()
    elif mode == 3:
        evaluate_password_complexity()
    else:
        print("Invalid mode number.")
        return

if __name__ == '__main__':
    main()
