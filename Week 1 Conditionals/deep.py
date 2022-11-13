def main():
    
# Ask user for his input striping any backspace and lower-casing it.
    ask = input("What is the answer of the great Question of Life, the Universe and Everything? ").strip().lower()
  
# Check the given conditions
    if ask == "42" or ask == "forty two" or ask== "forty-two":
        print("Yes")
    else:
         print("No")

main()
