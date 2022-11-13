def main():

    # Ask user for an the input
    ask = input("Any thoughts? ")

    #Print converted input
    print(f"{convert(ask)}")

# Define a function that converts caracters to smiley faces
def convert(x):
    return x.replace(":)", "🙂").replace(":(", "🙁")

main()
