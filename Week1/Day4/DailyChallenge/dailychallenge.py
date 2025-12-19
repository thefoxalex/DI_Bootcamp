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

word = input("Type a string with consecutive duplicate letters (e.g., 'ppooeemm' for 'poem'):")
new_word = ""

for letter in range(len(word)):
    if word[letter] == word[letter + 1]:
        continue
    else:
        new_word += word[letter]
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