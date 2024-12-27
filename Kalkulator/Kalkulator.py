def add(a, b):
    """Perform addition."""
    return a + b

def subtract(a, b):
    """Perform subtraction."""
    return a - b

def multiply(a, b):
    """Perform multiplication."""
    return a * b

def divide(a, b):
    """Perform division."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def power(a, b):
    """Perform exponentiation."""
    return a ** b


def calculator():
    print("Welcome to the Function-Based Python Calculator!")
    print("Operations:")
    print("  1: Addition (+)")
    print("  2: Subtraction (-)")
    print("  3: Multiplication (*)")
    print("  4: Division (/)")
    print("  5: Power (**)")
    print("Type 'exit' to quit.")

    while True:
        operation = input("\nChoose an operation (1-5 or exit): ").strip()

        if operation.lower() == 'exit':
            print("Goodbye!")
            break

        if operation not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please select a valid operation.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == '1':
                print(f"The result is: {add(num1, num2)}")
            elif operation == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif operation == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif operation == '4':
                print(f"The result is: {divide(num1, num2)}")
            elif operation == '5':
                print(f"The result is: {power(num1, num2)}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

calculator()

