def main():

    price = 50
    # Loop until conditions are met
    while True:
        # Ask the user for coins 25, 10 or 5 are accepted
        coin = int(input("Please insert coin! "))
        # Condition to provide only 25,10,5
        if coin in [5, 10, 25]:
            # Calculate remaining
            r = price - coin
            # Check if user inserted total price
            if r >= 5:
                print(f"Amount due {r}")
                price = r
            else: return print(f"Changed owned {abs(r)}")
        else: print("Amount due: 50")

main()
