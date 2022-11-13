def main():

    # Ak user for input
    ask = input("How are you? ")
    # Print the input with the vowels removed
    print(shorten(ask))
# Define a function that removes vowels from the input
def shorten(word):
    # Define list of vowels
    vowels = ["A", "E", "I", "O", "U"]
    # Loop through the input and find and remove vowels.
    for vowel in vowels:
        if vowel or vowel.lower() in word:
            word = word.replace(vowel,"").replace(vowel.lower(),"")
    return word

if __name__ == "__main__":
    main()
