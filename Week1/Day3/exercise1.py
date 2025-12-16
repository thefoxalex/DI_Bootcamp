# Given this list:


list1 = [5, 10, 15, 20, 25, 50, 20]
list1.remove(20)
list1.insert(3, 200)

# find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value


# Hint : Look at the index method
print(list1)

# Expected output:
# list1 = [5, 10, 15, 200, 25, 50, 20]

#Instructor's solution

list2 = [5, 10, 15, 20, 25, 50, 20]
is_20 = list2.index(20)
list2[is_20] = 200

print(list2)