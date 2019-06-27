"""2. Write a program to perform scalar multiplication of matrix and a number."""

from week3.Utility.Utilclass1 import Util


# parent class
class Matrix_scalar:
    obj = Util()

    # constructor
    def __init__(self):
        self.first_matrix = ([ 1, 2, 3 ],
                             [ 4, 5, 6 ],
                             [ 7, 8, 9 ])

        self.scalar_value = 4

    # function for display matrix
    def matrix_display(self):
        print("matrix")
        for value in self.first_matrix :
            print(value)


# object of class
obj = Matrix_scalar()

# call method
obj.matrix_display()


class Scalar_Multiplication(Matrix_scalar):

    # constructor for subclass
    def __init__(self):
        super(Scalar_Multiplication, self).__init__()

    def calculate(self):

        try:
            scalar_multiply = self.obj.scalar_Matrix(self.first_matrix, self.scalar_value)

        except TypeError:
            for value in scalar_multiply:
                print(value)


obj = Scalar_Multiplication()
obj.calculate()
