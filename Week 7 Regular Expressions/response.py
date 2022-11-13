# Import library that valdates the e-mail format
import validators

def main():

    # Print if input is a valid or invalid format
    print(validate(input("What`s your e-mail? ")))

# Define a function that uses the inported library to validate the input
def validate(address):
    if validators.email(address):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
