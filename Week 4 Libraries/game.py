# Import random library
import random

# Import command-line arguments library
import sys

def main():
# Define a variable that picks a random number between 1 and input
    try:
        rand = random.randrange(1, level("Level:"))
    except ValueError:
        rand = 1

# Infinite loop until user guesses the random number
    while True:
        try:
            guess = int(input("Guess:"))
            if guess < rand:
                print("Too small!")
            elif guess > rand:
                print("Too large!")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass

# Define a function that checks the input for int condition
def level(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
