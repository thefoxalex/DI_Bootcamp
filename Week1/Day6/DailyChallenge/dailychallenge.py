# Challenge 1: Letter Index Dictionary
# Goal: Create a dictionary that stores the indices (number of the position) of each letter in a word provided by the user(input()).



# Key Python Topics:

# User input (input())
# Dictionaries
# Loops (for loop)
# Conditional statements (if, else)
# String manipulation
# Lists

user_word = input("Enter a word: ")

new_dict = dict(enumerate(user_word)) 
print(new_dict)



# Instructions:
# 1. User Input:

# Ask the user to enter a word.
# Store the input word in a variable.
         


# 2. Creating the Dictionary:

# Iterate through each character of the input word using a loop.
# And check if the character is already a key in the dictionary.

#     * If it is, append the current index to the list associated with that key.
#     * If it is not, create a new key-value pair in the dictionary.
# Ensure that the characters (keys) are strings.
# Ensure that the indices (values) are stored in lists.
# 3. Expected Output:

# For the input “dodo”, the output should be: {"d": [0, 2], "o": [1, 3]}.
# For the input “froggy”, the output should be: {"f": [0], "r": [1], "o": [2], "g": [3, 4], "y": [5]}.
# For the input “grapes”, the output should be: {"g": [0], "r": [1], "a": [2], "p": [3], "e": [4], "s": [5]}.


# Challenge 2: Affordable Items
# Goal: Create a program that prints a list of items that can be purchased with a given amount of money.

# Program to list purchasable items within a budget

# # 1. Define the available items and their prices in a dictionary
# available_items = {
#     "Laptop": 1200,
#     "Keyboard": 100,
#     "Mouse": 50,
#     "Monitor": 300,
#     "USB Cable": 10,
#     "External Hard Drive": 80
# }

# # Convert the input to a float (handle potential errors with try-except if needed for a robust app)
# try:
#     user_budget = float(user_budget_input)
# except ValueError:
#     print("Invalid budget amount entered. Please enter a number.")
#     # Exit the program if input is invalid
#     exit()


# # 3. Initialize a list to store the affordable items
# purchasable_items = []

# # 4. Iterate through the available items and check against the budget
# for item, price in available_items.items():
#     if price <= user_budget:
#         purchasable_items.append(item)

# # 5. Print the list of items that can be purchased
# print(f"\nWith a budget of ${user_budget:.2f}, you can purchase the following items:")

# if not purchasable_items:
#     print("No items found within your budget.")
# else:
#     for item in purchasable_items:
#         print(f"- {item}")

# Key Python Topics:

# Dictionaries
# Loops (for loop)
# Conditional statements (if, else)
# String manipulation (replace())
# Type conversion (int())
# Lists
# Sorting (sorted())


# Instructions:
# 1. Store Data:

# You will be provided with a dictionary (items_purchase) where the keys are the item names and the values are their prices (as strings with a dollar sign). The priority is defined by the position of the iten on the dictionary: from the most important to the less important.
# You will also be given a string (wallet) representing the amount of money you have.
# 2. Data Cleaning:
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}

wallet = "$300"
new_wallet = int(wallet.replace("$", ''))
characters_to_remove = "$,"

items_purchase_clean = {}

for key, value in items_purchase.items():
    clean = value
    for char in characters_to_remove:
        clean = clean.replace(char, "")
    items_purchase_clean[key] = clean

for key, value in items_purchase_clean.items():
   items_purchase_clean[key] = int(value)

basket = []

for key, value in items_purchase_clean.items():
    if value <= new_wallet:
        basket.append(key)
        new_wallet -= value
    elif value > new_wallet:
        print("Nothing.")

basket.sort()

print(basket)        
print(new_wallet)        

# You need to clean the dollar sign and the commas using python. Don’t hard code it.
# 3. Determining Affordable Items:
# create a list called basket and add there the items that you can buy with the money you have on the wallet
# Don’t forget to update the wallet after buying an item.
# If the basket is empty (no items can be afforded), return the string “Nothing”.
# Otherwise, print the basket list in alphabetical order.
# 4. Examples:

# Given:
# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
# wallet = "$300"


# The output should be: ["Bread", "Fertilizer", "Water"].

# Given:
# items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
# wallet = "$100"


# The output should be: ["Apple", "Bananas", "Fan", "Honey", "Spoon"].

# Given:
# items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
# wallet = "$1"


# The output should be: "Nothing".

