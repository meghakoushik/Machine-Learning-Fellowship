"""13. The table below shows the height, x, in inches and the pulse rate, y, per minute
    for 9 people. Write a program to find the correlation coefficient and interpret your result.
    x ⇒ 68 72 65 70 62 75 78 64 68
    y ⇒ 90 85 88 100 105 98 70 65 72"""

#
import math


def correlation_Coefficient(X, Y, n):

    sum_X = 0
    sum_Y = 0
    sum_XY = 0
    squareSum_X = 0
    squareSum_Y = 0

    i = 0
    while i < n:
        # sum of elements of array X.
        sum_X = sum_X + X[i]

        # sum of elements of array Y.
        sum_Y = sum_Y + Y[i]

        # sum of X[i] * Y[i].
        sum_XY = sum_XY + X[i] * Y[i]

        # sum of square of array elements.
        squareSum_X = squareSum_X + X[i] * X[i]
        squareSum_Y = squareSum_Y + Y[i] * Y[i]

        i = i + 1
    print("sum of list X is:", sum_X)
    print("sum of list Y is:", sum_Y)
    print("summation of X and Y is:", sum_XY)
    # using calculating correlation formula
    correlation_result = float(n * sum_XY - sum_X * sum_Y) / float(
        math.sqrt((n * squareSum_X - sum_X * sum_X) * (n * squareSum_Y - sum_Y * sum_Y)))
    print("correlation_coefficient result is:", correlation_result)


list_X = [68, 72, 65, 70, 62, 75, 78, 64, 68]
list_y = [90, 85, 88, 100, 105, 98, 70, 65, 72]

# Find the size of array.
n = len(list_X)
print("length of list:", n)
# Function call
correlation_Coefficient(list_X, list_y, n)
