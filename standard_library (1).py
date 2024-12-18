
import math
import random

# Using math for Pythagoras
def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

# Guess-the-number game
def guess_the_number():
    number = random.randint(1, 50)
    guess = 0
    while guess != number:
        guess = int(input("Guess a number between 1 and 50: "))
        if guess == number:
            print("Correct! You guessed the number.")
        else:
            print("Wrong guess. Try again.")

if __name__ == "__main__":
    print(pythagoras(3, 4))  # Output: 5.0
    # Uncomment the following line to play the game
    # guess_the_number()
