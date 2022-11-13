# Import requred libraries
import json
import sys
import requests

def main():

    # Check if command-line argument is a float
    try:
        sys.argv[1] = float(sys.argv[1])
    except ValueError:
        sys.exit("Not a float")

    # Get data from URL
    try:
        data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("URL not reacheable")

    # Format data in .json
    data = data.json()

    # Define variable that contains the rate_float
    rate = float(data['bpi']['USD']['rate_float'])

    # Define variable that contains the total amount
    total = rate * sys.argv[1]

    # Print the amount with 4 decimals
    print(f"${total:,.4f}")

main()
