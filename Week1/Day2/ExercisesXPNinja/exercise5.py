# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

  
your_text = input("Please write the longest sentence you can that doesn't contain the letter 'a': ")

if "a" not in your_text:
	print("Congratulations! You did it!")
else:
	print("Try again!")
