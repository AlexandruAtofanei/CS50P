def main():

# Ask user for the file name striping any backspace and lower-casing it.
    ask = input("What`s the file name? ").strip().lower()

# Check the files extension type
    if ask.endswith(".gif"):
        print("image/gif")
    elif ask.endswith(".jpg"):
        print("image/jpeg")
    elif ask.endswith("jpeg"):
        print("image/jpeg")
    elif ask.endswith(".png"):
        print("image/png")
    elif ask.endswith(".pdf"):
        print("application/pdf")
    elif ask.endswith(".txt"):
        print("text/plain")
    elif ask.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()
