import pandas as pd
import numpy as np


class Util:
    def __init__(self):
        self.arr = np.array([1, 2, 3, 4, 5])
        self.exam_data = {
            'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin',
                     'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1 ],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes' ]}

        self.labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        self.df = pd.DataFrame(self.exam_data, index=self.labels)

    """-------------------------------------------------------------------------------"""
    """display a one-dimensional array-like object containing an array of data using Pandas module."""

    def create_series(self):
        series = pd.Series(self.arr)
        return series

    """-------------------------------------------------------------------------------"""
    """convert a Panda module Series to Python list and it's type"""

    def convert(self):
        series = pd.Series(self.arr)
        print("Convert Pandas Series to Python list", series)
        new_series = series.tolist()
        print(type(series.tolist()))
        return new_series

    """-------------------------------------------------------------------------------"""
    """Python program to add, subtract, multiple and divide two Pandas Series"""

    def operation_on_series(self, num1, num2):
        values = num1 + num2
        print("\n Add two Series:")
        print(values)
        print("\n Subtract two Series:")
        values = num1 - num2
        print(values)
        print("\n Multiply two Series:")
        values = num1 * num2
        print(values)
        print("\n Divide Series1 by Series2:")
        values = num1 / num2
        print(values)

    """-------------------------------------------------------------------------------"""
    """Python program to add, subtract, multiple and divide two Pandas Series")"""

    def get_power(self):
        values = np.arange(6)
        print("original list values:", values)
        values = (np.power(values, 3))
        return values

    """-------------------------------------------------------------------------------"""
    """display a DataFrame from a specified dictionary data which has the index labels"""

    def data_frame(self):
        df = pd.DataFrame(self.exam_data, self.labels)
        return df

    """-------------------------------------------------------------------------------"""
    """display a summary of the basic information about a specified Data Frame and its data"""

    def basic_information(self) :
        # df = pd.DataFrame(self.exam_data, self.labels)
        return self.df.info()

    """-------------------------------------------------------------------------------"""
    """ get the first 3 rows of a given DataFrame. Sample Python dictionary  data and list labels"""

    def display_dataframe(self):
        df = pd.DataFrame(self.exam_data, self.labels)
        return df.iloc[::3]

    """-------------------------------------------------------------------------------"""
    """Write a Python program to select the 'name' and 'score' columns from the following DataFrame."""

    def row_column(self):
        # df = pd.DataFrame(self.exam_data, index=self.labels)
        return self.df[['name', 'score']]

    """-------------------------------------------------------------------------------"""
    """Write a Python program to select the specified columns and rows from a given data frame"""

    def row_column_dataframe(self):
        # df = pd.DataFrame(self.exam_data, index=self.labels)
        return self.df.iloc[[1, 4, 9, 2], [1, 2]]

    """-------------------------------------------------------------------------------"""
    """select the rows where the number of attempts in the examination is greater than 2."""

    def set_attempts(self):
        # df = pd.DataFrame(self.exam_data, index=self.labels)
        return self.df[ (self.df['attempts'] < 3) & (self.df['score'] > 15)]

    """-------------------------------------------------------------------------------"""
    """ program to count the number of rows and columns of a DataFrame."""

    def count_row_column(self):
        # df = pd.DataFrame(self.exam_data, index=self.labels)
        rows = len(self.df.axes[0])
        columns = len(self.df.axes[1])
        print("count no. of rows", rows)
        print("count no. of columns", columns)

    """-------------------------------------------------------------------------------"""
    """Write a Python program to select the rows where the score is missing, i.e. is NaN"""

    def missing_score(self) :
        # df = pd.DataFrame(self.exam_data, index=self.labels)
        return self.df[ self.df['score'].isnull()]

    """-------------------------------------------------------------------------------"""
    """Write a Python program to select the rows where number of attempts in the examination is less than 2 and score"""
    def attempts_greater_less(self) :
        return self.df[ self.df[ 'score'].between(2, 15)]

    """-------------------------------------------------------------------------------"""
    """Write a Python program to change the score in row 'd' to 11.5"""

    def changed_score(self) :
        df = pd.DataFrame(self.exam_data, index=self.labels)
        df.loc['d', 'score'] = 11.5
        return df

    """-------------------------------------------------------------------------------"""
    """Write a Python program to calculate the sum of the examination attempts by the students"""
    def sum_Of_attempts(self):
        return self.df['attempts'].sum()

    """-------------------------------------------------------------------------------"""
    """Write a Python program to calculate the mean score for each different student in DataFrame."""
    def mean_score(self) :
        return self.df['score'].mean()

    """-------------------------------------------------------------------------------"""
    """append a new row 'k' to data frame with given values for each column. Now delete the new row and return the origi"""
    def update_row(self) :
        df = pd.DataFrame(self.exam_data, index=self.labels)
        df.loc['k'] = [1, 'xyz', 'yes', 12.2]
        print(df)
        df = df.drop('k')
        return df

    """---------------------------------------------------------------------------------"""
    """To sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order."""
    def Desc_Asc_order(self):
        print("original dataframe:\n\n", self.df)
        print("\n")
        return self.df.sort_values(by=['name', 'score'], ascending=[False, True])

    """---------------------------------------------------------------------------------"""
    """To replace the 'qualify' column contains the values 'yes' and 'no' with True and False."""

    def replace_column(self):
        print("original dataframe:\n\n", self.df)
        self.df['qualify'] = self.df['qualify' ].map({'yes': True, 'No': False})
        return self.df

    """---------------------------------------------------------------------------------"""
    """To delete the 'attempts' column from the DataFrame."""

    def delete_attempts(self):
        print("original dataframe:\n", self.df)
        del self.df['attempts']
        # OR del.pop('attempts')
        return self.df

    """---------------------------------------------------------------------------------"""
    """To insert a new column in existing DataFrame"""

    def insert_column(self):
        print("original dataframe:\n", self.df)
        print("\n")
        second_attempt = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
        self.df['second_attempt'] = second_attempt
        return self.df

    """---------------------------------------------------------------------------------"""
    """To iterate over rows in a DataFrame"""

    def iterated_row(self):
        print("original dataframe:\n", self.df)
        for index, row in self.df.iterrows():
            return row['name'], row['score']

    """---------------------------------------------------------------------------------"""
    """Write a Python program to get list from DataFrame column headers"""

    def column_header(self):
        print("original dataframe:\n", self.df)
        return list(self.df.columns.values)


obj = Util()
