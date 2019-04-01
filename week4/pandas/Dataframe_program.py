from week4.pandas.Utility.utility import Util


class Pandas_Programs:
    def __init__(self):
        self.obj = Util()

    def panda(self):
        flag = True
        print("1. display a one-dimensional array-like object containing an array of data using Pandas module.. ")
        print("2. convert a Panda module Series to Python list and it's type. ")
        print("3. Python program to add, subtract, multiple and divide two Pandas Series.")
        print("4. program to get the powers of an array values element-wise")
        print("5. display a DataFrame from a specified dictionary data which has the index labels")
        print("6. display a summary of the basic information about a specified Data Frame and its data ")
        print("7. get the first 3 rows of a given DataFrame. Sample Python dictionary  data and list labels")
        print("8. Write a Python program to select the 'name' and 'score' columns from the following DataFrame.")
        print("9.  Write a Python program to select the specified columns and rows from a given data frame.")
        print("10. select the rows where the number of attempts in the examination is greater than 2.")
        print("0. EXIT")
        while flag:
            try:

                print("_____________________________________________________")
                choice = int(input("Enter your choice"))

                if choice == 0:
                    flag = False

                elif choice == 1:
                    print("display one- dimensional array:", self.obj.create_series())

                elif choice == 2:
                    print("converted series:\n", self.obj.convert())

                elif choice == 3:
                    value1 = int(input("enter 1 st elements"))
                    num1 = int(value1)
                    value2 = int(input("enter 2nd elements"))
                    num2 = int(value2)
                    self.obj.operation_on_series(num1, num2)

                elif choice == 4:
                    print("powers of an array element :\n", self.obj.get_power())

                elif choice == 5:
                    print("display Dataframe:", self.obj.data_frame())

                elif choice == 6:
                    print("display the basic information:", self.obj.basic_information())

                elif choice == 7:
                    print("display the dataframe:\n", self.obj.display_dataframe())

                elif choice == 8:
                    print("row , column array:\n", self.obj.row_column())

                elif choice == 9:
                    print("row_columns dataframe:\n\n", self.obj.row_column_dataframe())

                elif choice == 10:
                    print("rows attempts:\n", self.obj.set_attempts())

                else:
                    print("enter valid choice")

            except Exception as e:
                print(e)


obj1 = Pandas_Programs()
obj1.panda()
