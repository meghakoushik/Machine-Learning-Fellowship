"""1. Write a Python programming to create a pie chart of the popularity of programming
Languages."""

import matplotlib.pyplot as plt


class Language_Popularity:
    choice = 0

    def pie_chart(self):
        flag = True
        print("1. create a pie chart of the popularity of programming Languages.")
        print("2. Create a pie chart with a title of the popularity of programming Languages.")
        print("3. Exit")

        while flag:
            try:
                # accept choice from user
                self.choice = input("Enter choice :")

                # validate choice number

                def validate_num(num):
                    try:
                        int(num)
                        return True
                    except ValueError:
                        print("enter valid integer value")

                valid_choice = validate_num(self.choice)
                if valid_choice:
                    choice = int(self.choice)

                    def create_list_all(element):
                        new_value = []
                        try:
                            for item in range(element):
                                input_value = input("Enter element:")
                                # if input_value.isalpha():
                                #      break
                                # print ( "invalid input\n", "enter only alphabets")
                                if len(input_value) >= 1:
                                    new_value.append(input_value)
                                else:
                                    print("String length should be 2 or more")

                        except Exception as e:
                                print(e)
                        return new_value
                    if choice == 0:
                        flag = True
                    if choice == 1:
                        print("Enter programming languages:")
                        # create list of 5 languages
                        lang = create_list_all(5)
                        print("Enter popularity of that language:")
                        # list of popularity
                        popularity = create_list_all(5)
                        # explode 1st slice
                        explode = (0.1, 0, 0, 0, 0)
                        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

                        # plot
                        plt.pie(popularity, explode=explode, labels=lang, colors=colors, autopct='%1.1f%%',
                                shadow=True, startangle=140)
                        plt.axis('equal')

                        # set the title
                        plt.title("Popularity of Programming Language\n")
                        plt.show()

                    elif choice == 2:

                        print("Enter programming languages:")
                        # create list of 5 languages
                        lang = create_list_all(5)
                        print("Enter popularity of that language:")
                        # list of popularity
                        popularity = create_list_all(5)
                        # explode 1st slice
                        explode = (0.1, 0, 0, 0, 0)
                        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd" ]

                        # plot
                        plt.pie(popularity, explode=explode, labels=lang, colors=colors, autopct='%1.1f%%',
                                shadow=True, startangle=140)
                        plt.axis('equal')

                        # set the title
                        # plt.title("Popularity of Programming Language\n")
                        plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago",
                                   bbox={'facecolor': '0.8', 'pad': 5})

                        plt.show()

                    elif choice == 3:
                        print("Exit")

                    else:
                        print("Enter valid choice")
                else:
                    print("Enter integer number")
            except Exception as e:
                print(e)


obj = Language_Popularity()
obj.pie_chart()
