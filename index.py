import random

def generate_password(nr_letters, nr_symbols, nr_numbers):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    # Generate random characters for each category
    password = [
        random.choice(letters) for _ in range(nr_letters)
    ] + [
        random.choice(symbols) for _ in range(nr_symbols)
    ] + [
        random.choice(numbers) for _ in range(nr_numbers)
    ]

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string
    password_random = ''.join(password)

    return password_random

