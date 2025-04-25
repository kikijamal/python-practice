# ass1.py
# random password generator program

import random
import string


def generate_password(length):
    # Define the characters to choose from
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


# Input: Password length from the user
length = int(input("Enter the desired password length: "))

# Generate and display the password
password = generate_password(length)
print(f"Your random password is: {password}")
