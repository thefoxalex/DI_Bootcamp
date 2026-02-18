# Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
    def __repr__(self):
        return f"Cat('{self.name}', {self.age})"

cats = [
    Cat('Claws', 14), 
    Cat('Caraway', 10), 
    Cat('Kipling', 8), 
    Cat('Keats', 7)
]

oldest_cat = max(cats, key=lambda self: self.age)

print(f'The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.')


# Exercise 2: Dogs

class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        x = self.height * 2
        print(f'{self.name} jumps {x} cm high!')  

    def compare(self):
        if davids_dog.height > sarahs_dog.height: 
            print(f'{davids_dog.name} is bigger than {sarahs_dog.name}')
        else:
            print(f'{davids_dog.name} is smaller than {sarahs_dog.name}')

davids_dog = Dog('Biff', 20)
sarahs_dog = Dog('Skipper', 30)


print(davids_dog.name)
print(davids_dog.height)

print(sarahs_dog.name)
print(sarahs_dog.height)

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()
davids_dog.compare()

# Exercise 3: Who's the Song Producer?

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

poker_face = Song([
    "I wanna hold 'em like they do in Texas, please",
    "Fold 'em, let 'em hit me, raise it, baby, stay with me (I love it)",
    "LoveGame intuition, play the cards with spades to start",
    "And after he's been hooked, I'll play the one that's on his heart"
])

poker_face.sing_me_a_song()

# Exercise 4: Afternoon at the Zoo

from collections import defaultdict

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        self.animals.append(new_animal)
        print(f'Added {new_animal} to the {self.zoo_name}.')
    
    def get_animals(self):
        if not self.animals:
            print(f'There are no animals in the {self.zoo_name}.')
        else:    
            print(f'Animals in {self.zoo_name}: {self.animals}')
        return self.animals
        
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f'{animal_sold} sold from {self.zoo_name}.')
        else:
            print(f'{animal_sold} not found.')
    
    def sort_animals(self):
        # Sorts animals alphabetically
        self.animals.sort()
        print(f"Animals sorted: {self.animals}")

    def get_groups(self):
        # Example grouping (e.g., by first letter)
        groups = {}
        for animal in self.animals:
            key = animal[0]
            groups.setdefault(key, []).append(animal)
        print(f"Animal groups: {groups}")
        return groups

san_diego_zoo = Zoo("San Diego Zoo")
san_diego_zoo.add_animal("Zebra")
san_diego_zoo.add_animal("Lion")
san_diego_zoo.add_animal("Elephant")
san_diego_zoo.add_animal("Llama")
san_diego_zoo.add_animal("Eagle")
san_diego_zoo.add_animal("Tiger")
san_diego_zoo.get_animals()
san_diego_zoo.sell_animal("Lion")
san_diego_zoo.get_animals()
san_diego_zoo.sort_animals()
san_diego_zoo.get_groups()


    