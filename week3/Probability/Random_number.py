"""12.  Write a program to find the probability of getting a random number from the interval [2, 7]"""
import random


class Random_number:

    def __init__(self):
        self.interval_difference = 6
        self.get_Random_number = 1

    def for_random_number(self):
        num = random.randint(2, 7)
        print("random number is ", num)
        return num

    def display(self, num1):
        result = num1 / self.interval_difference
        print("probability of getting a random number", result)


obj = Random_number()
num = obj.for_random_number()
obj.display(num)
