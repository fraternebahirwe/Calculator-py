import sys

def add_numbers(num1, num2):
    """
    Add two numbers.

    Parameters:
    num1 (float): The first number to be added.
    num2 (float): The second number to be added.

    Returns:
    float: The sum of num1 and num2.
    """
    result = num1 + num2
    return result

def subtract_numbers(num1, num2):
    """
    Subtract two numbers.

    Parameters:
    num1 (float): The number from which to subtract.
    num2 (float): The number to subtract.

    Returns:
    float: The difference between num1 and num2.
    """
    result = num1 - num2
    return result

def multiply(numbers):
    """Return the product of the numbers."""
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    """Return the result of dividing the first number by the rest."""
    if 0 in numbers[1:]:
        return "Error: Division by zero is not allowed."
    
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result

def parse_numbers(args):
    """Convert command line arguments to a list of numbers."""
    try:
        return [float(arg) for arg in args]
    except ValueError:
        print("Error: All inputs must be valid numbers.")
        sys.exit(1)

def main():
    """Main function to run the calculator."""
    if len(sys.argv) < 3:
        print("Usage: calc <operation> <number1> <number2> [...]")
        print("Supported operations: add, subtract, multiply, divide")
        sys.exit(1)

    operation = sys.argv[1].lower()
    numbers = parse_numbers(sys.argv[2:])

    if operation == 'add':
        result = add_numbers(numbers[0], numbers[1])
    elif operation == 'subtract':
        result = subtract_numbers(numbers[0], numbers[1])
    elif operation == 'multiply':
        result = multiply(numbers)
    elif operation == 'divide':
        result = divide(numbers)
    else:
        print("Error: Unsupported operation.")
        sys.exit(1)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
