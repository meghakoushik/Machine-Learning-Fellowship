"""3. Write a program to perform multiplication of given matrix and vector"""

from week3.Utility.Utilclass1 import Util


class Matrix:

    # constructor
    def __init__(self):
        self.matrix_first = ([5, 1, 3],
                            [1, 1, 1],
                            [1, 2, 1])

        self.vector_first = [[1], [2], [3]]

    # function for display matrix
    def matrix(self):
        print("Matrix:")
        for value in self.matrix_first:
            print(value)
        print("\nmatrix:")
        for value2 in self.vector_first:
            print(value2)

    def display(self):
        print("\n Vector Multiplication:", obj1.vector_multiplication(self.matrix_first, self.vector_first))


obj1 = Util()

# object of class
obj = Matrix()
obj.matrix()
obj.display()