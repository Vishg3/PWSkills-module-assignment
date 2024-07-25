def add(a, b):
    """
    Function to add two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Function to subtract two numbers.
    """
    return a - b

def multiply(a, b):
    """
    Function to multiply two numbers.
    """
    return a * b

def divide(a, b):
    """
    Function to divide two numbers. Handles division by zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
