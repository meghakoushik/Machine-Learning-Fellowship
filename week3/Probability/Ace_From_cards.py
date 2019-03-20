""" 1. Write a program to find probability of drawing an ace from pack of cards"""

from week3.Utility.Utility_probability import Util


class Probability(Util):
    obj = Util

    def __init__(self):
        self.ace = 4
        self.cards = 52

    def ace_Probability(self) :
        result = obj.ace_cards(self.ace, self.cards)
        print("\nProbability of ace from deck of cards:", result)


obj = Probability()
obj.ace_Probability()
