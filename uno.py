import random

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS = ["🟦","🟩","🟨","🟥"]


class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def ___str___(self):
        return f"{self.color} {self.number}"

# card1 = Card(NUMBERS[2], COLORS[0])
# print(card1.___str___())

# card2 = Card(NUMBERS[4], COLORS[1])
# print(card2.___str___())

# card3 = Card(NUMBERS[6], COLORS[2])
# print(card3.___str___())

# card4 = Card(NUMBERS[8], COLORS[3])
# print(card4.___str___())


class Deck:

    def __init__(self, numbers, colors):
        self.cards = []
        for number in numbers:
            for color in colors:
                card = (color + ' ' + str(number))
                self.cards.append(card)


deck1 = Deck(NUMBERS, COLORS)
print(deck1.cards)