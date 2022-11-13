import sys
import os
from PIL import Image, ImageOps

def main():
        # Case-insensitive arguments
        sys.argv[1] = sys.argv[1].lower()
        sys.argv[2] = sys.argv[2].lower()
        # Check the gven condtions
        if len(sys.argv) == 3 and check_format(sys.argv[1],sys.argv[2]) == True:
            fit_image(sys.argv[1],sys.argv[2])
        else:
            sys.exit("Please specify exactly two command-line arguments!")

# Define a fnctions that checks all given conditions
def check_format(input, output):
    # Define list with the valid formats
    valid_format = [".jpg", ".jpeg", ".png"]
    # Spliting the root from the extension
    _, input_format = os.path.splitext(input)
    _, output_format = os.path.splitext(output)
    # Check if input and output have the same formats
    if input_format != output_format:
        sys.exit("Input and output have different extensions")
    # Check if the input and output have one of the valid formats
    elif input_format not in valid_format or output_format not in valid_format:
        sys.exit("Extension is not correct!")
    else:
        return True

# Define a fuction that fits, overlais the two images and saves to output
def fit_image(input, output):
    # Define exception
    try:
        with Image.open("shirt.png") as shirt:              # Open shirt.png
            with Image.open(input) as base:                 # Open the input
                base = ImageOps.fit(base, shirt.size)       # Size and crop the input as per shirt
                base.paste(shirt, shirt)                    # Paste shirt to the input
                base.save(output)                           # Save result as output
    except FileNotFoundError:
        sys.exit("The specified input does not exist")

if __name__ == "__main__":
    main()
