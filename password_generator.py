import random
import string

def generate_password(password_length, special_characters=False, numbers=False):
    letters = string.ascii_letters  # [a-z,A-Z]
    digits = string.digits          # [0-9]
    special = string.punctuation    # contains all special characters

    allowed_characters = letters  # the characters to choose from when generating the password
    if special_characters:
        allowed_characters += special
    if numbers:
        allowed_characters += digits

    password = ''
    meets_criteria = False
    has_special = False
    has_number = False

    while len(password) < password_length or not meets_criteria:
        new_char = random.choice(allowed_characters)
        password += new_char

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password


password_length = int(input('Enter a password length: '))
special_characters = input('Do you want to include special characters (y/n)? ').lower() == 'y'
numbers = input('Do you want to include numbers (y/n)? ').lower() == 'y'

pwd = generate_password(password_length, special_characters, numbers)
print('Your generated password:', pwd)


    
