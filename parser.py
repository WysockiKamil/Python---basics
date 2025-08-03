def Simple_parser(text):
    elements = text.split()  # Split the text into elements
    
    if len(elements) != 3:
        raise ValueError("Wymagany format: liczba operator liczba (np. 2 + 3, 7 * 8)")
    
    num1, op, num2 = elements
    
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        raise ValueError("Liczby muszą być całkowite.")
    
    if op not in ['+', '-', '*', '/']:
        raise ValueError("Nieprawidłowy operator. Dozwolone operatory to: +, -, *, /")
    elif op == '/' and num2 == 0:
        raise ValueError("Dzielenie przez zero jest niedozwolone.")
    elif op == '*':
        return num1 * num2
    elif op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '/':
        return num1 / num2
