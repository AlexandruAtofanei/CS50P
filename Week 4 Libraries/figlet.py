# Install # installing the 3rd party figlet library
# pip install pyfiglet

# Importing the pyfiglet library, Figlet function
from pyfiglet import Figlet
# Import random library
import random
# Import command-line arguments library
import sys

# Define variable for the available fonts in Figlet
figlet = Figlet()
fonts = figlet.getFonts()

# Define conditions: only 0 or 2 command-line argumets and fonstyle ; exit if conditions are not met
if len(sys.argv) == 3 and sys.argv[1] == ("-f" or "--font") and sys.argv[2] in fonts:
    # Ask user for input
    s = input()
    # Set font from the users command line input
    figlet.setFont(font=sys.argv[2])
    # Print with new font
    print(figlet.renderText(s))
elif len(sys.argv) == 1:
    # Random choose a font
    f = random.choice(fonts)
    # Set the random choosen font
    figlet.setFont(font=f)
    # Ask user for input
    s = input()
    # Print input with the randomized font
    print(figlet.renderText(s))
    # Exit with message if conditions are not met
else:
    sys.exit("Invalid usage")
