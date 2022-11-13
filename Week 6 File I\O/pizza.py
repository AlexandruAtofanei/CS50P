from tabulate import tabulate
import sys
import csv


def main():

    #Check if argument ends with .csv
    if sys.argv[1].endswith(".csv") and len(sys.argv) == 2:
        format_ascii(sys.argv[1])
    else:
        sys.exit("Please specify the name (or path) of a csv file in one command-line argument!")

# Define a function that outputs a table formatted as ASCII art using tabulate
def format_ascii(csv_file):
    # Define exception
    try:
        # Open file and read it using csv reader
        with open(csv_file) as file:
            table = csv.DictReader(file)
            print(tabulate(table, headers = "keys", tablefmt = "grid"))
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
