# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
winter = [12, 1, 2]

user_month = int(input("Please enter a month (1-12): "))

if user_month in spring:
    print("It's Spring!")
if user_month in summer:
    print("It's Summer!")
if user_month in autumn:
    print("It's Autumn!")
if user_month in winter:
    print("It's Winter!")

else:
    print(user_month = int(input("Please enter a month (1-12): ")))





