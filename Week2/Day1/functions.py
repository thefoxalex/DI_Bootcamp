# Functions always start with "def" (short for define)

def say_hello():
    """A function that says hello"""
    print("Hello!")

say_hello()

def say_hello(username):
    print(f"Hello {username}")

say_hello('Alex')
say_hello('Claws')
say_hello('Dada')
say_hello('Kipling')
say_hello('Keats')


def say_hello(username, language):
# Can create default by writing this:  def say_hello(username, language="EN"):  

    if language == 'EN':
        print(f"Hello {username}")
    elif language == 'CL':
        print(f"FHHEIE {username}")
    elif language == 'IT':
        print(f"Ciao {username}")
    elif language == 'HE':
        print(f"Shalom {username}")
    else:
        print("Sorry, this language is not supported: " + language)    

say_hello(username='Alex', language='EN')
say_hello('Claws', 'CL')
say_hello('Dada', 'IT')
say_hello('Kipling', 'HE')
say_hello('Keats', 'HE')

# TO ASK A USERNAME AND LANGUAGE

# username = input("What's your name? ")
# language = input("Language preference? ")
# say_hello(username, language)

# ALTERNATE : say_hello(input('What is your name? '), input('Which language do you prefer? '))

# LOCAL AND GLOBAL SCOPE

my_number = 11

# def numberator(number): # local scope
#     new_number = my_number * number # local scope
#     print(f"{my_number} times {number} is {new_number}") # local scope

# numberator(2)

# print(my_number) # Global scope

def numberator(number): 
    new_number = my_number * number 
    return new_number

my_val = numberator(2) # Storing the return into a new variable ("my_val")
print(my_val * 8) # Doing something else with the return


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('eric', 'clapton') 
print(musician)



def divide_by_three(number):
  return number / 3

first_number = 12
first_number_computed = divide_by_three(first_number)
print(first_number_computed)


second_number = 27
second_number_computed = divide_by_three(second_number)
print(second_number_computed)



# EXERCISE

# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

# For example:

def calculation(a, b):
    return (a - b, a + b)

res = calculation(40, 10)
print(res)

# So you can do things with the number values if you want instead of them being inside a tuple
minus, plus = calculation(40, 10)
print(minus, plus)


def greet_users(users):             # users should be a list
    for user in users:              # Because it's a list, we can loop through it
        print("Hello " + user.title() + " !")       # For each user, print "hello" and then his name

usernames = ["steve", "stan", "debbie"]
greet_users(usernames)



def print_models(unprinted_designs, completed_models):
    """    
    Simulate printing each design until none are left.    
    Move each design to completed_models after printing.    
    """

    while unprinted_designs:        
        current_design = unprinted_designs.pop()            

        # Simulate creating a 3D print from the design.        
        print("Printing model: " + current_design)        
        completed_models.append(current_design)        

def show_completed_models(completed_models):    
    """
    Show all the models that were printed.
    """    
    print("\nThe following models have been printed:")   
    for completed_model in completed_models:        
        print(completed_model)        

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)



# *** IMPORTANT *** 
# 
# map() Function

def upper_string(s):
    return s.upper()

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(upper_string, fruit)

print(list(map_object))


#filter()

def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filtered_object = filter(starts_with_A, fruit)

print(list(filtered_object))


# functools.reduce()

from functools import reduce

def sum_numbers(first, second):
    return first+second

my_list = [1, 3, 5, 7]
reduced_list = reduce(sum_numbers, my_list)

print(reduced_list)


# *** IMPORTANT *** 
# Lambda Functions

# lambda arg1, arg2: value_returned

# A function that returns a string in capital letters:
# lambda s: s.upper()

# You can also store this function into a variable if you want to reuse it:

# my_function = lambda s: s.upper()
# # This is the same as doing: 
# def my_function(s):
#     return s.upper()


# Those functions can be handy when using maps, filter, and reduce operations because they allow you to create it quickly. For example, let’s recreate the previous snippets using lambda functions.

# The map example:

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(lambda s: s.upper(), fruit)

# print(list(map_object))


# The filter example:

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# filtered_object = filter(lambda s: s[0] == "A", fruit)

# print(list(filtered_object))


# The reduce example:

# from functools import reduce
# my_list = [1, 3, 5, 7]
# reduced_list = reduce(lambda first, second: first+second, my_list)

# Exercise
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters

filtered_object = filter(lambda name: len(name) <= 4 , people)
map_object = map(lambda name: f"Hello {name}", filtered_object)
print(list(map_object))

# *****

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
def show_tree():
    for image in picture:
        for pixel in image:
            if (pixel):
                print('*', end="")
            else:
                print(' ', end="")
        print('')            

show_tree()
