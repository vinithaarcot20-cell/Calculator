# Python Calculator
# Supports basic and advanced arithmetic operations

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a divided by b."""
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed.")
    return a / b

def modulus(a, b):
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed.")
    return a % b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def square_root(a):
    """Return the square root of a."""
    if a < 0:
        raise ValueError("Error: Cannot compute square root of a negative number.")
    return a ** 0.5

def display_menu():
    print("\n===== Python Calculator =====")
    print("1. Addition       (+)")
    print("2. Subtraction    (-)")
    print("3. Multiplication (*)")
    print("4. Division       (/)")
    print("5. Modulus        (%)")
    print("6. Power          (**)")
    print("7. Square Root    (sqrt)")
    print("8. Exit")
    print("=============================")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Python Calculator!")
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == '8':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice == '7':
            a = get_number("Enter a number: ")
            try:
                result = square_root(a)
                print(f"\nSquare Root of {a} = {result}")
            except ValueError as e:
                print(e)
            continue

        if choice in ('1', '2', '3', '4', '5', '6'):
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")

            try:
                if choice == '1':
                    result = add(a, b)
                    op = '+'
                elif choice == '2':
                    result = subtract(a, b)
                    op = '-'
                elif choice == '3':
                    result = multiply(a, b)
                    op = '*'
                elif choice == '4':
                    result = divide(a, b)
                    op = '/'
                elif choice == '5':
                    result = modulus(a, b)
                    op = '%'
                elif choice == '6':
                    result = power(a, b)
                    op = '**'

                print(f"\nResult: {a} {op} {b} = {result}")
            except ValueError as e:
                print(e)
        else:
            print("Invalid choice. Please select a number between 1 and 8.")

if __name__ == "__main__":
    main()
