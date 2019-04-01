from week4.Numpy.Utility.Numpy_utility import Util


class Array:
    obj = Util()

    def numpy_program(self):
        self.obj = Util()

    flag = True
    print("1. program to convert a list of numeric value to array")
    print("2. Create a 3x3 matrix with values ranging from 2 to 10.")
    print("3. program to create a null vector of size 10 and update sixth value to 11. ")
    print("4. program to reverse an array (first element becomes last.")
    print("5. program to create a 2d array with 1 on the border and 0 inside.")
    print("6. program to add a border (filled with 0's) around an existing array.")
    print("7. program to create a 8x8 matrix and fill it with a checkerboard pattern")
    print("8. program to convert a list and tuple into arrays")
    print("9. program to append values to the end of an array ")
    print("10. program to find the real and imaginary parts of an array of complex numbers.")
    print("0. Exit")
    while flag:

        try:

            print("_____________________________________________________")
            choice = int(input("Enter your choice"))

            if choice == 0:
                flag = False

            elif choice == 1:
                list = [12.23, 13.32, 100, 36.32]
                print("convert a list value to one-dimensional array:\n", obj.list_to_array(list))

            elif choice == 2:
                print("3x3 matrix with range from 2 to 10:\n", obj.create_matrix())

            elif choice == 3:
                print("null vector :", obj.null_vector())

            elif choice == 4:
                print("reverse Array is:", obj.reverse_Array())

            elif choice == 5:
                print("array with 1's in border and 0 inside:\n", obj.ones_border())

            elif choice == 6:
                print("array with 0's in border and 1 inside\n", obj.zero_Border())

            elif choice == 7:
                print(" 8x8 matrix checkerboard pattern\n ", obj.check_board())

            elif choice == 8:
                print("array of list\n", obj.array_list())
                print("array of tuple\n", obj.array_tuple())

            elif choice == 9:
                print("append values to the end of an array:", obj.append())

            elif choice == 10:
                obj.complex()
            else:
                print("enter valid choice ")
        except Exception as e:
            print(e)


obj = Array()
obj.numpy_program()
