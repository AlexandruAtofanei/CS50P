# Import random library
import random

def main():

    # Ask user for input through function
    get_level()
    # Define score variable and initialize it to value 0
    score = 0
    # Infinite loop that generates the user 10 math problems
    i = 1
    j = 1
    while i < 11:
        x,y = generate_integer()
        prompt = int(input(f"{x} + {y} = "))
        z = x + y
        # Condition if user inputs wrong answer three times
        if prompt == z:
            score = score + 1
        else:
            while True:
                print("EEE")
                prompt = int(input(f"{x} + {y} = "))
                j = j + 1
                if prompt == z:
                    break
                elif j == 3:
                    print("EEE")
                    print(f"{x} + {y} = {z}")
                    break
        i = i + 1
    print(f"Score: {score}")

# Define fction that will promp the user for level; checking required conditions through an infinite loop
def get_level():
    while True:
            global level
            level = int(input("Level:"))
            if 1 <= level <=3:
                return level
            else:
                pass

# Define fction that randomly returns two integers with "level" number of digits
def generate_integer():
    if level == 1:
        n = 0
        m = 9
    elif level == 2:
        n = 10
        m = 99
    else:
        n = 100
        m = 999
    x = random.randint(n, m)
    y = random.randint(n, m)
    return x, y

if __name__ == "__main__":
    main()
