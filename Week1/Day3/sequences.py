my_list = ["one", 2, "apple", 55, "pear", 89]

print(my_list[0]) # Forwards through the list, starting at 0

print(my_list[-1]) # Backwards through the list, starting at 1

print(my_list[0:2]) # Range index, does not include last element

print(my_list[2:5]) # Another range example

# Strings are actually sequences

my_name = "Alex"

print(my_name[0])
print(my_name[1])
print(my_name[2])
print(my_name[3])

# Add an item to the list
my_list.append("cats") 
print(my_list)

#Remove an item from the list
my_list.remove(89)
print(my_list)

#Or using pop
my_list.pop(0)
print(my_list)

#without value will remove last item
my_list.pop()
print(my_list)

#LIST FUNCTIONS

#Length using len()

len(my_list) 

#Sum of numbers (use with int not strings)
# sum(my_int)

#Sorting using sorted()
my_numbers = [9, 6000, 278, 200]
print(sorted(my_numbers))

#With strings, will alphabetize
my_letters = ["f", "b", "x", "n"]
print(sorted(my_letters))

#Insert
my_letters.insert(0, "x")
print(my_letters)

#Extend
my_letters.extend(["g", "l"])
print(my_letters)


#SETS
#cannot have duplicates
my_set = set()

my_set.add("Claws")
my_set.add("Dada")
print(my_set)

this_set={"Claws", "cat", "Dada", "Kipling", "cat", "Keats"}
print(this_set)
#will not print duplicate values