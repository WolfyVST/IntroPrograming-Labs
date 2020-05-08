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
while flag == True:
    awsnser = input("do you want a card").lower()
    i = 0
    if awsnser == "yes":
        print(deck.draw(i))
        i = i + 1
    else:
        flag = False




#for val in completedeck:
    #print(val.getSuit()+val.getRank())
