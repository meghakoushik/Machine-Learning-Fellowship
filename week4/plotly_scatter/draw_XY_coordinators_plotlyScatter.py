from week4.plotly_scatter.plotly_scatter_utility.utility import Util


class plotly_programs:

    # class constructor
    def __init__(self):
        self.obj1 = Util()

    def display(self):
        flag = True
        print("1. Draw a scatter plot for random 1000 x and y coordinates ")
        print("2. Draw line and scatter plots for random 100 x and y coordinates")
        print("3. Draw a scatter plot for random 500 x and y coordinates and style it")
        print("4. Draw a scatter plot for a given data set and show data labels on hover")
        print("5. Exit")

        while flag:
            try:

                print("______________________________________")
                choice = int(input("Enter your choice"))

                if choice == 0:
                    flag = False

                elif choice == 1:
                    x_axis = int(input("enter X axis values"))
                    y_axis = int(input("enter Y axis values"))
                    if x_axis == y_axis:
                        self.obj1.draw_scatter_plot(x_axis, y_axis)
                    else:
                        print("enter same value of x and y axis")

                elif choice == 2:
                    x_axis = int(input("enter X axis values"))
                    y_axis = int(input("enter Y axis values"))
                    if x_axis == y_axis:
                        self.obj1.draw_line(x_axis, y_axis)
                    else:
                        print("enter same value of x and y axis")

                elif choice == 3:
                    x_y_axis = int(input("Enter random value for  x and y axis, to draw Scatter line"))
                    self.obj1.sctter_plot_style(x_y_axis)

                elif choice == 4:
                    self.obj1.data_set()

                else:
                    print(" enter valid choice: ")

            except Exception as e:
                print(e)


obj = plotly_programs()
obj.display()
