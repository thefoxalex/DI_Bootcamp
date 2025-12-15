# 1. ask the user to enter his/her name

# 2. use the len() function to check the lenght of the name. if it is less than 5 letter print('You have a short name :)')

name = input('What is your name? ')

if len(name) < 5:
    print('You have a short name :)')

elif len(name) > 5:
    print('You have a long name.')

else:
    print(f'Bye-bye, {name}!')

print(f'Bye-bye, {name}!')