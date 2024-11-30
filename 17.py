"""
exercise 17
"""
from functools import reduce
import time


def multi(x, y):
    return x * y


def factorial_map(n):
    """
    can also use std's math.factorial(n), writing one using map and reduce for exercise's sake
    """
    return reduce(multi, map(int, range(1, n + 1)))


if __name__ == "__main__":
    start_time = time.time()
    # I advice against printing result
    result = factorial_map(10_000_000)
    end_time = time.time()
    print(f"Factorial of 10,000,000 calculated in {end_time - start_time:.2f} seconds.")
