from week4.matplotlib_scatterPlot.scatterPlot_utility.utility_demo import validate_num, list_created
import matplotlib.pyplot as plt
import numpy as np


# class to perform graphical representation of data using matplotlib pie chart
class CompareWeightsAndHeights:
    choice = 0

    def scatter_plots(self):
        print("1. program to draw a scatter plot for three different groups comparing weights and heights.")
        print("2. Exit")
        while True:
            try:
                # accept choice from user
                self.choice = input("Enter choice : ")
                # validate choice number
                valid_choice = validate_num(self.choice)
                if valid_choice:
                    choice = int(self.choice)

                    if choice == 1:

                        print("Weight 1 values:")
                        weight1 = list_created(3)
                        print("height 1 values:")
                        height1 = list_created(3)
                        print("Weight 2 values:")
                        weight2 = list_created(3)
                        print("height 2 values:")
                        height2 = list_created(3)
                        print("Weight 3 values:")
                        weight3 = list_created(3)
                        print("height 3 values:")
                        height3 = list_created(3)

                        weight = np.concatenate(weight1, weight2, weight3)
                        height = np.concatenate(height1, height2, height3)

                        plt.scatter(weight, height, marker='*', color=['red', 'green', 'blue'])

                        plt.xlabel("weight", fontsize=16)
                        plt.ylabel("height", fontsize=16)

                        plt.title("Group of weight and height scatter plot", fontsize=20)
                        plt.show()

                    elif choice == 2:
                        exit()
                else:
                    print("Enter valid choice")
            except Exception as e:
                print(e)


obj = CompareWeightsAndHeights()
obj.scatter_plots()