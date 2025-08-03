import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_"
    password = ""
    if length % 3 == 0:
        part_length = length // 3
        password1 = ''.join(random.choice(characters) for _ in range(part_length))
        password2 = ''.join(random.choice(characters) for _ in range(part_length))
        password3 = ''.join(random.choice(characters) for _ in range(part_length))

        password = f"{password1}+{password2}+{password3}"
        return password
    else:
        part_length = length // 3
        password1 = ''.join(random.choice(characters) for _ in range(round(part_length)))
        password2 = ''.join(random.choice(characters) for _ in range(round(part_length)))
        password3 = ''.join(random.choice(characters) for _ in range(round(part_length) + 1))

        password = f"{password1}+{password2}+{password3}"
        return password
        


print(generate_password(22))