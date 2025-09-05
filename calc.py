"""
Calculator Project-1
-----------------------
Author : Zaber Bhuiyan Tawhid
GitHub : https://github.com/z4t-neverdie
Description:
    A simple calculator for
    addition, subtraction, multiplication, and division.
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers, handles zero division."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def calculator():
    """Main function to run the calculator."""
    print("\n=== Welcome to ZBT Calculator ===")
    print("Available operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation. Please choose +, -, *, /")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Error: Please enter valid numbers.")

        choice = input("Do you want to calculate again? (y/n): ").lower()
        if choice != 'y':
            print("Thank you for using ZBT Calculator. Ba-bye!")
            break

if __name__ == "__main__":
    calculator()
