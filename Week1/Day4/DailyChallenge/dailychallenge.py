# Challenge 1: Multiples of a Number

# Instructions:
# 1. Ask the user for two inputs:

# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

input_number = int(input("Please provide a number: "))
input_length = int(input("Please provide a length: "))

for num in range (1, input_length):
    print(input_length * num )

# Challenge 2: Remove Consecutive Duplicate Letters

# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.

# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.

# Example 1:

# Input:
# user’s word: "ppoeemm"
# Output: 
# "poem"

user_word = input("Please type a word with consecutive duplicate letters (e.g., 'pppoooeeemm' for 'poem'): ")

new_word = ""

for letter in user_word:
    if new_word == "" or letter != new_word[len(new_word) - 1]:
        new_word = new_word + letter

print(new_word)

# Example 2:

# Input:
# user’s word: "wiiiinnnnd"
# Output:
# "wind"


# Example 3:

# Input:
# user’s word: "ttiiitllleeee"
# Output:
# "title"


# Example 4:

# Input:
# user’s word: "cccccaaarrrbbonnnnn"
# Output:
# "carbon"