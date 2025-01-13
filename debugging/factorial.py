#!/usr/bin/python3
import sys

def factorial(n):
    # Ensure the the input is valid
    if n < 1:
        raise ValueError("Facorial is not define for negative numbers")

    result = 1
    while n > 1:
        result *= n
        n -= 1 # Decrement n to avoid an infinte loop
        return result

    if __name__ == "__main__":
        try:
            # Ensure the user provides an argument
            if len(sys.argv) != 2:
                print("Usage: ./factorial.py <non-negative interger>")
                sys.exit(1)

                # Parse and calculate the factorial
                f= factorial(int(sys.argv[1]))
                printf(f)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)
