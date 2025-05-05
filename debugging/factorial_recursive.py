#!/usr/bin/python3
import sys

# Function to calculate the factorial of a number using recursion
def factorial(n):
    """
    Function Description:
    ---------------------
    This function calculates the factorial of a given number `n` using recursion.
    The factorial of a non-negative integer `n` is the product of all positive integers less than or equal to `n`.
    It is defined as:
    - factorial(0) = 1
    - factorial(n) = n * factorial(n - 1) for n > 0
    
    Parameters:
    -----------
    n : int
        A non-negative integer for which the factorial will be calculated.
    
    Returns:
    --------
    int
        The factorial of the input integer `n`. If `n` is 0, returns 1 as per the definition of factorial.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n * factorial of (n-1)

# Getting the input number from the command line argument
f = factorial(int(sys.argv[1]))

# Output the result
print(f)

