# Exercise 1: Cats

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

all_cats = [
    Bengal('Brad', 5),
    Chartreux('Chippy', 7),
    Siamese('Sprint', 11)
]

sara_pets = Pets(all_cats)

sara_pets.walk()

# Exercise 2: Dogs
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        
        if self_power > other_power:
            return f"{self.name} won the fight!"
        elif other_power > self_power:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a draw!"
dog1 = Dog('Apple', 7, 15)
dog2 = Dog('Ginger', 3, 20)
dog3 = Dog('Monroe', 12, 10)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

# Exercise 3: Dogs Domesticated

import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join(args)
        print(f"{dog_names} and {self.name} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet!")

my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()


# Exercise 4: Family and Person Classes

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)
        print(f"Congratulations! {first_name} {self.last_name} was added to the family.")

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No family member named {first_name} found.")

    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        for member in self.members:
            print(f"Name: {member.first_name}, Age: {member.age}")

my_family = Family("Hirsch")
my_family.born("Kipling", 8)
my_family.born("Caraway", 11)

my_family.family_presentation()
my_family.check_majority("Kipling")
my_family.check_majority("Caraway")

