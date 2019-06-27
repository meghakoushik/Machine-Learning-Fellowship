"""4. Write a program to multiply matrices in problem 1"""
from week3.Utility.Utilclass1 import Util


class Multiplication(Util):
    obj = Util()

    # constructor for subclass
    def __init__(self):
        super(Multiplication, self).__init__()

        self.result = ([ 0, 0, 0 ],
                       [ 0, 0, 0 ],
                       [ 0, 0, 0 ])

    def display(self) :
        result = obj.multiply_matrix(self.first_matrix, self.first_matrix, self.result)
        print("\n Vector Multiplication:", )
        for value in result:
            print(value)


obj = Multiplication()

# call method
obj.display()
