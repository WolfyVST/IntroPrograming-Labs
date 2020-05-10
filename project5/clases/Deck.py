import random
class Deck:
    wholedeck = []

    def __init__(self, wholedeck):
        self.wholedeck = wholedeck

    def Shuffle(self):
        random.shuffle(self.wholedeck)

    def draw(self, item):
        dimension = len(self.wholedeck)
        i = item
        while i < dimension:
                if i == item:
                    print(self.wholedeck[i].getSuit() + self.wholedeck[i].getRank())
                    break

