import re

def main():

    # Validate the users input
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Split the users IP input in to 4 groups using re.search
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        # Define a variable for each match.group
        v, x, y, z = matches.groups()
        # Check if the variables meet the required range condition
        if 0 <= int(v) <= 255 and 0 <= int(x) <= 255 and 0 <= int(y) <= 255 and 0 <= int(z) <= 255:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
