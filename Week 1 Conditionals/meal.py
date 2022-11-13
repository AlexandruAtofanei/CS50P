def main():

    # Ask the user for the time
    ask = input("What time is it? ")
    # Convert the input using defined function
    t = convert(ask)

    # Define conditionals
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

# Define convert function
def convert(time):
    # Split input into hours and minutes
    hours , minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    time = (60*hours + minutes)/60
    return float(time)

if __name__ == "__main__":
    main()
