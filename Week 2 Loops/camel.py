def main():
    
# Ask user for his input
    s = input("what is your name? ")
# Iterate through the caracters of the string
    for c in s:
        if c == c.capitalize():
            # Replace capitalize caracter with "_c"
            # c = c.replace(c, f"_{c}").lower()
            # print(c, end="")
            print(c.replace(c, f"_{c.lower()}"), end="")

        else:
            print(c, end="")

main()
