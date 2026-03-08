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