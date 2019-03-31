"""10. Write a Python program to plot quantities which have an x and y position"""

from week4.Python_matplotlib.Utility.matplotlib_Utility import Util
from matplotlib import pyplot as plt


class plot_quantities:
    def __init__(self):
        self.obj = Util()

    def plot_xy_quantities(self):
        values = int(input("enter numbers for list1:"))
        x_axis1 = self.obj.list_creation(values)
        print(x_axis1)
        values = int(input("enter the values for list2:"))
        y_axis1 = self.obj.list_creation(values)
        print(y_axis1)
        values = int(input("enter numbers for list3:"))
        x_axis2 = self.obj.list_creation(values)
        print(x_axis2)
        values = int(input("enter the values for list4:"))
        y_axis2 = self.obj.list_creation(values)
        print(y_axis2)

        plt.xlabel('x_axis')
        plt.ylabel('y_axis')
        plt.title("plot quantities for x, y position ")
        plt.axis([0, 100, 0, 100])
        plt.plot(x_axis1, y_axis1, 'b*', x_axis2, y_axis2, 'ro')
        plt.show()


obj = plot_quantities()
obj.plot_xy_quantities()
