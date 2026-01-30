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

# Exercise 3: Zara
# Key Python Topics:

# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()


# Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.

brand = {
    'name': 'Zara',
    'creation_date': '1975',
    'creator_name': 'Amancio Ortega Gaona',
    'number_stores': 7000,
    'type_of_ clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'major_color': {
    'France': 'blue',
    'Spain': 'red',
    'US': ['pink', 'green']
    }
}
brand['number_stores'] = 2


brand['country_creation'] = 'Spain'
brand['international_competitors'].append('Desigual')
brand.pop('creation_date')
print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
number_keys = len(brand)
all_keys = brand.keys()
print(number_keys)
print(all_keys)

# Brand Information:
# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.


# Bonus:

# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

# Exercise 4: Disney Characters
# Key Python Topics:

# Looping with indexes
# Dictionary creation
# Sorting


# Instructions
# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:



# Character List:

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney1 = {key: i for i, key in enumerate(users)}
print(disney1)

disney2 = {index: value for index, value in enumerate(users)}
print(disney2)

disney3 = users.sort()
disney3 = {key: i for i, key in enumerate(users)}
print(disney3)



# Expected Results:

# 1. Create a dictionary that maps characters to their indices:

# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}


# 2. Create a dictionary that maps indices to characters:

# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}


# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:

# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}