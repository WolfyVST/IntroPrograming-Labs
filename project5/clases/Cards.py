class Cards:
    suit = ""
    rank = ""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def getSuit (self):
        return self.suit

    def getRank (self):
        return self.rank
