def main():

    # Define the menu using a dictionary
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
     "Quesadilla": 8.50,
     "Super Burrito": 8.50,
     "Super Quesadilla": 9.50,
      "Taco": 3.00,
      "Tortilla Salad": 8.00
    }
    # Define a variable that will increment each input with the value from dict
    bill = 0
    # Loop through users input updating the bill
    while True:
        # Define exceptions
        try:
            # Ask user for input, titlecsing it
            x = input("What will you order? ").lower().title()
            # Get the value from the dict
            z = menu.get(x)
            # Update the bill
            bill = bill + z
            # Print updated bill
            print(f"Total: ${bill:.2f}")
        except (KeyError, TypeError):
            pass
        except EOFError:
            print("\n")
            break

main()
