import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''
    all_characters = lowercase + uppercase + numbers + symbols
    if not all_characters:
        raise ValueError("At least one character type must be selected.")
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator")
    length = int(input('Enter Password Length:'))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f'Generated Password: {password}')
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()