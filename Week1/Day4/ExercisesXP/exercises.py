# EXERCISE 1: FAVORITE NUMBERS
# Instructions:
# Create a set called my_fav_numbers and populate it with your favorite numbers.
my_fav_numbers = {5, 7, 22, 11}
# Add two new numbers to the set.
my_fav_numbers.add(13)
my_fav_numbers.add(77)
# Remove the last number you added to the set.
my_fav_numbers.remove(77)
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
friend_fav_numbers = {4, 88, 202, 14}
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.
print(our_fav_numbers)

# EXERCISE 3: LIST MANIPULATION

# Instructions:

# You have a list: 

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove "Banana" from the list.

basket.remove("Banana")
# Remove "Blueberries" from the list.
basket.remove("Blueberries")
# Add "Kiwi" to the end of the list.
basket.append("Kiwi")
# Add "Apples" to the beginning of the list.
basket.insert(0, "Apples")
# Count how many times "Apples" appear in the list.
# "Apples" appears twice in the list.
# Empty the list.
basket.clear()

# Print the final state of the list.
print(basket)

# EXERCISE 4: FLOATS

# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
# # Avoid hard-coding each number manually.
# # Think: Can you generate this sequence using a loop or another method?

my_int = [number * 1 for number in range(2, 6)]
print(my_int)

my_list = [number * 0.5 for number in range(3, 11, 2)]
print(my_list)

result = my_int + my_list
result.sort()
print(result)


# EXERCISE 5: FOR LOOP

# Instructions:

# Write a for loop to print all numbers from 1 to 20, inclusive.

my_numbers = range(1, 21)

for number in my_numbers:    
    print(number)

# Write another for loop that prints every number from 1 to 20 where the index is even.

even_numbers = range(2, 21, 2)

for even in even_numbers:
    print(even)

# EXERCISE 6: WHILE LOOP

# Instructions:

# Use an input to ask the user to enter their name.

while True:
    your_name = input("Please enter your name: ")

    if len(your_name) >= 3 and your_name.isalpha():
        print("Thank you!")
        break

# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop


# EXERCISE 7: FAVORITE FRUITS

# Instructions:

# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

user_input = input("What are your favorite fruits? (please use a space between each fruit) ")

user_favorites = user_input.split() 

more_fruits = input("Please add another fruit: ")

new_fruits = more_fruits.split()

if user_favorites == new_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# EXERCISE 8: PIZZA TOPPINGS

# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.


pizza_toppings = []

while True:
    pizza = input("Please add a pizza topping (type 'quit' to quit): ")

    if pizza == "quit":
        break

    pizza_toppings.append(pizza)
    
    for topping in pizza_toppings:
        
        print(f"Adding {topping} to your pizza.")
    
    subtotal = len(pizza_toppings)    
    
    base = 10.00
    
    pizza_total = base + subtotal * 2.50    

print(pizza_toppings, "Here is your total: ", pizza_total)   

# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.


# EXERCISE 9: CINEMAX TICKETS
# Instructions:

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

# user_age = []

# while True:
#     user_age = int(input ("Please enter the age of the person: "))
    
#     user_total.append(user_age)
    
#     if user_age < 3:
#         cost = 0
#     if user_age >= 3:
#         cost = 10
#     if user_age <= 12:
#         cost = 0    
#     if user_age < 12:
#         cost = 15
    
#     total_ticket_cost = sum(user_total) 


# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.