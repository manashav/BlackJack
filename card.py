import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def getValue(self) -> int:
        if isinstance(self.rank, int):
            return self.rank
        elif self.rank == 'A':
            return 1
        elif self.rank in "KQJ":
            return 10
        else:
            raise ValueError(f"Invalid rank: {self.rank}")
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J']
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self, playerName):
        self.cards = []
        self.value = 0
        self.name = playerName
    
    def getValue(self):
        return self.value
    
    def addCard(self, card):
        self.cards.append(card)
        self.value += card.getValue()
    
    def __str__(self):
        c = '\n'.join(str(card) for card in self.cards)
        return f"{self.name}'s Hand:\n{c}\nTotal Value: {self.value}"

        