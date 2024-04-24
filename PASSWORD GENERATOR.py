import string
import random

def generate_password(length):
    if length < 4:  # Ensure the password length is sufficient for complexity
        return "Password length must be at least 4 characters."

    # Define the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        print(f"Your new password is: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
