# Sets Programs
from week2.Utility.Utilclass import Util


class Set:
    obj = Util()

    set_number = {9, 60, 7, 56}

    flag = True

    print("1. Write a Python program to create a set. ")
    print("2. Write a Python program to iteration over sets. ")
    print("3. Write a Python program to add member(s) in a set. ")
    print("4. Write a Python program to remove item(s) from set ")
    print("5. Write a Python program to remove an item from a set if it is present in the set.")
    print("6. Write a Python program to create an intersection of sets.")
    print("7. Write a Python program to create a union of sets.")
    print("8. Write a Python program to create set difference.")
    print("9. Write a Python program to create a symmetric difference.")
    print("10. Write a Python program to clear a set.")
    print("11. Write a Python program to use of frozen sets.")
    print("12. Write a Python program to find maximum and the minimum value in a set. ")
    print("0. EXIT")

    while flag:

        try:

            print('_________________________________________')

            choice = int(input("Enter your choice"))

            if choice == 0:
                flag = False

            elif choice == 1:

                """1. Write a Python program to create a set."""
                print("\n Set:", set_number)

            elif choice == 2:

                """2. Write a Python program to iteration over sets. """
                set2 = obj.display_set(set_number)

            elif choice == 3:

                """ 3. Write a Python program to add member(s) in a set"""

                print("\n Updated set:", obj.add_set(set_number))

            elif choice == 4:

                """ 4. Write a Python program to remove item(s) from set """

                print("set:", obj.remove_set(set_number))

            elif choice == 5:

                """ 5. Write a Python program to remove an item from a set if it is present in the set."""

                print("\n Original set :", set_number)

                print("\n After discard element", obj.discard_set(set_number))

                print("\n ", set_number)

            elif choice == 6:
                """ 6. Write a Python program to create an intersection of sets. """
                set_third = {1, 6, 3, 4, 5}
                set_fourth = {2, 4, 6, 3, 9}

                print(" \n Intersection of two sets", obj.intersection_set(set_third, set_fourth))

            elif choice == 7:

                """ 7. Write a Python program to create a union of sets."""

                print("\n Union of two sets", obj.union_set(set_third, set_fourth))

            elif choice == 8:

                """ 8. Write a Python program to create set difference."""

                print("\n set Difference", obj.diff_set(set_third, set_fourth))

            elif choice == 9:

                """ 9. Write a Python program to create a symmetric difference."""
                set_third = {'a', 'b', 'c', 'd'}
                set_fourth = {'c', 'd', 'e'}

                print("\n set symmetric Difference", obj.sys_diff(set_third, set_fourth))

            elif choice == 10:

                """ 10. Write a Python program to clear a set."""

                print("set ", obj.clr_set(set_number))

            elif choice == 11:

                """ 11. Write a Python program to use of frozen sets."""

                print("\nset frozen:", obj.frozen_set())

            elif choice == 12:

                """ 12. Write a Python program to find maximum and the minimum value in a set."""

                set_value = {33, 7, 88, 14}

                set_seven = obj.max_set(set_value)
                set_eight = obj.min_set(set_value)

                print("\n Maximum value in set", set_seven)
                print("\n Minimum value in set", set_eight)

            else:
                print("Enter valid choice Between 0-12")

        except Exception as e:
            print(e)
