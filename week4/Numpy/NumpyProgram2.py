from week4.Numpy.Utility.Numpy_utility import Util


class Array:
    obj = Util()

    def numpy_program(self):
        self.obj = Util()

    flag = True
    print("11.program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements.")
    print("12.program to find common values between two arrays.")
    print("13.To find the set difference of two arrays and return the sorted, unique values in array1 that are not in array2")
    print("14.To find the set exclusive-or of two arrays.")
    print("15.To compare two array using numpy")
    print("16.program to create a contiguous flattened array.")
    print("17.To change the data type of an array.")
    print("18.To create a 3-D array with ones on a diagonal and zeros")
    print("19.To create an array which looks like below array.")
    print("20.To concatenate two 2-dimensional array")
    print("21.To make an array immutable (read-only).")
    print("22.To create an array of (3, 4) shape, multiply every element value by 3 and display the new array.")
    print("23.To convert a NumPy array into Python list structure.")
    print("24.To convert a NumPy array into Python list structure.")
    print("25.To suppresses the use of scientific notation for small numbers in numpy array.")
    print("26.To how to add an extra column to an numpy array.")
    print("27.To remove specific elements in a numpy array.")
    print("0. Exit")
    while flag:

        try:

            print("_____________________________________________________")
            choice = int(input("Enter your choice"))

            if choice == 0:
                flag = False

            elif choice == 11:
                obj.element_size()

            elif choice == 12:
                print("common values in array:", obj.common_value())

            elif choice == 13:
                print("set difference:", obj.set_difference())

            elif choice == 14:
                print("set Exclusive-or value:", obj.set_Exclusive_or())

            elif choice == 15:
                obj.compare_Array()

            elif choice == 16:
                print("New contiguous flattened array", obj.contiguous_Array())

            elif choice == 17:
                print("Changed data type\n", obj.change_dataType())

            elif choice == 18:
                print("3D- array:\n", obj.create_3Darray())

            elif choice == 19:
                print("array:\n", obj.array_structure())

            elif choice == 20:
                print("concatenate 2D- Array:\n", obj.concatenate_Array())

            elif choice == 21:
                print("immutable array:\n", obj.immutable_array())

            elif choice == 22:

                print("array (3, 4) shape, multiply value by 3 and display new array\n", obj.array_manipulation())

            elif choice == 23:
                print("list structure:\n", obj.array_to_list())

            elif choice == 24:
                print("list structure:\n", obj.array_to_list())

            elif choice == 25:
                print("supress the array:\n", obj.suprees_array())

            elif choice == 26:
                print("New Array:\n", obj.add_column())

            elif choice == 27:
                print("remove_element:\n", obj.remove_element())

            else:
                print("enter valid choice")

        except Exception as e:
            print(e)
