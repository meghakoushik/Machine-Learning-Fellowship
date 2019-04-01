import numpy as np


class Util:
    """1. program to convert a list of numeric value to array"""

    def list_to_array(self, list_value):
        array_list = np.array(list_value)
        return array_list

    """----------------------------------------------------------------------------------"""
    """2.Create a 3x3 matrix with values ranging from 2 to 10."""

    def create_matrix(self):
        matrix_Arrange = np.arange(2, 11).reshape(3, 3)
        return matrix_Arrange

    """----------------------------------------------------------------------------------"""
    """3.program to create a null vector of size 10 and update sixth value to 11."""

    def null_vector(self):
        vector_value = np.zeros(10)
        print("vector values:", vector_value)
        print("update sixth value:")
        vector_value[6] = 11
        return vector_value

    """----------------------------------------------------------------------------------"""
    """4. program to reverse an array (first element becomes last"""

    def reverse_Array(self):
        value_one = np.arange(12, 38)
        print("original array:", value_one)
        value_one = value_one[::-1]
        return value_one

    """----------------------------------------------------------------------------------"""
    """5. program to create a 2d array with 1 on the border and 0 inside."""

    def array_border(self):
        values = np.ones((5, 5))
        print("original array:", values)
        values[1:-1, 1:-1] = 0
        return values

    def ones_border(self):
        values = np.ones((5, 5))
        print("original array:", values)
        values[-1:1, -1:1] = 0
        return values

    """----------------------------------------------------------------------------------"""
    """6. program to add a border (filled with 0's) around an existing array"""

    def zero_Border(self):
        values = np.ones((3, 3))
        print("original array:", values)
        values = np.pad(values, pad_width=1, mode='constant', constant_values=0)
        return values

    """----------------------------------------------------------------------------------"""
    """7.program to create a 8x8 matrix and fill it with a checkerboard pattern"""

    def check_board(self):
        values = np.zeros((8, 8), dtype=int)
        values[1::2, 0::2] = 1
        values[0::2, 1::2] = 1
        return values

    """----------------------------------------------------------------------------------"""
    """8.program to convert a list and tuple into arrays."""

    def array_list(self):
        list_value = [2, 12, 4, 5, 6]
        result = np.asarray(list_value)
        return result

    def array_tuple(self):
        tuple_value = ([2, 3, 7], [5, 6, 7])
        result = np.asarray(tuple_value)
        return result

    """----------------------------------------------------------------------------------"""
    """9.program to append values to the end of an array"""

    def append(self):
        list_value = [2, 3, 4]
        print("original list", list_value)

        list_value = np.append(list_value, [[3, 5, 6], [5, 7, 8]])
        return list_value

    """----------------------------------------------------------------------------------"""
    """10. program to find the real and imaginary parts of an array of complex numbers"""

    def complex(self):
        value_one = np.sqrt([.00000000 + 0.70710678 + 0.70710678j])
        value_two = np.sqrt([1.00000000 + 0.70710678 + 0.70710678j])
        print("original value_ one:", value_one)
        print("original value_two:", value_two)
        print("value one real value:", value_one.real)
        print("value one imaginary value:", value_one.imag)
        print("value two real value:", value_two.real)
        print("value two imaginary value:", value_two.imag)

    """--------------------------------------------------------------------------------------"""

    """11.find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements."""

    def element_size(self):
        elements = np.array([1, 2, 3], dtype=np.float64)
        print("size o fan array:", elements.size)
        print("Length of one array element in bytes:", elements.itemsize)
        print("Total bytes of an elements of the array:", elements.nbyte)

    """-------------------------------------------------------------------------------------------"""
    """"12.program to find common values between two arrays."""

    def common_value(self):
        Array__one = np.array([1, 23, 3, 56, 7])
        print(Array__one)
        Array_two = np.array([1, 8, 27, 56, 3])
        print(Array_two)
        result = np.intersect1d(Array__one, Array_two)
        return result

    """-----------------------------------------------------------------------------------------------"""
    """13.To find the set difference of two arrays """

    def set_difference(self):
        Array__one = np.array([1, 23, 3, 56, 7])
        print("Array 1", Array__one)
        Array_two = np.array([1, 8, 27, 56, 3])
        print("Array 2", Array_two)
        result = np.setdiff1d(Array__one, Array_two)
        return result

    """------------------------------------------------------------------------------------------------------"""
    """14. Find the set exclusive-or of two arrays """

    def set_Exclusive_or(self):
        Array__one = np.array([1, 23, 3, 56, 7])
        print("Array 1", Array__one)
        Array_two = np.array([1, 8, 27, 56, 3])
        print("Array 2", Array_two)

        result = np.setxor1d(Array__one, Array_two)
        return result

    """------------------------------------------------------------------------------------------------------------"""
    """15.To compare two array using numpy """

    def compare_Array(self):
        Array__one = np.array([1, 2])
        print("Array 1", Array__one)
        Array_two = np.array([4, 5])
        print("Array 2", Array_two)
        result_one = np.greater(Array__one, Array_two)
        print(result_one)
        result_two = np.greater_equal(Array__one, Array_two)
        print(result_two)
        result_one = np.less(Array__one, Array_two)
        print(result_one)
        result_two = np.less_equal(Array__one, Array_two)
        print(result_two)

    """------------------------------------------------------------------------------------------------"""
    """16. program to create a contiguous flattened array."""

    def contiguous_Array(self):
        value = np.array([[1, 2, 9], [3, 4, 5]])
        print("original Array:\n", value)
        result = np.ravel(value)
        return result

    """------------------------------------------------------------------------------------------------"""
    """17.To change the data type of an array"""

    def change_dataType(self):
        array_list = np.array([[2, 3, 4], [4, 5, 7]], np.int32)
        print("original array\n", array_list)
        print("type:", array_list.dtype)
        result = array_list.astype(float)
        return result

    """----------------------------------------------------------------------------------------------------"""
    """18.To create a 3-D array with ones on a diagonal and zeros """

    def create_3Darray(self):
        Array_value = np.eye(3)
        return Array_value

    """------------------------------------------------------------------------------------------------"""
    """19. To create an array which looks like below array"""

    def array_structure(self):
        array_format = np.tri(4, 3, -1)
        return array_format

    """------------------------------------------------------------------------------------------------"""
    """20.To concatenate two 2-dimensional array """

    def concatenate_Array(self):
        array_one = np.array([[1, 2, 4], [4, 6, 7]])
        print(array_one)
        array_two = np.array([ [ 1, 3, 5 ], [ 4, 5, 6 ] ])
        print(array_two)
        result = np.concatenate((array_one, array_two), 1)
        return result

    """-------------------------------------------------------------------------------------------------"""
    """21.To make an array immutable (read-only)."""

    def immutable_array(self):
        read_array = np.arange(10)
        read_array.flags.writeable = False
        read_array[0] = 1

    """-------------------------------------------------------------------------------------------------"""
    """22.To create an array of (3, 4) shape, multiply every element value by 3 and display the new array. """

    def array_manipulation(self):
        value = np.arange(12).reshape(3, 4)
        print("original value is\n", value)
        for item in np.nditer(value, op_flags=['readwrite']):
            item[...] = 3 * item
            return value

    """-------------------------------------------------------------------------------------------------"""
    """23. To convert a NumPy array into Python list structure."""

    def array_to_list(self):
        value = np.arange(6).reshape(3, 2)
        print("original array:\n", value)
        result = value.tolist()
        return result

    """-------------------------------------------------------------------------------------------------"""

    """24. To convert a NumPy array into Python list structure."""

    def suprees_array(self):
        array_value = np.array([1.6e-10, 1.6, 1200, .235])
        np.set_printoptions(suppress=True)
        return array_value

    """-------------------------------------------------------------------------------------------------"""
    """26.To how to add an extra column to an numpy array."""

    def add_column(self):
        value_one = np.array([[1, 2, 3], [4, 6, 7]])
        value_two = np.array([[333], [111]])
        return np.append(value_one, value_two, axis=1)

    """-------------------------------------------------------------------------------------------------"""
    """27.To remove specific elements in a numpy array."""

    def remove_element(self):
        array_lsit = np.array([10, 20, 30, 40, 50, 60])
        index = [2, 3, 4]
        print("original array:\n", array_lsit)
        print("remove specific element: second, third, fourth")
        return np.delete(array_lsit, index)

    """-------------------------------------------------------------------------------------------------"""
