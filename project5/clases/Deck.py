import random
class Deck:
    wholedeck = []

    def __init__(self,wholedeck ):
        self.wholedeck = wholedeck
    def Shuffle(self):
        random.shuffle(self.wholedeck)
    def draw(self, i ):
        return self.wholedeck[i]

