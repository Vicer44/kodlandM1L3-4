import random

def gen_pass(pass_length):
    # Znaki, z których będzie składać się hasło
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    # Zmienna do przechowywania wygenerowanego hasła
    password = ""

    # Losowanie znaków o podanej długości
    for i in range(pass_length):
        password += random.choice(elements)

    # Zwrócenie wygenerowanego hasła
    return password
