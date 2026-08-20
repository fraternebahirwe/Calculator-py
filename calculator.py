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

def multiply_numbers(num1, num2):
    """
    Multiply two numbers.

    Parameters:
    num1 (float): The first number to be multiplied.
    num2 (float): The second number to be multiplied.

    Returns:
    float: The product of num1 and num2.
    """
    # Calculate the product of the two numbers
    result = num1 * num2
    return result


def divide_numbers(num1, num2):
    """
    Divide one number by another.

    Parameters:
    num1 (float): The number to be divided.
    num2 (float): The number to divide by.

    Returns:
    float: The quotient of num1 divided by num2.

    Raises:
    ValueError: If num2 is zero, an error will be raised since division by zero is not allowed.
    """
    # Check if the divisor is zero to avoid division by zero
    if num2 == 0:
        raise ValueError("Error: Division by zero is not allowed.")
    
    # Calculate the quotient
    result = num1 / num2
    return result


# Example usage of the functions
if __name__ == "__main__":
    a = 10
    b = 5

    # Multiplying two numbers
    product_result = multiply_numbers(a, b)
    print(f"The product of {a} and {b} is: {product_result}")

    # Dividing two numbers
    try:
        divide_result = divide_numbers(a, b)
        print(f"The quotient of {a} divided by {b} is: {divide_result}")
    except ValueError as e:
        print(e)


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
        result = multiply_numbers(numbers[0], numbers[1])  # Use multiply_numbers
    elif operation == 'divide':
        result = divide_numbers(numbers[0], numbers[1])  # Use divide_numbers
    else:
        print("Error: Unsupported operation.")
        sys.exit(1)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
