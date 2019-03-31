import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
from week4.Seaborn_plot.Seaborn_utility.seaborn_bar_utility import Util


class Seaborn_Programs:

    def __init__(self):
        self.obj = Util()
    
    print("1. to draw bar plot of sex against survived for a dataset given in the url ")
    print("2. to draw a point plot for sex against survived for a data set given in url ")
    print("3. 1. Write a program to draw a scatter plot of “day” against “total bill” for a dataset given in a url")
    print("4. to draw a violin plot of sex against total_bill  for a  given data set")
    print("5. 2. Write a program to draw a violin plot of “species” against “sepal length” for a dataset given in a url")
    print("6. to draw box plot of life expectancy by continent for a data set given in a url ")
    print("7. Write a program to draw a box plot of day by tips for a data set given in a url")
    print("8. Write a program to draw a swarm plot of total bill against size  for a  given data set.")
    print("9. Write a program to draw swarm plot of “total bill” against day for a dataset given in url")
    print("0. EXIT")

    def choice_display(self):

        flag = True

        while flag:

            try:

                print()

                choice = int(input("Enter your choice"))

                if choice == 0:
                    flag = False

                elif choice == 1:

                    """Write a program to draw bar plot of sex against survived for a dataset given in the url"""
                    self.obj.bar_plot()

                elif choice == 2:

                    """Write a program to draw a point plot for sex against survived for a data set given in url"""

                    self.obj.point_plot()

                elif choice == 3:

                    """program to draw a scatter plot of "day" against "total bill" for a data set given in a url """

                    self.obj.scatter_plot()

                elif choice == 4:

                    """Write a program to draw a violin plot of sex against total_bill  for a  given data set """
                    self.obj.violin_plot()

                elif choice == 5:

                    """prog to draw a violin plot of "species" against "sepal length" for a data set given in a url"""

                    df = sb.load_dataset('iris')
                    sb.violinplot(x="species", y="sepal_length", data=df)
                    plt.title("VIOLIN PLOT")
                    plt.show()

                elif choice == 6:

                    """ program to draw box plot of life expectancy by continent for a data set given in a url """

                    self.obj.box_plot()

                elif choice == 7:

                    """Write a program to draw a box plot of day by tips for a data set given in a url"""

                    df_two = pd.read_csv('tips.csv')

                    sb.boxplot(data=df_two, x="tip", y="day")
                    plt.title("BOX PLOT")
                    plt.show()

                elif choice == 8:

                    """Write a program to draw a swarm plot of total bill against size  for a  given data set """

                    self.obj.swarm_plot()

                elif choice == 9:

                    """Write a program to draw swarm plot of "total bill" against day for a data set given in url"""
                    df = sb.load_dataset('tips')
                    sb.swarmplot(x="size", y="total_bill", data=df)
                    plt.title("SWARM PLOT")
                    plt.show()

                else:
                    print(" Enter Valid choice between 0-9")

            except Exception as e:
                print("Invalid Input", e)


obj = Seaborn_Programs()
obj.choice_display()
