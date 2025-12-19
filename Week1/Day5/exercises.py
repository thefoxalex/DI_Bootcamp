# Access the value of key history


sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

history = sample_dict["class"]["student"]["marks"]["history"]
print(history)


# Adding an entry to existing dictionary
# keats_dict['fur_color'] = white

# Deleting an entry
# del keats_dict['fur_color']

# Delete set of keys from Python Dictionary


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}

# Expected output:

# {'city': 'New york', 'age': 25}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    del sample_dict[key]

print(sample_dict)

# IMPORTANT LIST CASTING
print(list(range(1, 10, 2)))

# VS.
for i in range(1, 10, 2):
   print(i)

# ENUMERATE
# creates index
for item in enumerate('abcd'):
    print(item)
# unpacking
# for (index_count, letter) in enumerate('abcd'):
#     print('At index {} the letter is {}'.format(index_count, letter))

    for (index_count, letter) in enumerate('abcd'):
      print(f'At index {index_count} the letter is {letter}')


# FOR ELSE

for i in range(1, 3):
    print(i)
else:
    print('The for loop is over')      

# WHILE ELSE
x = 0

while x < 2:
    print(f'x is {x}')
    x += 1
else:
    print('x is bigger than 2')    

# The basic way of appending an element into a list
# my_number = '1234'
# my_list = []

# for num in my_number:
#     my_list.append(num)
# print(my_list)


# The list comprehension way

my_number = '1234'

my_list = [int(num) for num in my_number]
print(my_list)