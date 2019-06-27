import numpy as np
import matplotlib.pyplot as plt


class Util:
    weight = []
    height = []
    # creating list for all types and len > 2

    def grouping(self, element):
        list_value = []
        try:
            for item in range(element):
                input2 = input("Enter element : ")
                if int(input2) >= 1:
                    list_value.append(input2)
                else:
                    print("please enter valid size")

        except Exception as e:
            print(e)
        return list_value

    def group_wise(self, weight1, weight2, weight3, height1, height2, height3):

        weight = np.concatenate(weight1, weight2, weight3)
        height = np.concatenate(height1, height2, height3)
        plt.scatter(weight, height, marker='*', color=[ 'red', 'green', 'blue'])
        plt.xlabel('weight', fontsize=16 )
        plt.ylabel('height', fontsize=16 )
        plt.title('Group wise Weight vs Height scatter plot', fontsize=20)
        plt.show()
