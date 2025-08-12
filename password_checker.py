import re
def password_strenght_checker(password):
    if not password:
        return "Password cannot be empty"
    
    score = 0

    if len(password) > 8:
        score += 1

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1

    if re.search(r'\d', password): 
        score += 1

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    
    if score <= 2:
        return "Słabe hasło"
    elif score == 3:
        return "Średnie hasło"
    else:
        return "Silne hasło"
    
def main():
    password = input("Wprowadź hasło: ")
    result = password_strenght_checker(password)
    print(f'Wynik sprawdzania hasła: {result}')

if __name__ == "__main__":
    main()