import random

def generate_random_password(length=8):
    """Generates a random password of specified length."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 10
    random_password = generate_random_password(password_length)
    print("Randomly generated password:", random_password)
111
