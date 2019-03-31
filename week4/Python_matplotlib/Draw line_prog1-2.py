from week4.Python_matplotlib.Utility.matplotlib_Utility import Util
from matplotlib import pyplot as plt


class Matplotlib_Programs:

    def __init__(self):
        self.obj = Util()

    def draw_line(self):
        flag = True
        print("1. program to draw a line with suitable label in the x axis, y axis and a title")
        print("2.to draw a line using given axis values with suitable label in the x axis, y axis and a title")

        while flag :
            try :

                print("______________________________________")
                choice = int(input("Enter your choice"))

                if choice == 0:
                    flag = False

                elif choice == 1:
                    x_axis = int(input("enter a values for X- axis"))
                    x_axis_values = self.obj.list_creation(x_axis)
                    print(x_axis_values)
                    y_axis = int(input("enter a values for Y- axis"))
                    y_axis_values = self.obj.list_creation(y_axis)
                    print(y_axis_values)

                    # set a title
                    plt.title("draw a line")

                    # set x-axis lable
                    plt.xlabel("x-axis")

                    # set y-axis lable
                    plt.ylabel("y-axis")

                    # set plot lines
                    plt.plot(x_axis_values, y_axis_values)
                    plt.show()

                elif choice == 2:
                    x_axis = int(input("enter a values for X- axis"))
                    x_axis_values = self.obj.list_creation(x_axis)
                    print(x_axis_values)
                    y_axis = int(input("enter a values for Y- axis"))
                    y_axis_values = self.obj.list_creation(y_axis)
                    print(y_axis_values)

                    # set a title
                    plt.title("draw a line")

                    # set x-axis lable
                    plt.xlabel("x-axis")

                    # set y-axis lable
                    plt.ylabel("y-axis")

                    # set plot lines
                    plt.plot(x_axis_values, y_axis_values)
                    plt.show()

                else:
                    print("enter valid choice")
            except Exception as e:
                print(e)


obj = Matplotlib_Programs()
obj.draw_line()
