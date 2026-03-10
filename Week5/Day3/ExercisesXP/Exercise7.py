from faker import Faker

fake = Faker()
users = []

def add_users(count):
    for _ in range(count):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        
        users.append(user)

add_users(5)

for u in users:
    print(u)
