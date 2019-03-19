#  Write a program to find inverse matrix of matrix X in problem 1


from week3.Utility.Utilclass1 import Util


class Transpose(Util):

    def __init__(self):
        super(Transpose, self).__init__()

    # function for transpose
    def display(self):
        result = obj.transpose_matrix(self.first_matrix)
        print("transpose matrix:")
        for value in result:
            print(value)


obj = Util()

# object of subclass
obj = Transpose()

# call method
obj.display()
