from week3.Utility.Utilclass1 import Util


class Addition(Util) :
    obj = Util()

    def __init__(self) :
        super(Addition, self).__init__()

    def display_matrix(self):
        result = obj.addition_matrix(self.first_matrix, self.second_matrix)
        print('addition matrix')
        for value in result :
            print(value)


obj = Addition()
obj.display_matrix()
