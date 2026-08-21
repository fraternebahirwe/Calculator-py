import sys

class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass

def add_numbers(num1, num2):
    """Add two numbers."""
    return num1 + num2

def subtract_numbers(num1, num2):
    """Subtract two numbers."""
    return num1 - num2

def multiply_numbers(num1, num2):
    """Multiply two numbers."""
    return num1 * num2

def divide_numbers(num1, num2):
    """Divide one number by another."""
    if num2 == 0:
        raise CalculatorError("Division by zero is not allowed.")
    return num1 / num2

# Dictionary to map operation names to functions
operations = {
    'add': add_numbers,
    'subtract': subtract_numbers,
    'multiply': multiply_numbers,
    'divide': divide_numbers
}

def parse_numbers(args):
    """Convert command line arguments to a list of numbers."""
    numbers = []
    for arg in args:
        try:
            number = float(arg)  # Try to convert to float
            numbers.append(number)  # Add valid number to the list
        except ValueError:
            print(f"Error: '{arg}' is not a valid number.")
            return None  # Return None to indicate an error
    return numbers

def main():
    """Main function to run the calculator."""
    while True:  # Start an infinite loop for interactive mode
        # Check if command-line arguments are provided
        if len(sys.argv) == 4:  # Expecting operation and two numbers
            operation = sys.argv[1].lower()
            numbers = parse_numbers(sys.argv[2:])  # Parse and convert inputs

            if numbers is None or len(numbers) != 2:
                print("Error: Exactly two valid numbers are required.")
                continue  # Start the next iteration of the loop

            # Perform the operation
            try:
                if operation in operations:
                    result = operations[operation](numbers[0], numbers[1])
                else:
                    print("Error: Unsupported operation.")
                    continue  # Start the next iteration of the loop

                print(f"Result: {result}")

            except CalculatorError as error:
                print(f"Error: {error}")

            break  # Exit the loop after processing the command-line args
        else:
            # If no command-line args, prompt for user input
            user_input = input("Enter operation (add, subtract, multiply, divide) followed by two numbers (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the calculator.")
                break  # Exit the loop
            
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
