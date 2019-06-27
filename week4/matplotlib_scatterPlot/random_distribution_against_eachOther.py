"""2. Draw a scatter plot with empty circles taking a random distribution in X and Y "
              "and plotted against each other"""
from week4.matplotlib_scatterPlot.scatterPlot_utility.utility_demo import validate_num, random_distribution
import matplotlib.pyplot as plt


class EmptyCircle_plotted:

    def scatter_plots(self):
        print("1. Draw a scatter plot with empty circles taking a random distribution in X and Y "
              "and plotted against each other")
        print("2. Exit")
        while True:
            try:
                print()
                # accept choice from user
                self.choice = input("Enter choice : ")
                # validate choice number
                valid_choice = validate_num(self.choice)
                if valid_choice:
                    choice = int(self.choice)
                    if choice == 1:
                        x_value = random_distribution()
                        y_value = random_distribution()
                        # generate a scatter plots
                        plt.scatter(x_value, y_value, s=70, facecolors='none', edgecolors='g')
                        plt.xlabel('X')
                        plt.ylabel('Y')
                        plt.show()
                    elif choice == 2:
                        exit()
                    else:
                        print("Enter valid choice")
                else:
                    print("Enter only numbers")
            except Exception as e:
                print(e)


obj = EmptyCircle_plotted()
obj.scatter_plots()