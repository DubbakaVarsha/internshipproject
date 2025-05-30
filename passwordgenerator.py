import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    character_set = lowercase
    if use_uppercase:
        character_set += uppercase
    if use_numbers:
        character_set += digits
    if use_special:
        character_set += special_chars

    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special_chars))

    password += random.choices(character_set, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Password Generator")

    while True:
        length = int(input("Enter password length: "))
        if length > 6:
            break
        print("Password length must be greater than 6. Please try again.")

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_numbers, use_special)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
