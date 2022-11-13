def main():
    # Ask user to input the value of the meal in $
    dollars = dollars_to_float(input("How much was the meal? "))

    # Ask user to input the procentual value of the tip
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # Calculate de value of the tip
    tip = dollars * percent

    # Print the calculated value of the tip
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d.removeprefix("$"))

def percent_to_float(p):
    p = float(p.removesuffix("%"))
    return p * 0.01

main()
