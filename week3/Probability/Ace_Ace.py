"""3. Write a program to find the probability of drawing an ace after drawing an ace on the first draw"""

from week3.Utility.Utility_probability import Util


class Ace_from_Ace(Util):
    obj = Util()

    def __init__(self):
        self.Ace = 4
        self.new_Ace = self.Ace - 1
        self.cards = 52
        self.new_cards = self.cards - 1

    def AceProbability(self):
        result = obj.ace_ace(self.new_cards, self.new_Ace)
        print("\ndrawing an ace after drawing an ace", result)


obj = Ace_from_Ace()
obj.AceProbability()
