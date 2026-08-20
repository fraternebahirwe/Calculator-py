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
    return num1 + num2

def subtract_numbers(num1, num2):
    """
    Subtract two numbers.
    
    Parameters:
    num1 (float): The number from which to subtract.
    num2 (float): The number to subtract.

    Returns:
    float: The difference between num1 and num2.
    """
    return num1 - num2

def multiply_numbers(num1, num2):
    """
    Multiply two numbers.
    
    Parameters:
    num1 (float): The first number to be multiplied.
    num2 (float): The second number to be multiplied.

    Returns:
    float: The product of num1 and num2.
    """
    return num1 * num2

def divide_numbers(num1, num2):
    """
    Divide one number by another.
    
    Parameters:
    num1 (float): The number to be divided.
    num2 (float): The number to divide by.

    Returns:
    float or str: The quotient of num1 divided by num2 or an error message if division by zero.
    """
    
    if num2 == 0:
          return "Error: Division by zero is not allowed by Fraterne'system."
    return num1 / num2
 
def parse_numbers(args):
    """Convert command line arguments to a list of numbers."""
    numbers = []
    for arg in args:
        try:
            number = float(arg)  # Try to convert to float
            numbers.append(number)  # Add valid number to the list
        except ValueError:
            print(f"Error: '{arg}' is not a valid number.")  # Print error for invalid input
            sys.exit(1)  # Exit the program with an error code
    return numbers


def main():
    """Main function to run the calculator."""
    # Check for the right number of arguments
    # We expect at least 3 arguments: the operation and two numbers
    if len(sys.argv) != 4:
        print("Usage: calc <operation> <number1> <number2>")
        print("Supported operations: add, subtract, multiply, divide")
        sys.exit(1)
    
    # Extract the operation type and parse numbers
    operation = sys.argv[1].lower()  # Get the operation type
    numbers = parse_numbers(sys.argv[2:])  # Parse and convert inputs

    # It's already ensured that we get exactly two numbers in parse_numbers
    if len(numbers) != 2:
        print("Error: Exactly two numbers are required.")
        sys.exit(1)

    try:
        # Perform the chosen operation
        if operation == 'add':
            result = add_numbers(numbers[0], numbers[1])
        elif operation == 'subtract':
            result = subtract_numbers(numbers[0], numbers[1])
        elif operation == 'multiply':
            result = multiply_numbers(numbers[0], numbers[1])
        elif operation == 'divide':
            result = divide_numbers(numbers[0], numbers[1])
        else:
            print("Error: Unsupported operation.")
            sys.exit(1)

        print(f"Result: {result}")

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
