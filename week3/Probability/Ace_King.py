"""2 Write a program to find the probability of drawing an ace after drawing a king on the first draw"""

from week3.Utility.Utility_probability import Util


class Ace_From_King(Util):
    obj = Util

    def __init__(self):
        self.king = 4
        self.cards = 52
        self.new_cards = self.cards - 1

    def Ace_probability(self):
        result = obj.ace_king(self.king, self.new_cards)
        print("\ndrawing an ace after drawing a king", result)


obj = Ace_From_King()
obj.Ace_probability()
