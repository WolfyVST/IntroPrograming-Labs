from clases import Cards
from clases import Deck
suit = ["T", "D", "H", "S"]
rank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
completedeck = []

for s in suit:
    for r in rank:
        completedeck.append(Cards.Cards(s, r))
deck = Deck.Deck(completedeck)
deck.Shuffle()
flag = True
i = 0

while flag is True:
    awsnser = input("do you want a card: ").lower()
    if awsnser == "yes":
        deck.draw(i)
        i = i + 1
    else:
        flag = False