#!/usr/bin/python3
import sys

def factorial(n):
    """
    Compute the factorial of a number n.
    Raise an error if n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid an infinite loop
    return result

if __name__ == "__main__":
    try:
        # Ensure the user provides exactly one argument
        if len(sys.argv) != 2:
            print("Usage: ./factorial.py <non-negative integer>")
            sys.exit(1)

        # Parse and calculate the factorial
        num = int(sys.argv[1])
        f = factorial(num)
        print(f)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

