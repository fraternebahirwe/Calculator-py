import sys

class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# Dictionary to map operation names to functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def parse_numbers(args):
    """Convert command-line arguments to a list of numbers."""
    numbers = []
    for arg in args:
        try:
            number = float(arg)  # Try to convert to float
            numbers.append(number)
        except ValueError:
            print(f"Error: '{arg}' is not a valid number.")
            return None  # Return None to indicate an error
    return numbers

def process_command_line_args():
    """Process command-line arguments for calculator operations."""
    if len(sys.argv) != 4:  # Check for the expected number of arguments
        print("Error: Expected operation and two numbers.")
        return False

    operation = sys.argv[1].lower()
    numbers = parse_numbers(sys.argv[2:])  # Parse and convert inputs

    if numbers is None or len(numbers) != 2:
        print("Error: Exactly two valid numbers are required.")
        return False

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
    """Main function to run the calculator."""
    while True:  # Start an infinite loop for interactive mode
        # Check for command-line arguments
        if len(sys.argv) == 4 and process_command_line_args():
            break  # Exit after processing command-line args

        # If no command-line args, prompt for user input
        user_input = input("Enter operation (add, subtract, multiply, divide) followed by two numbers (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the calculator.")
            break
            
        parts = user_input.split()
        if len(parts) != 3:
            print("Error: Please provide an operation followed by two numbers.")
            continue  # Start the next iteration of the loop

        operation = parts[0].lower()
        numbers = parse_numbers(parts[1:])  # Parse and convert inputs

        if numbers is None or len(numbers) != 2:
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
