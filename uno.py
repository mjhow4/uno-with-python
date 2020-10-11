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
        p1_hand = []
        p2_hand = []
        self.shuffle()
        i = 0
        while i < 7:
            a = self.cards.pop()
            p1_hand.append(a)
            b = self.cards.pop()
            p2_hand.append(b)
            i += 1
        print("Player 1 Hand: ", p1_hand)
        print("Player 2 Hand: ", p2_hand)
        #comment len out later
        print(len(self.cards))
        a = self.cards
        # print(a)
        print("Let's Begin!")
        first_card = a.pop()
        print("The first card from the deck is:", first_card)
        used_deck = []
        used_deck.append(first_card)
        print("Player 1, you go first.")
        i = 0
        for card in p1_hand:
            if card[0] == first_card[0] or card[2] == first_card[2]:
                i += 1
            else:
                i += 0
        if i > 0:
                player1_card = int(input("Please select a card to play (by number from left to right start at 0): "))
                while True:
                    if p1_hand[player1_card][0] == first_card[0] or p1_hand[player1_card][2] == first_card[2]:
                        print("Great Choice.")
                        p1_card = p1_hand[player1_card]
                        p1_hand.remove(p1_card)
                        used_deck.append(p1_card)
                        newtoppilecard = p1_card
                        print(p1_card)
                        print(p1_hand)
                        print(newtoppilecard)
                        break
                    else:
                        print("Please select another card.")
                        player1_card = int(input("Please select a card to play (by number from left to right start at 0): "))
        else:
            print("Please pluck a card from the deck.")
        # return p1_hand
        # return p2_hand
        # return a


# deck1 = Deck(NUMBERS, COLORS)
# # a = deck1.cards.pop()
# # print(a)

# # print(deck1.shuffle())

# print(deck1.deal())

def play_game():
    print("Welcome to Uno!")
    player1 = input("Player 1 please enter your name: ")
    Player(player1)
    print("Player 1 is: ", player1.title())
    player2 = input("Player 2 please enter your name: ")
    Player(player2)
    print("Player 2 is: ", player2.title())
    print("Let's Shuffle Up and Play!")
    deck = Deck(NUMBERS, COLORS)
    deck.deal()
play_game()