"""3. Draw a line using given axis values taken from a text file,
                        with suitable label in the x axis, y axis and a title."""
from matplotlib import pyplot as plt


class text_file_program:

    def value_text_file(self):
        with open("test.txt") as f:
            file = f.read()
            file = file.split('\n')

            x = [row.split(' ')[0] for row in file]
            y = [row.split(' ')[0] for row in file]
            # plotting the line points

            plt.plot(x, y)
            # Set the x axis label of the current axis.
            plt.xlabel('x-axis')
            # Set the x axis label of the current axis.
            plt.ylabel('y-axis')

            # set the title
            plt.title("draw a line using values that taken from text file")

            # show the plot
            plt.show()


obj = text_file_program()
obj.value_text_file()
