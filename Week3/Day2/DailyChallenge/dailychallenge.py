your_string = input("Please provide a string that is exactly 10 characters long: ")

if len(your_string) == 10:
    print("Perfect string. \n" + your_string[0] + your_string[-1])
elif len(your_string) < 10:
    print("String not long enough.")
elif len(your_string) > 10:
    print("String too long.")

new_string = ""

for character in your_string:
    new_string += character
    print(new_string)
    
