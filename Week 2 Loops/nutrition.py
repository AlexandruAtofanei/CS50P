def main():
    
# Ask user for the input
    k = input("What fruit do you prefer ? ").title()
# Define dict with FDA info
    FDA = {
    "Apple": "130", "Avocado": "50",
    "Banana": "110", "Cantaloupe": "50",
    "Grapefruit": "60", "Grapes": "90",
    "Honeydew Melon" : "50", "Kiwifruit": "90",
    "Lemon": "15", "Lime": "20",
    "Nectarine": "60", "Orange": "80",
    "Peach": "60", "Pear": "100",
    "Pineapple": "50", "Plums": "70",
    "Strawberries": "50", "Sweet Cherries": "100",
    "Tangerine": "50", "Watermelon": "80"
}
# Query through the dict
    if k in FDA:
# Print the Value found in the dict
        print(FDA[k])

main()
