"""4.You toss a fair coin three times write a program to find following:
    1.What is the probability of three heads, HHH?
    2.What is the probability that you observe exactly one heads?
    3.Given that you have observed at least one heads, what is the probability that you observe at least two heads?"""

"""    1.What is the probability of three heads, HHH? """
from week3.Utility.Utility_probability import Util

obj = Util()


class Toss_coin(Util) :
    def __init__(self) :
        self.Probabilities = [ 'HHH', 'HHT', 'HTH', 'THH', 'HTT', 'THT', 'TTH', 'TTT' ]
        print("\n All Probability", self.Probabilities)
        self.len_Probabilities = len(self.Probabilities)
        print("\n length of Probability: ", self.len_Probabilities)

    def display(self) :
        HHH_Probabilities = self.Probabilities.count('HHH')
        print("\n count of HHH Probabilities :", HHH_Probabilities)
        result = obj.count_probHHH(self.len_Probabilities, HHH_Probabilities)
        print("\n probability of three heads : ", result)
        print("_______________________________________________")


obj = Toss_coin()
obj.display()

"""2.What is the probability that you observe exactly one heads?"""


class Exactly_OneHead(Toss_coin) :

    def __init__(self) :
        super(Exactly_OneHead, self).__init__()

    def one_Head(self) :

        list = [ ]
        for temp in self.Probabilities :
            count = 0
            for char in temp :
                if char == 'H' :
                    count += 1
            if count == 1 :
                list.append(temp)
        length_OneHead = len(list)

        print("\n one Head ", length_OneHead)
        print("\n probability of exactly one heads", obj.One_HHH(self.len_Probabilities, length_OneHead))
        print("____________________________________________________")


obj = Exactly_OneHead()
obj.one_Head()

"""3.Given that you have observed at least one heads, what is the probability that you observe at least two heads?"""


class Least_head(Toss_coin):

    def __init__(self):
        super(Least_head, self).__init__()

    def display(self):
        at_least_one = obj.at_least_one(self.Probabilities, self.len_Probabilities)
        at_least_two = obj.at_least_two(self.Probabilities, self.len_Probabilities)
        result = at_least_two / at_least_one
        print("\n probability at least two heads", result)


obj = Least_head()
obj.display()
