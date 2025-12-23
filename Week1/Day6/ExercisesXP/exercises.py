# Exercise 1: Converting Lists into Dictionaries
# Key Python Topics:

# Creating dictionaries
# Zip function or dictionary comprehension


# Instructions
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.



# Lists:

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict1 = dict(zip(keys, values))

print(my_dict1)

# Expected Output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# Exercise 2: Cinemax #2
# Key Python Topics:

# Looping through dictionaries
# Conditionals
# Calculations


# Instructions
# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15


# Family Data:
free = 0
child = 10
adult = 15

total_cost = 0

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

for age in family.values():
    print({age})
    if age < 3:
        cost = free
    if age >= 3 or age <= 12:
        cost = child

    if age > 12:
        cost = adult
   

# total_cost = sum(cost)

# print(total_cost)



# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.


# Bonus:

# Allow the user to input family members’ names and ages, then calculate the total ticket cost.