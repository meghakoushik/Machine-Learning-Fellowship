from matplotlib import pyplot as plt
import pandas as pd


class financial:

    def read_data(self):
        # reading csv file
        df = pd.read_csv('test.csv', sep=',', parse_dates=True, index_col=0)
        # plotting lines
        df.plot()
        # Show the figure.
        plt.show()


# creates class object
obj = financial()
# calling method by using class object
obj.read_data()