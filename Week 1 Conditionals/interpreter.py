def main():

  # Ask user for the math problem
    ask = input("Please provide your math problem! ")

# Split input in to three variables
    x , y , z = ask.split()
    x = int(x)
    z = int(z)
# Define conditionals for the operators
    if y == "+":
        print(float(x + z))
    elif y == "-":
        print(float(x - z))
    elif y == "*":
        print(float(x * z))
    else:
        print(float(x / z))

main()
