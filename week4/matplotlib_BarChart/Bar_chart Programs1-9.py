import matplotlib.pyplot as plt
from week4.matplotlib_BarChart.BarChart_utility.utility import Util


class bar_chart:
    # creates utility class object
    utility_obj = Util()

    # accept size of points you wanna accept
    size = utility_obj.accept_size ()

    # accepts x axis values
    print("enter programming languages")
    language = utility_obj.accept_languages(size)
    print(language)

    # accepts y axis values
    print("enter popularity")
    popularity = utility_obj.accept_popularity(size)
    print(popularity)

    # Set the x axis label
    plt.xlabel("Languages")

    # Set the y axis label
    plt.ylabel("Popularity")

    # Sets a title
    plt.title("Popularity of Programming Languages")

    """1. Write a Python programming to display a bar chart of the popularity of programming
        Languages."""

    def draw_bar_vertically(self) :

        # iterate through no.of language
        x_pos = [i for i, _ in enumerate(self.language)]

        # plotting x and y axis values to create bar chart
        plt.bar(x_pos, self.popularity, color='blue')

        # set the current tick locations and labels(language name)of the x-axis
        plt.xticks(x_pos, self.language)

        # Shows the figure.
        plt.show()

    """----------------------------------------------------------------------------------------------"""
    """2.Write a Python programming to display a horizontal bar chart of the popularity of
        programming Languages."""

    def draw_bar_horizontally(self):
        # iterate through no.of language
        x_pos = [i for i, _ in enumerate(self.language)]

        # plotting x and y axis values to create bar chart horizontally
        plt.barh(x_pos, self.popularity, color='green')

        # set the current tick locations and labels(language name) to y-axis
        plt.yticks(x_pos, self.language)

        plt.show()

    """----------------------------------------------------------------------------------------------"""
    """3.Write a Python programming to display a bar chart of the popularity of programming
         Languages. Use uniform color."""

    def draw_bar_with_uniform_color(self):
        # iterate through no.of language
        x_pos = [i for i, _ in enumerate(self.language)]

        # plotting x and y axis values to create bar chart
        plt.bar(x_pos, self.popularity, color=(0.2, 0.4, 0.6, 0.6))

        # set the current tick locations and labels(language name)of the x-axis
        plt.xticks(x_pos, self.language)

        # Shows the figure.
        plt.show()

    """----------------------------------------------------------------------------------------------"""
    """4.Write a Python programming to display a bar chart of the popularity of programming
        Languages. Use different color for each bar."""

    def draw_bar_with_diff_color(self):
        # iterate through no.of language
        x_pos = [i for i, _ in enumerate(self.language)]

        # plotting x and y axis values to create bar chart
        plt.bar(x_pos, self.popularity, color=['black', 'red', 'green', 'blue', 'cyan'])

        # set the current tick locations and labels(language name)of the x-axis
        plt.xticks(x_pos, self.language )

        # Shows the figure.
        plt.show()

    """----------------------------------------------------------------------------------------------"""
    """5.Write a Python programming to display a bar chart of the popularity of programming
           Languages. Attach a text label above each bar displaying its popularity (float value)"""

    def attach_label(self):

        # iterate through no.of language
        x_pos = [i for i, _ in enumerate(self.language)]

        fig, ax = plt.subplots ()
        rects1 = ax.bar(x_pos, self.popularity, color='b')
        plt.xticks(x_pos, self.language)

        # for i, v in enumerate(rects1):
        #     ax.text(v + 3, i + .25, str(v), color='red', fontweight='bold')

        def autolabel(rects):
            # Attach a text label above each bar displaying its height
            for rect in rects:
                height = rect.get_height()
                print("getx", rect.get_x())
                ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                          '%f' % float(height),
                          ha='center', va='bottom')

        autolabel(rects1)

        # Shows the figure.
        plt.show()

    """----------------------------------------------------------------------------------------------"""
    """6.Write a Python programming to display a bar chart of the popularity of programming
            Languages. Make blue border to each bar."""

    def make_border(self):
        # iterate through no.of language
        x_pos = [i for i, _ in enumerate(self.language)]

        # plotting x_pos and popularity values to create bar chart
        plt.bar(x_pos, self.popularity, color='red', edgecolor='blue')

        # set the current tick locations and labels(language name)of the x-axis
        plt.xticks(x_pos, self.language)

        # Shows the figure.
        plt.show()

    """----------------------------------------------------------------------------------------------"""

    """7.Write a Python programming to display a bar chart of the popularity of programming
             Languages. Specify the position of each bar plot."""

    def specify_width_position(self):

        x_pos = [i for i, _ in enumerate(self.language)]
        plt.xticks(x_pos, self.language)

        # Select the width of each bar and their positions
        width = [0.2, 0.1, 0.3, 1.1, 0.2, 0.3]
        y_pos = [0, .7, 1.5, 3, 9, 6]

        # Create bars
        plt.bar(y_pos, self.popularity, width=width)
        plt.xticks(y_pos, self.language)

        plt.show ()

    """------------------------------------------------------------------------------------------------"""
    """9.Write a Python programming to display a bar chart of the popularity of programming
                Languages. Increase bottom margin"""

    def increase_margin(self) :
        # iterate through no.of language
        x_pos = [i for i, _ in enumerate(self.language)]
        # plotting x_pos and popularity values to create bar chart
        plt.bar(x_pos, self.popularity, color=(0.4, 0.6, 0.8, 1.0))

        # Rotation of the bars names
        plt.xticks(x_pos, self.language)

        # Custom the subplot layout
        plt.subplots_adjust(bottom=0.10, top=.4)

        # Shows the figure.
        plt.show()

    """----------------------------------------------------------------------------------------------"""
    def menu(self):

        print("1.Write a Python programming to display a bar chart of the popularity of programming Languages.")
        print("2.Write a Python programming to display a horizontal bar chart of the popularity of programming Languages")
        print("3.display a bar chart of the popularity of programming Languages. Use uniform color.")
        print("4.Write a Python programming to display a bar chart of the popularity of programming Languages. Use different color for each bar")
        print("5.display a bar chart of the popularity of programming Languages. Attach a text label above each bar displaying its popularity (float value)")
        print("6.display a bar chart of the popularity of programming Languages. Make blue border to each bar.")
        print("7.to display a bar chart of the popularity of programming Languages. Specify the position of each bar plot")
        print("9.to display a bar chart of the popularity of programming Languages. Increase bottom margin")
        print("0.exit")

        flag = True

        while flag:

            try:
                choice = int(input("\nEnter ur choice"))

                if choice == 1:
                    obj.draw_bar_vertically()

                if choice == 2:
                    obj.draw_bar_horizontally()

                if choice == 3:
                    obj.draw_bar_with_uniform_color()

                if choice == 4:
                    obj.draw_bar_with_diff_color()

                if choice == 5:
                    obj.attach_label()

                if choice == 6:
                    obj.make_border()

                if choice == 7:
                    obj.specify_width_position()

                if choice == 9:
                    obj.increase_margin()

                if choice == 0:

                    flag = True
                else:
                    raise ValueError

            except ValueError:
                print("enter valid input")


# creates class object
obj = bar_chart()


# calling method by using class object
obj.menu()
