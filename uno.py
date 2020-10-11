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
        self.name = name


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
        player1_hand = []
        player2_hand = []
        self.shuffle()
        i = 0
        while i < 7:
            a = self.cards.pop()
            player1_hand.append(a)
            b = self.cards.pop()
            player2_hand.append(b)
            i += 1
        print("Player 1 Hand: ", player1_hand)
        print("Player 2 Hand: ", player2_hand)
        print(len(self.cards))


# deck1 = Deck(NUMBERS, COLORS)
# # a = deck1.cards.pop()
# # print(a)

# # print(deck1.shuffle())

# print(deck1.deal())

def play_game():
    print("Welcome to Uno!")
    player1 = input("Player 1 please enter hyour name: ")
    Player(player1)
    print("Player 1 is: ", player1.title())
    player2 = input("Player 2 please enter hyour name: ")
    Player(player2)
    print("Player 2 is: ", player2.title())
    print("Let's Shuffle Up and Play!")
    deck = Deck(NUMBERS, COLORS)
    deck.deal()
play_game()