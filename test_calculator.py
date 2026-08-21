from calculator import add_numbers, subtract_numbers, multiply_numbers, divide_numbers


def test_add_numbers():
    """Test cases for the add_numbers function."""
    assert add_numbers(10, 5) == 15.0, "Test Case 1 Failed"
    assert add_numbers(-10, -5) == -15.0, "Test Case 2 Failed"
    assert add_numbers(1e10, 1e10) == 20000000000.0, "Test Case 3 Failed"
    assert add_numbers(10.5, 2.3) == 12.8, "Test Case 4 Failed"
    print("All add_numbers test cases passed!")

def test_subtract_numbers():
    """Test cases for the subtract_numbers function."""
    assert subtract_numbers(10, 5) == 5.0, "Test Case 1 Failed"
    assert subtract_numbers(-10, -5) == -5.0, "Test Case 2 Failed"
    print("All subtract_numbers test cases passed!")

def test_multiply_numbers():
    """Test cases for the multiply_numbers function."""
    assert multiply_numbers(4, 5) == 20.0, "Test Case 1 Failed"
    assert multiply_numbers(-3, 4) == -12.0, "Test Case 2 Failed"
    print("All multiply_numbers test cases passed!")

def test_divide_numbers():
    """Test cases for the divide_numbers function."""
    assert divide_numbers(20, 4) == 5.0, "Test Case 1 Failed"
    assert divide_numbers(-15, 3) == -5.0, "Test Case 2 Failed"
    assert divide_numbers(10.0, 3.0) == 3.3333333333333335, "Test Case 3 Failed"
    
    # Check division by zero case
    result = divide_numbers(10, 0)
    assert result == "Error: Division by zero is not allowed.", "Test Case 4 Failed"
    
    print("All divide_numbers test cases passed!")

def run_tests():
    """Run all test cases."""
    test_add_numbers()
    test_subtract_numbers()
    test_multiply_numbers()
    test_divide_numbers()

if __name__ == "__main__":
    run_tests()
