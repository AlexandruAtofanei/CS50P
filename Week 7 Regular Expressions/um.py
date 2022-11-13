import re


def main():

    # Print the number of "um" that are in the users input
    print(count(input("Text: ")))

# Define a functions that finds all the "um" in the input
def count(s):
    count = (re.findall(r"\bum\b", s, re.IGNORECASE))
    return len(count)


if __name__ == "__main__":
    main()
