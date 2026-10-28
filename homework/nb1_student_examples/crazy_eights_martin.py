import random

suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
faces = ["Jack", "Queen", "King", "Ace"]
numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10]

suit = random.choice(suits)
card = random.choice(faces + numbered)
print("card in play is:", card, "of", suit)

player_suit = random.choice(suits)
player_card = random.choice(faces + numbered)
print("Your card:", player_card, "of", player_suit)

if card == player_card or suit == player_suit:
    print("You can discard your card.")
else:
    print("You can't discard your card.")