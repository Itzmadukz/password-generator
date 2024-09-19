# Random Passoword Generator

## Example of how the function can be used

```python
if __name__ == "__main__":
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    # Generate and print the password
    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    print(f"Your generated password is: {password}")
```
