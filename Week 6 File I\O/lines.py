import sys

def main():

    # Check the requied conditions for agument and print number of lines
    if sys.argv[1].endswith(".py") and len(sys.argv) == 2:
        print(count_lines(sys.argv[1]))
    else:
        sys.exit("Please specify the name (or path) of a Python file in one command-line argument!")

# Define a function that counts the lines in a file excluding comments and blank lines.
def count_lines(code_file):
    # Init variable that will store the number of lines
    count = 0
    # Define exception
    try:
        # Open the file
        with open(code_file) as file:
            # Read all the lines in the file and return them in a list
            lines = file.readlines()
        # Loop through the elements of the list
        for line in lines:
            line = line.lstrip()
            # Condition to exclude comments and blanck lines
            if line.startswith("#") or len(line) == 0:
                continue
            # Update counter
            count += 1
        return count
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
