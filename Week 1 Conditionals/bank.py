def main():
    
# Get the  users greeting striping any backspace and lower-casing it
    greet = input("What`s your greeting? ").strip().lower()

# Check the given conditions
    if greet.startswith("hello"):
        print("$0")
    elif greet.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
