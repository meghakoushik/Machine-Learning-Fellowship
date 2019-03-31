"""9.Write a Python program to display the current axis limits values and set new axis value"""
from week4.Python_matplotlib.Utility.matplotlib_Utility import Util
from matplotlib import pyplot as plt


class Set_Get_Axis_Values :
    # line 1 points
    utility_obj = Util()

    def draw_line(self) :
        # line 1 points
        x1 = int(input("enter the values for x-axis"))
        x1_list = self.utility_obj.list_creation(x1)
        print(x1_list)

        y1 = int(input("enter the values for y-axis"))
        y1_list = self.utility_obj.list_creation(y1)
        print(y1_list)

        # plotting the line 1 points
        plt.plot(x1_list, y1_list, label="line 1")

        # Set the x axis label
        plt.xlabel('x - axis')
        # Set the y axis label
        plt.ylabel('y - axis')

        # Sets a title
        plt.title('Two or more lines on same plot with suitable legends ')

        # returns current axis values
        print(plt.axis())

        # accepting values to set new axis values
        print("set new axis limit")

        # x_min = int(input("x_min val"))
        x_max = int(input("x_max val"))
        # y_min = int(input("y_min val"))
        y_max = int(input("y_max val"))

        # sets new axis values
        plt.axis([ 0, x_max, 0, y_max ])

        # show a legend on the plot
        plt.legend()

        # Display a figure.
        plt.show()


# creates class object
obj = Set_Get_Axis_Values()

# calling method by using class object
obj.draw_line()
