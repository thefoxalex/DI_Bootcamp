# Check what is the type of each value, then change it: if it is a string, make it an integer and vice-versa:
# bank_balance = '33000'
# phone_number = 532287514

bank_balance = '33000'
phone_number = 532287514

print(type(bank_balance))
print(type(phone_number))

bank_balance = int(bank_balance)
phone_number = str(phone_number)

print(type(bank_balance))
print(type(phone_number))

print(bank_balance, phone_number)
