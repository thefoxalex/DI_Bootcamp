# Ask the user for a number between 1 and 100

user = int(input('Please provide a number between 1 and 100: '))

# If the number is a divisible by three, print Fizz
if user % 3 == 0 and user % 5 == 0:
    print('FizzBuzz')

elif user % 3 == 0:
    print('Fizz')

# If the number is a divisible by five, print Buzz.

elif user % 5 == 0:
    print('Buzz')

# If the number is a divisible by both three and five, print FizzBuzz instead.
