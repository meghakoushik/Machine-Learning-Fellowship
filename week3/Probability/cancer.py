"""6. Given the following statistics, write a program to find the probability that a woman has
cancer if she has a positive mammogram result?
a. One percent of women over 50 have breast cancer.
b. Ninety percent of women who have breast cancer test positive on
mammograms.
c. Eight percent of women will have false positives."""

from week3.Utility.Utility_probability import Util


class Cancer(Util):
    obj = Util()

    def __init__(self):
        self.cancer = 0.01
        self.no_cancer = 0.99
        self.test_positive = 0.9
        self.false_positive = 0.08

    def Probability(self):
        result = obj.mammogram_result(self.cancer, self.no_cancer, self.test_positive, self.false_positive)
        print("Probability of women has cancer, if she has positive mammogram result:\n", result)


# create a class object
obj = Cancer()
obj.Probability()
