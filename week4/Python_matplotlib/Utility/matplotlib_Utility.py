from matplotlib import pyplot as plt


class Util:

    def list_creation(self, size):
        list_value = []
        for value in range(size):
            words = int(input("enter value"))
            list_value.append(words)
        return list_value

    def draw_multiple_line(self, x1_axis, y1_axis, x2_axis, y2_axis):
        # # plot the value for x- axis
        plt.plot(x1_axis, y1_axis, label="line 1")

        # plot the value for y-axis
        plt.plot(x2_axis, y2_axis, label="line 2")

        # for x axis label
        plt.xlabel('x - axis')
        # for y axis label
        plt.ylabel('y - axis')

        # Set a title
        plt.title('same plot with suitable legends of each line ')

        plt.xlabel('X -axis')
        plt.ylabel('Y- axis')
        # show a legend on the plot, on top right corner as x-axis and y-axis
        plt.legend()

        # Display a figure.
        plt.show()

    def different_colors(self, x1_axis, y1_axis, x2_axis, y2_axis) :
        plt.plot(x1_axis, y1_axis, color='blue', linewidth=3, label='line1-width-3')
        plt.plot(x2_axis, y2_axis, color='red', linewidth=5, label='line2-width-5')

        # Set the x axis label
        plt.xlabel('x - axis')
        # Set the y axis label
        plt.ylabel('y - axis')

        # Set a title
        plt.title('Two or more lines on same plot with suitable legends, and color ')

        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')

        # show a legend on the plot, on top right corner as line1 and line2
        plt.legend()

        # Display a figure.
        plt.show()

    def different_style(self, x1_axis, y1_axis, x2_axis, y2_axis):
        plt.plot(x1_axis, y1_axis, linestyle='dashed', label="line 1")
        plt.plot(x2_axis, y2_axis, linestyle=':', label="line 2")

        # Set the x axis label
        plt.xlabel('x - axis')
        # Set the y axis label
        plt.ylabel('y - axis')

        # Set a title
        plt.title(' plot two or more lines and set the line markers ')

        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')

        # show a legend on the plot, on top right corner as line1 and line2
        plt.legend()

        # Display a figure.
        plt.show()

    def line_marker(self, x1_axis, y1_axis, x2_axis, y2_axis):
        plt.plot(x1_axis, y1_axis, color='red', linestyle='dashdot', linewidth=3, marker='0', markerfacecolor='blue', markersize='12')
        plt.plot(x2_axis, y2_axis, color='red', linestyle='dotted', linewidth=3, marker='0', markerfacecolor='blue', markersize='12')

        plt.ylim(1, 8)
        plt.ylim(1, 8)

        # Set the x axis label
        plt.xlabel('x - axis')
        # Set the y axis label
        plt.ylabel('y - axis')

        # Set a title
        plt.title(' plot two or more lines and set the line markers ')
        plt.legend()

        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')

        # Display a figure.
        plt.show()
