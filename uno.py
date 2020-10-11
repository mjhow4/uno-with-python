import random

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS = ["🟦","🟩", "🟥", "🟨"]


class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color


    def ___str___(self):
        return f"{self.color} {self.number}"


class Player:
    def __init__(self, name):
        self.name = input('Enter your name: ')


class Deck:

    def __init__(self, numbers, colors):
        self.cards = []
        for number in numbers:
            for color in colors:
                card = (color + ' ' + str(number))
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
        return str(self.cards)
    
    def deal(self):
        player1 = []
        player2 = []
        self.shuffle()
        i = 0
        while i < 7:
            a = self.cards.pop()
            player1.append(a)
            b = self.cards.pop()
            player2.append(b)
            i += 1
        print("Player 1 Hand: ", player1)
        print("Player 2 Hand: ", player2)
        print(i)

Player()
deck1 = Deck(NUMBERS, COLORS)
# a = deck1.cards.pop()
# print(a)

# print(deck1.shuffle())

print(deck1.deal())

