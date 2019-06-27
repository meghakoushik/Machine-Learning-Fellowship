from week2.Utility.Utilclass import Util


class Tuple:
    obj = Util()

    number = (82, 23, 13, 55, 44, 76, 83, 34, 78)

    flag = True

    print("1. Python program to create a tuple. ")
    print("2. Python program to create a tuple with different data types ")
    print("3. Python program to unpack a tuple in several variables.")
    print("4. Python program to create the colon of a tuple.")
    print("5. Python program to find the repeated items of a tuple")
    print("6. Python program to check whether an element exists within a tuple. ")
    print("7. Python program to convert a list to a tuple. ")
    print("8. Python program to remove an item from a tuple.")
    print("9. Python program to slice a tuple.")
    print("10.Python program to reverse a tuple")
    print("0. EXIT")

    while flag:

        try:
            print('_____________________________________________')

            choice = int(input("Enter your choice"))

            if choice == 0:
                flag = False

            elif choice == 1:

                """1. Python program to create a tuple."""

                print("\n Tuple:", obj.tuple_create())

            elif choice == 2:

                """2. Python program to create a tuple with different data types"""

                print("\n tuple with different data types", obj.tuple_datatype())

            elif choice == 3:

                """3. Python program to unpack a tuple in several variables."""

                tuple_variable = ("IIM", 5000, "Engineering")

                print("output:", obj.unpack_tuple(tuple_variable))

            elif choice == 4:

                """4. Python program to create the colon of a tuple."""

                list_number = [4, 8, 2, 10, 15, 18]

                print("\n Original List:", list_number)
                print("\n After Cloning:", obj.Cloning(list_number))

            elif choice == 5:

                """5. Python program to find the repeated items of a tuple"""

                vowels = ('a', 'e', 'i', 'o', 'i', 'o', 'e', 'i', 'u')

                print("\n Repeated element:", obj.repeat_element(vowels))

            elif choice == 6:

                """6. Python program to check whether an element exists within a tuple."""

                print("original tuple numbers:", number)
                print("numbers:", obj.exist_element(number))

            elif choice == 7:

                """7. Python program to convert a list to a tuple. """

                list_element = [1, 34, 435, 546]

                print("\n convert a list to a tuple", tuple(list_element))

            elif choice == 8:

                """8. Python program to remove an item from a tuple."""
                tuple_number = [2, 3, 4, 5, 56]
                print("Modified Tuple:", obj.remove_items(tuple_number))

            elif choice == 9:

                """9. Python program to slice a tuple."""

                print("\n slice of tuple ", number[2:])

            elif choice == 10:

                """10.Python program to reverse a tuple"""

                print("\nOriginal Tuple", number)

                print("Reverse Tuple", obj.Reverse_tuple(number))

            else:
                print("enter valid choice between 0-10")

        except Exception as e:
            print(e)
