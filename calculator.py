

# This program is a basic calculator

# Ask the user for the first number
num1 = float(input("Enter the first number: "))

# Ask the user for the second number
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
op = input("Choose an operation (+, -, *, /): ")

if op == "+":  # Addition
    result = num1 + num2
elif op == "-":  # Subtraction
    result = num1 - num2
elif op == "*":  # Multiplication
    result = num1 * num2
elif op == "/":  # Division
    result = num1 / num2

    # Print out the result of the calculation
print(f"The result is {result}")
