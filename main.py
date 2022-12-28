import random

def password_create():
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "@#%$^"
    pass_lenght = 8

    use_for = lower_letters + upper_letters + numbers + symbols

    password = "".join(random.sample(use_for, pass_lenght))

    print(password)


password_create()