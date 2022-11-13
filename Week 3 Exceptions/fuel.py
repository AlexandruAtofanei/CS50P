def main():

    check("what`s the fraction? ")

# Define a function that checks for the given conditions and prints
def check(prompt):
    while True:
        # Create exceptions
        try:
            # Ask user for the input
            x, y = input(prompt).split("/")
            # Convert to integer
            x = int(x)
            y = int(y)
            # Convert to procentile rounding to nearest integer
            z = int(round(x / y * 100, 0))
            # Check if the tank is empty
            if z <= 1:
                return print("E")
            # Check if the tank is full
            elif 99 <= z <= 100:
                return print("F")
            # Return procentile
            elif z <= 100:
                return print(f"{z}%")
        except (ValueError, ZeroDivisionError):
            pass

main()
