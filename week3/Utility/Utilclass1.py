class Util :
    def __init__(self) :

        self.first_matrix = [ [ 12, 7, 3 ],
                              [ 4, 5, 6 ],
                              [ 7, 8, 9 ] ]

        self.second_matrix = [ [ 5, 8, 1 ],
                               [ 6, 7, 3 ],
                               [ 4, 5, 9 ] ]

    def matrix1(self) :
        print("first matrix:")
        for value in self.first_matrix :
            print(value)

    def matrix2(self) :
        print("second matrix:")
        for value in self.second_matrix :
            print(value)

    # for addition:

    def addition_matrix(self, first_matrix, second_matrix) :
        result = [ [ first_matrix[ row ][ column ] + second_matrix[ row ][ column ] for column in
                     range(len(first_matrix[ 0 ])) ]
                   for row in range(len(first_matrix)) ]
        return result

    def scalar_Matrix(self, first_matrix, scalar_value) :
        print("\n scalar multiplication of matrix:")
        for row in range(len(first_matrix)) :

            for column in range(len(first_matrix[ 0 ])) :
                first_matrix[ row ][ column ] = first_matrix[ row ][ column ] * scalar_value
        for value in first_matrix :
            print(value)

    def vector_multiplication(self, matrix_first, vector_first) :
        first = len(matrix_first)
        second = len(vector_first)
        list_new = [ 0 ] * first
        sum1 = 0
        for value_2 in range(first) :
            row1 = matrix_first[ value_2 ]
        for value_1 in range(second) :
            sum1 += sum(row1[ value_1 ] * vector_first[ value_1 ])
        list_new[ value_2 ] = sum1
        return list_new

    def transpose_matrix(self, first_matrix) :
        result = [ [ first_matrix[ column ][ row ] for column in range(len(first_matrix)) ] for row in
                   range(len(first_matrix[ 0 ])) ]
        return result

    def multiply_matrix(self, first_matrix, second_matrix, result) :
        for row in range(len(first_matrix)) :
            for column in range(len(first_matrix[ 0 ])) :
                result[ row ][ column ] += first_matrix[ row ][ column ] * second_matrix[ row ][ column ]
        return result
