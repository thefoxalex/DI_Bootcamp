# for <variable_name> in <sequence_name>:
#     CODE
#     CODE

# fruits = ['apple', 'banana', 'kiwi', 'pear']

# for fruit in fruits:
#   print(fruit)


# >> apple
# >> banana
# >> kiwi
# >> pear


# Naming conventions for lists
# Variable should be plural noun, then select individual item as singular noun

cities = ["London", "San Francisco", "Paris", "Barcelona"]

for city in cities:
    print("I once went to", city)

# The first line of the loop is:

# for city in cities:
# This line tells Python to retrieve the first value from the list cities and store it in the variable city.

# You can choose any name you want for this variable; however, it’s helpful to choose a meaningful name representing a single item from the list.    

# RANGE
numbers = range(4, 19) # numbers from 4-18 (does not include final number 19)

# for number in numbers:
#     print(number)

for number in range(10):
    print(number)

# You can store ranges in a list

numbers = list(range(1,6))
print(numbers)



# WHILE LOOPS
# can go forever
# !!! Hit CTRL + C to stop code
current_number = 1 
while current_number <= 5:    
    print(current_number)   
    current_number += 1 # Current number increases by 1 each time through the while loop

print("Finished")

#Using a Flag

# active = True # this is the "flag"

# while active: 
#     city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
#     if city == 'quit':
#         active = False
#     elif city == 'leave me alone':
#         active = False
#     elif city == 'stop':
#         active = False
#     else:
#         print("I'd love to go to", city)

# print("Goodbye !")

# Infinite Loop
# while 1 == 1: #---------->(More commonly: "while true" replaces "while 1 == 1")
#     print("Looping...")

# Break and Continue

while True: 
    city = input("Please enter the name of a city you have visited (enter 'quit'  when you are finished): ")
    if city == 'quit':
        break
    else:
        print("I'd love to go to", city)

print("Goodbye !")


# secret_number = 4

# while True:
#   user_number = input('Guess the secret number: ')
#   if int(user_number) == secret_number:
#     print('Congrats! You win!')
#     break
#   else:
#     print('Wrong guess...')

#CONTINUE

# current_number = 0
# while current_number <= 10:
#     current_number += 1
#     if 3 < current_number < 7: # If the number is between 3 and 7 
#         continue                # Go back to the beginning of the loop
#     print(current_number)
# >> 1
# >> 2
# >> 3
# >> 7
# >> 8
# >> 9
# >> 10