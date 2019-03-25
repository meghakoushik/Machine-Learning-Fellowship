"""5. Write a program to find inverse matrix of matrix X in problem 1 """


class Matrix:

    def __set__(self, matrix_value):
        self.main_matrix = matrix_value

    def __get__(self):
        return self.main_matrix

    # Function to print matrix
    def print_Matrix(self, matrix_value):
        print(" the matrix is:")
        for item in matrix_value:
            print(item)

    # calculate the co factors of the elements of specific row and column
    def cofactors(self, row, column, matrix_value):
        list1 = list()
        for row_one in range(0, len(matrix_value[row])):
            for column_one in range(0, len(matrix_value[row])):
                # eliminating the current row and column and entering rest to the list
                if row_one != row and column_one != column:
                    list1.append(matrix_value[row_one][column_one])
        counter = 0
        # multiplying the cross elements that is first and last element in the list
        item = (list1[counter] * list1[-(counter + 1)])
        counter += 1
        # subtracting the multiplication of the rest 2 values from the previous one calculated
        item = item - (list1[counter] * list1[-(counter + 1)])
        return item

    # returns the transpose of any matrix
    def transpose_Matrix(self, matrix_value) :
        print("transpose matrix")
        # new matrix will be calculated by exchanging the elements of previous matrix
        transpose_adj_matrix = [[matrix_value[row][col] for row in range(0, len(matrix_value[0]))] for col in
                                range(0, len(matrix_value))]
        return transpose_adj_matrix

    def calculate_adjoint(self, matrix_value):
        adjoint_matrix = []
        for row in range(0, len(matrix_value[0])):
            list1 = list()
            for col in range(0, len(matrix_value)):
                # adding each element returned by co factor method in list
                list1.append(self.cofactors(row, col, matrix_value))
            # the list contains the co factors of each row so appends for each row
            adjoint_matrix.append(list1)
        temp = -1
        # Here we'll multiply each elements by +-+ signs respectively
        for row in range(0, matrix_value.__len__()):
            for col in range(0, matrix_value[row].__len__()):
                temp *= -1
                adjoint_matrix[row][col] *= temp

        return adjoint_matrix

    def calculate_determinant(self, matrix_value):
        temp = -1
        item = 0
        for col in range(0, len(matrix_value)):
            cofactor = self.cofactors(0, col, matrix_value)
            # as we need to add first subtract second and add third that is + - + hence multiplying with -1
            temp *= -1
            item += temp * (matrix_value[0][col] * cofactor)
            # print("col is", col, ', element taken is ', matrix_passed[0][col], 'and co factor is ', co factor)
        return item

    def matrix_multiply(self, matrix_one, matrix_two):
        matrix_three = [[0, 0, 0]] * 3

        for row in range(0, matrix_one[0].__len__()):
            for col in range(0, len(matrix_two)):
                for count in range(0, matrix_two[0].__len__()):
                    matrix_three[row][col] += matrix_one[row][count] * matrix_two[count][col]
        print("multiplication is")
        self.print_Matrix(matrix_three)

    def inverse_Matrix(self, ):
        original_matrix = [[1, 3, 7],
                   [4, 2, 3],
                   [1, 2, 1]]
        self.print_Matrix(original_matrix)
        adjoint_matrix = self.calculate_adjoint(original_matrix)
        adjoint_matrix = self.transpose_Matrix(adjoint_matrix)
        determinant = self.calculate_determinant(original_matrix)
        print("determinant is ", determinant, " and inverse matrix is ")
        inverse_matrix = [[adjoint_matrix[row][col] / determinant for col in range(0, len(original_matrix[row]))] for row in range(0, len(original_matrix)) ]
        self.print_Matrix(inverse_matrix)
        print("or \n 1/", determinant, 'x')
        self.print_Matrix(adjoint_matrix)
        print("checking if inverse is right")
        self.matrix_multiply(original_matrix, inverse_matrix)


try :
    matrix_object = Matrix()
    flag: bool = True
    while flag:
        matrix_object.inverse_Matrix()
        print("To exit press 0 ")
        if input() == 0:
            flag = False
except Exception as e:
    print("Process stopped because %s" % e)
