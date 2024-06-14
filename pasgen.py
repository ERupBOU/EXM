import string
import random

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special):
    try:
        characters = ""
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        if not characters:
            return None

        password = ''.join(random.choice(characters) for i in range(length))
        return password
    except ValueError:
        return None

def get_password_options():
    while True:
        try:
            length = int(input("Enter the password length: "))
            if length <= 0:
                print("[!] Password length must be a positive integer.")
                continue

            use_lowercase = input("Use lowercase letters? (yes/no) ").lower() == "yes"
            use_uppercase = input("Use uppercase letters? (yes/no) ").lower() == "yes"
            use_digits = input("Use digits? (yes/no) ").lower() == "yes"
            use_special = input("Use special characters? (yes/no) ").lower() == "yes"

            return length, use_lowercase, use_uppercase, use_digits, use_special
        except ValueError:
            print("[!] Invalid input. Please enter a positive integer for the password length.")
            continue

def run_password_generator():
    while True:
        length, use_lowercase, use_uppercase, use_digits, use_special = get_password_options()
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
        if password is None:
            print("[!] Failed to generate password. Please try again.")
        else:
            print("Generated password:", password)

        choice = input("[?] Do you want to generate another password? (y/n) ")
        if choice.lower() == "n":
            print("[*] Returning to main menu...")
            break
        elif choice.lower() == "y":
            continue
        else:
            print("[!] Invalid choice. Please try again.")