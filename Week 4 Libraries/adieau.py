# Intall 3rd party libray
# pip install inflect

# Import the library
import inflect
p = inflect.engine()

# Define a list in which all inputs whill be stored
list = []

# iInfinite loop to ask user for one or mutiple names
while True:
    # Define exceptions
    try:
        # Get input from user
        x = input()
        # Add input to list
        list.append(x)
    except EOFError:
        print("Adieu, adieu, to " + p.join(list))
        break
        # sys.exit("Adieu, adieu, to " + p.join(list))
