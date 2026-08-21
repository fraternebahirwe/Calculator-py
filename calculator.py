import sys

class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass

def add(x, y):
    """Return the sum of two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """Return the difference of two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The result of x minus y.
    """
    return x - y

def multiply(x, y):
    """Return the product of two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """Return the quotient of two numbers.

    Args:
        x (float): The dividend.
        y (float): The divisor.

    Raises:
        ValueError: If y is zero, as division by zero is not allowed.
        
    Returns:
        float: The result of x divided by y.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# Dictionary to map operation names to their corresponding functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def parse_numbers(args):
    """Convert command-line arguments to a list of numbers.

    Args:
        args (list): A list of strings representing numbers.

    Returns:
        list: A list of floats representing the parsed numbers, or None if any input is invalid.
    """
    numbers = []
    for arg in args:
        try:
            number = float(arg)  # Try to convert to float
            numbers.append(number)  # Append valid number to the list
        except ValueError:
            print(f"Error: '{arg}' is not a valid number.")
            return None  # Return None to indicate an error
    return numbers

def process_command_line_args():
    """Process command-line arguments for calculator operations.

    Validates the number of arguments, parses the numbers, and performs the requested operation.

    Returns:
        bool: True if processing was successful, otherwise False.
    """
    if len(sys.argv) != 4:  # Check for the expected number of arguments
        print("Error: Expected operation and two numbers.")
        return False

    operation = sys.argv[1].lower()
    numbers = parse_numbers(sys.argv[2:])  # Parse and convert inputs

    if numbers is None or len(numbers) != 2:
        print("Error: Exactly two valid numbers are required.")
        return False

    # Perform the operation based on the user's choice
    try:
        if operation in operations:
            result = operations[operation](numbers[0], numbers[1])
            print(f"Result: {result}")
        else:
            print("Error: Unsupported operation.")
    except CalculatorError as error:
        print(f"Error: {error}")

    return True

def main():
    """Main function to run the calculator.

    Continuously prompts the user for input or processes command-line arguments.
    Allows the user to perform basic arithmetic operations or exit the program.
    """
    while True:  # Start an infinite loop for interactive mode
        # Check for command-line arguments
        if len(sys.argv) == 4 and process_command_line_args():
            break  # Exit after processing command-line args

        # If no command-line args, prompt for user input
        user_input = input("Enter operation (add, subtract, multiply, divide) followed by two numbers (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the calculator.")
            break  # Exit the loop
            
        parts = user_input.split()  # Split the input into parts
        # Ensure that the user provided exactly one operation and two numbers
        if len(parts) != 3:
            print("Error: Please provide an operation followed by two numbers.")
            continue  # Start the next iteration of the loop

        operation = parts[0].lower()
        numbers = parse_numbers(parts[1:])  # Parse and convert inputs

        if numbers is None or len(numbers) != 2:  # Validate if two numbers were provided
            print("Error: Exactly two valid numbers are required.")
            continue  # Start the next iteration of the loop

        # Perform the operation
        try:
            if operation in operations:
                result = operations[operation](numbers[0], numbers[1])
                print(f"Result: {result}")
            else:
                print("Error: Unsupported operation.")
        except CalculatorError as error:
            print(f"Error: {error}")

if __name__ == "__main__":
    main()
