import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print(generate_password(12))