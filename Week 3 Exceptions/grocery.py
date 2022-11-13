def main():

# Define the dict that will store the key(grocery) and value(number)
    list = {}
# Loop to get all groceries from users input
    while True:
        # Define exceptions
        try:
            x = input().upper()
            # Check if input is in list
            if x in list:
                list [x] += 1
            else:
                list [x] = 1
        except EOFError:
            # When the user ends the inputs, sort the dict and print the value and key
            for key,value in sorted(list.items()):
                print (value, key,)
            break

main()
