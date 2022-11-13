import sys
import csv

def main():

# Check the requied conditions for agument and print new csv
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv") and len(sys.argv) == 3:
        formated_csv(sys.argv[1], sys.argv[2])
    else:
        sys.exit("Please specify the name of two csv files in a two command-line argument!")

# Define a function that outputs a csv with the new required column order
def formated_csv(input, output):
    # Define exception
    try:
        # Open and read the given csv
        with open(input) as input_file:
            reader = csv.DictReader(input_file)
            # Create and write to new csv
            with open(output, "w") as output_file:
                writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
                # Write the header to the new file
                writer.writeheader()
                # Loop to write to new csv with new column order
                for row in reader:
                    last, first = row["name"].split(",")
                    house = row["house"]
                    writer.writerow({"first" : first.strip(), "last" : last, "house" : house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")

if __name__ == "__main__":
    main()
