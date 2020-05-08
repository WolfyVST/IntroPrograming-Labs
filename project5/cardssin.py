from Cl
suit = ["T", "D", "H", "S"]
rank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
completedeck = []

for s in suit:
    for r in rank:
        completedeck.append(Cards.Cards(s, r))

#for val in completedeck:
    #print(val.getSuit()+val.getRank())
