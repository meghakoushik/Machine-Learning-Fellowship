"""7. A bank teller serves customers standing in the queue one by one. Suppose
   that the service time XiXi for customer ii has mean EXi=2 (minutes) and Var(Xi)=1. We assume that
   service times for different bank customers are independent. Let YY be the total time the bank teller spends serving
   50 customers. Write a program to find P(90<Y<110)class Bank"""

from week3.Utility.Utility_probability import Util
import math


class Bank_Teller(Util):
    obj = Util()

    def __init__(self) :
        self.Total = 50
        self.value_one = 90
        self.Value_two = 110
        self.mean = 2
        self.deviation = 1

    # by using central limit theorem we are calculating probability
    def probability(self):
        prob_value_one = ((self.value_one - (self.Total * self.mean)) / (math.sqrt(self.Total) * self.deviation))
        print(prob_value_one)

        prob_value_two = ((self.Value_two - (self.Total * self.mean)) / (math.sqrt(self.Total) * self.deviation))
        print(prob_value_two)

        result = obj1.calculate(prob_value_one, prob_value_two)
        print(result)


# creates object of class
obj1 = Bank_Teller()
# calling method by using class object
obj1.probability()
