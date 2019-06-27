"""1. Write a Python program to draw a scatter graph taking a random distribution in X and Y and
       plotted against each other."""

import matplotlib.pyplot as plt
import random
import math


class random_distribution:

    def scatter_plots(self):

        flag = True
        print("1. to draw a scatter graph taking a random distribution in X and Y and plotted against each other")
        print("2. Exit")

        while flag:
            try:
                    print("______________________________________")
                    choice = int(input("Enter your choice"))

                    if choice == 0:
                       flag = False

                    if choice == 1:
                        no_of_balls = 25

                        # Draw samples from the triangular distribution over the interval [left, right].
                        x = [random.triangular() for _ in range(no_of_balls)]

                        # draw samples from normal distribution/gaussian distribution
                        y = [random.gauss(0.5, 0.25) for _ in range(no_of_balls)]

                        colors = [random.randint(1, 4) for _ in range(no_of_balls)]

                        areas = [math.pi * random.randint(5, 15) ** 2 for _ in range(no_of_balls)]
                        # create a figure object
                        plt.figure()

                        plt.scatter(x, y, s=areas, c=colors, alpha=0.850)
                        plt.axis([0.0, 1.0, 0.0, 1.0])
                        plt.xlabel('X')
                        plt.ylabel('Y')
                        plt.show()
                    elif choice == 2:
                        exit()

                    else:
                         print("Enter valid choice")
            except Exception as e:
                print(e)


obj = random_distribution()
obj.scatter_plots()