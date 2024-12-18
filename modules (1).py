
import math
import random

# Using math module
def rhombus_area(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

# Using random module
def generate_random_numbers(n, a, b):
    return [random.randint(a, b) for _ in range(n)]

if __name__ == "__main__":
    print(rhombus_area(10, 8))  # Output: 40.0
    print(generate_random_numbers(5, 1, 100))
