from week4.matplotlib_scatterPlot.scatterPlot_utility.utility_demo import get_marks
import matplotlib.pyplot as plt


class CompareTwoSubject:

    def scatter_plots(self):
        print("1. Draw a scatter plot comparing two subject marks of Mathematics and Science.Use marks of 10 students.")
        print("2. Exit")

        while True:
            try:
                print("______________________________________")
                choice = int(input("enter choice"))
                if choice == 0:
                    print('select choice')
                elif choice == 1:
                    # range of marks
                    marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
                    print("Mathematics marks:")
                    # get maths marks
                    math_marks = get_marks(len(marks_range))
                    print("Science marks:")
                    # get science marks
                    science_marks = get_marks(len(marks_range))
                    # plot math marks
                    plt.scatter(marks_range, math_marks, label="Maths marks", color='g')
                    # plot science marks
                    plt.scatter(math_marks, science_marks, label="Science marks", color='r' )
                    plt.xlabel("marks range")
                    plt.ylabel("marks scored")
                    # linked to the data being graphically displayed in the plot area of the chart.
                    plt.legend()
                    plt.show()
                elif choice == 2:
                    exit()
                else:
                    print("Enter valid choice")
            except Exception as e:
                print(e)


obj = CompareTwoSubject()
obj.scatter_plots()
