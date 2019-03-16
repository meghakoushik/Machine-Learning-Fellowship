from week2.Utility.Utilclass import Util
from itertools import groupby
from operator import itemgetter
import itertools


class List:
    obj = Util()

    main_list = [23, 42, 45, 57, 66, 22, 66, 94]

    flag = True

    print("1. Write a Python program to sum all the items in a list. ")
    print("2. Write a Python program to multiplies all the items in a list. ")
    print("3. Write a Python program to get the smallest number from a list. ")
    print("4. Python program to count the number of str the first and last character are same from a given list of str")
    print("5. Write a Python program to get a list, sorted in increasing order by the last element")
    print("6. Write a Python program to remove duplicates from a list.  ")
    print("7. Write a Python program to clone or copy a list. ")
    print("9. Python function that takes two lists and returns True if they have at least one common member")
    print("10. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.")
    print("11. Write a Python program to generate all permutations of a list in Python.")
    print("12. Write a Python program to get the difference between the two lists.")
    print("13. Write a Python program to append a list to the second list. ")
    print("14. Write a python program to check whether two lists are circularly identical.")
    print("15. Write a Python program to find common items from two lists.")
    print("16. Write a Python program to split a list based on first character of word.")
    print("17. Write a Python program to remove duplicates from a list of lists.  ")
    print("0. EXIT")

    while flag:

        try:

            print('_______________________________________________________________')

            choice = int(input("Enter your choice"))

            if choice == 0:
                flag = False

            if choice == 1:

                """ 1. Write a Python program to sum all the items in a list.  """
                try:
                    # create empty list
                    list_words = []

                    # get num of element from user
                    number = input("\nEnter the number of elements in list:")
                    num1 = int(number)
                    print("")
                    # if user enter number is valid
                    if number.isdigit():

                        # enter element in list
                        input_string = input("Enter a list element separated by space ")

                        # for space
                        list11 = input_string.split()

                        sum_element = 0

                        # get num in list11
                        for num in list11:
                            # sum of element
                            sum_element += int(num)

                        if num.isdigit():

                            print("Sum = ", sum_element)

                        else:
                            raise Exception
                    else:
                        raise Exception

                except Exception as e:

                    print("enter digit only", e)

            elif choice == 2:

                """2. Write a Python program to multiplies all the items in a list.  """

                print("multiplies all the items in a list:", obj.multi_list(main_list))

            elif choice == 3:

                """3. Write a Python program to get the smallest number from a list.  """

                print("smallest number from a list", obj.min_list(main_list))

            elif choice == 4:

                """4. Write a Python program to count the number of strings where the string length is 2 or more and the
                first and last character are same from a given list of strings."""

                words_list = ['abc', 'xyz', 'aba', '1221']

                print("\n first and last character same from list of strings count: ", obj.match_words(words_list))

            elif choice == 5:

                """5. Write a Python program to get a list, sorted in increasing order by the last element in each 
                tuple from a given list of non-empty tuples"""

                Sample_List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
                print("Sorted:", obj.sort(Sample_List))

            elif choice == 6:

                """6. Write a Python program to remove duplicates from a list. """

                print("\n my result list:", obj.remove_Duplicates(main_list))

            elif choice == 7:

                """7. Write a Python program to clone or copy a list. """

                print("\n clone or copy a list:", obj.cloning_list(main_list))

            elif choice == 8:
                """8. Write a Python program to find the list of words that are longer than n from a
                      given list of words."""
                print(obj.longer_words(3, "python is an programming language"))

            elif choice == 9:

                """9. Python function that takes two lists and returns True if they have at least one common member."""

                first_set = [1, 2, 3, 4, 5]
                second_set = [5, 6, 7, 8, 9]

                print("\n Common member", obj.common_member(first_set, second_set))

                first_set = [1, 2, 3, 4, 5]
                second_set = [6, 7, 8, 9]

                print("\ncommon member", obj.common_member(first_set, second_set))

            elif choice == 10:

                """10. Write a program to print a specified list after removing the 0th, 4th and 5th elements"""

                print("\n list after removing 0th, 4th and 5th elements:", obj.remove_specific_element(main_list))

            elif choice == 11:

                """11. Write a Python program to generate all permutations of a list in Python. """

                list_1 = [1, 2, 3, 4, 5]

                print("permutations of a list in Python", obj.permute(list_1))

            elif choice == 12:

                """12. Write a Python program to get the difference between the two lists."""

                list_first = [10, 15, 20, 25, 30, 35, 40]
                list_second = [25, 40, 35]

                print("difference between the two lists:", obj.diff_list(list_first, list_second))

            elif choice == 13:

                """13. Write a Python program to append a list to the second list. """

                # Initializing lists
                list_third = [1, 4, 5, 6, 5]
                list_fourth = [3, 5, 7, 2, 5]

                print("list:", obj.append_list(list_third, list_fourth))

            elif choice == 14:

                """14. Write a python program to check whether two lists are circularly identical.  """

                list_one = [10, 10, 0, 0, 10]
                list_two = [10, 10, 10, 0, 0]
                list_three = [1, 10, 10, 0, 0]

                # check for list 1 and list 2
                if obj.circularly_identical(list_one, list_two):
                    print("list are circularly identical")
                else:
                    print("list are not circularly identical")

                # check for list 2 and list 3
                if obj.circularly_identical(list_two, list_three):
                    print("list are circularly identical")
                else:
                    print("list are not circularly identical")

            elif choice == 15:

                """15. Write a Python program to find common items from two lists.  """

                itemList_first = [1, 2, 3, 4, 5]
                itemList_second = [5, 6, 7, 8, 9]

                print("common items from two lists", obj.common_member(itemList_first, itemList_second))

                itemList_first = [1, 2, 3, 4, 5]
                itemList_second = [6, 7, 8, 9]

                print("common items from two lists", obj.common_member(itemList_first, itemList_second))

            elif choice == 16:

                """16. Write a Python program to split a list based on first character of word.  """

                word_list = ['give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

                for letter, words in groupby(sorted(word_list), key=itemgetter(0)):

                    print("\n letter:-", letter)

                    for word in words:
                        print("\n word:-", word)

            elif choice == 17:

                """17. Write a Python program to remove duplicates from a list of lists."""

                list_num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

                print("Original List:-", list_num)
                list_num.sort()

                new_num = list(list_num for list_num, _ in itertools.groupby(list_num))

                print("New List:-", new_num)

            else:
                print("Enter Valid choice between 0-16")

        except Exception as e:

            print(e)
