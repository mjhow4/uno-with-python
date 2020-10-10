import random

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS = ["🔵","🟢","🟡","🔴"]


class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def ___str___(self):
        return f"{self.color} {self.number}"

card1 = Card(NUMBERS[0], COLORS[2])
print(card1.___str___())