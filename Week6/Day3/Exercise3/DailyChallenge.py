import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.cards = []
        self.shuffle()

    def shuffle(self):
        """Recreates a full deck of 52 cards and randomly shuffles them."""
        self.cards = [Card(suit, value) for suit in self.SUITS for value in self.VALUES]
        random.shuffle(self.cards)

    def deal(self):
        """Removes and returns a single card from the top of the deck."""
        if len(self.cards) == 0:
            print("No cards left in the deck to deal!")
            return None
        return self.cards.pop()