from week4.pandas.Utility.utility import Util


class Pandas_Programs:
    def __init__(self):
        self.obj = Util()

    def panda(self):
        flag = True
        print("11. Write a Python program to count the number of rows and columns of a DataFrame.")
        print("12. Write a Python program to select the rows where the score is missing, i.e. is NaN.")
        print("13. Write a Python program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.")
        print("14.Write a Python program to change the score in row 'd' to 11.5.")
        print("15.Write a Python program to calculate the sum of the examination attempts by the students")
        print("16.Write a Python program to calculate the mean score for each different student in DataFrame.")
        print("17 append a new row 'k' to data frame with given values for each column. Now delete the new row and return the original DataFrame.")
        print("18.To sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.")
        print("19.To replace the 'qualify' column contains the values 'yes' and 'no' with True and False.")
        print("20.To delete the 'attempts' column from the DataFrame.")
        print("21.To insert a new column in existing DataFrame")
        print("22.To iterate over rows in a DataFrame.")
        print("23.Write a Python program to get list from DataFrame column headers.")
        while flag:
            try:

                print("_____________________________________________________")
                choice = int(input("Enter your choice"))

                if choice == 0:
                    flag = False

                elif choice == 11:
                    self.obj.count_row_column()

                elif choice == 12:
                    print("rows where score is missing:\n\n", self.obj.missing_score())

                elif choice == 13:
                    print("no. of attempts that is less than 2 and grater than 15:\n", self.obj.attempts_greater_less() )

                elif choice == 14:
                    print("changed score is:\n", self.obj.changed_score())

                elif choice == 15:
                    print("sum of the examination attempts:\n", self.obj.sum_Of_attempts())

                elif choice == 16:
                    print("display the mean score\n", self.obj.mean_score())

                elif choice == 17:
                    print("original Dataframe is:\n", self.obj.update_row())

                elif choice == 18:
                    print("dataframe descending and ascending order:\n\n", self.obj.Desc_Asc_order())

                elif choice == 19:
                    print("Replace column with true and false:\n ", self.obj.replace_column())

                elif choice == 20:
                    print("after deleting attempts column :\n", self.obj.delete_attempts())

                elif choice == 21:
                    print("after inserting new column:\n", self.obj.insert_column())

                elif choice == 22:
                    print("After iteration row , Dataframe:\n", self.obj.iterated_row())

                elif choice == 23:
                    print("Display list from DataFrame column headers:\n", self.obj.column_header())

                else:
                    print("enter valid choice")
            except Exception as e:
                print(e)


obj = Pandas_Programs()
obj.panda()