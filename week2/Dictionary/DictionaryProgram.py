from week2.Utility.Utilclass import Util


class Dictionary:
    obj = Util()

    dict_numbers = {'first': 1, 'second': 2, 'third': 3, 'Fourth': 4}

    dictionary_values = {'first_value': 1, 'second_value': 2, 'third_value': 3, 'fourth_value': 4, 'Fifth_value': 5, 'Sixth_value': 6,
                         'Seventh_value': 7}

    flag = True

    print("1. Write a Python script to sort (ascending and descending) a dictionary by value. ")
    print("2. Write a Python script to add a key to a dictionary. ")
    print("3. Write a Python script to concatenate following dictionaries to create a new one.")
    print("4. Write a Python program to iterate over dictionaries using for loops.")
    print("5. Write a Python script to generate dictionary a number (between 1 and n) in the form (x, x*x)")
    print("6. Write a Python program to remove a key from a dictionary. ")
    print("7. Write a Python program to print all unique values in a dictionary.")
    print("8. Write a Python program to create a dictionary from a string. ")
    print("9. Write a Python program to print a dictionary in table format.")
    print("10. Write a Python program to count the values associated with key in a dictionary. ")
    print("11. Write a Python program to convert a list into a nested dictionary of keys.")
    print("12. Write a Python program to check multiple keys exists in a dictionary")
    print("13. Write a Python program to count number of items in a dictionary value that is a list.")
    print("0. EXIT")

    while flag:

        try:

            print("___________________________________________________________________________")
            choice = int(input("Enter your choice"))

            if choice == 0:
                flag = False

            elif choice == 1:

                """1. Write a Python script to sort (ascending and descending) a dictionary by value. """

                print("Dictionary:", dict_numbers)

                print("\n Sort Dictionary in ascending order:", obj.asc_order(dict_numbers))
                print("Sort Dictionary in descending order:", obj.desc_order(dict_numbers))

            elif choice == 2:

                """2. Write a Python script to add a key to a dictionary. """

                print("\n Add key into dictionary:", obj.add_dict(dict_numbers))

                print("Updated Dictionary", dict_numbers)

            elif choice == 3:

                """3. Write a Python script to concatenate following dictionaries to create a new one. """

                dict_first = {'first': 1, 'second': 2, 'third': 3}
                dict_second = {'fourth': 4, 'Fifth': 5}
                dict_third = {'Sixth': 6, 'Seventh': 7}

                print("\nconcatenate dictionary:", obj.concatenate_dict(dict_first, dict_second, dict_third))

            elif choice == 4:

                """4. Write a Python program to iterate over dictionaries using for loops. """

                print("iterate over dictionary:", obj.iterate_dict(dictionary_values))

            elif choice == 5:

                """5. Write a Python script to generate and print a dictionary that contains 
                    a number (between 1 and n) in the form (x, x*x)"""

                print("dictionary that contains a number in the form (x, x*x)", obj.create_dict())

            elif choice == 6:
                """6. Write a Python program to remove a key from a dictionary. """

                dict5 = {'first_value': 1, 'second_value': 2, 'third_value': 3, 'fourth_value': 4, 'Fifth_value': 5, 'Sixth_value': 6,
                         'Seventh_value': 7}

                # using Utility obj call del_dict()
                # return dictionary

                print("\n original dictionary :", dictionary_values)
                print("\n dictionary after deleting key:", obj.remove_key(dictionary_values))

            elif choice == 7:

                """7. Write a Python program to print all unique values in a dictionary. """

                dictionary_values = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
                                     {"V": "S009"}, {"VIII": "S007"}]

                # call unique_dict function
                # return dict
                print("\n unique values is :", obj.unique_dict(dictionary_values))

            elif choice == 8:

                """8. Write a Python program to create a dictionary from a string. 
                    Note: Track the count of the letters from the string.
                    Sample string : 'w3resource'
                    Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
                """
                sample_string = "w3resource"
                print("original string:", sample_string)

                print("Dictionary from a string", obj.count_dict(sample_string))

            elif choice == 9:

                """9. Write a Python program to print a dictionary in table format. """

                my_dict = {'col1': [11, 12], 'col2': [55, 66], 'col3': [99, 10]}
                print(obj.table_dict(my_dict))

            elif choice == 10:

                """10. Write a Python program to count the values associated with key in a dictionary. """

                # create dictionary

                student = [{'id': 1, 'success': True, 'name': 'Lary'},
                           {'id': 2, 'success': False, 'name': 'Rabi'},
                           {'id': 3, 'success': True, 'name': 'Alex'}]

                print("\n Count of how many dictionaries have success as True:", sum(d['success'] for d in student))

            elif choice == 11:

                """11. Write a Python program to convert a list into a nested dictionary of keys. """

                # list
                num_list = [1, 2, 3, 4]
                print("original list:", num_list)
                print("\n nested dictionary:", obj.nested_dictionary(num_list))

            elif choice == 12:

                """12. Write a Python program to check multiple keys exists in a dictionary. """
                dictionary_values = {'first_value': 1, 'second_value': 2, 'third_value': 3, 'fourth_value': 4, 'Fifth_value': 5, 'Sixth_value': 6,
                                     'Seventh_value': 7}

                print("key_dictionary:", obj.key_matching(dictionary_values))

            elif choice == 13:
                """13. Write a Python program to count number of items in a dictionary value that is a list."""

                dictionary = {'subjects1': ['subj1', 'subj2', 'subj3'], 'subjects2': ['subj1', 'subj2']}
                print("number of items in a dictionary value:", obj.count_number(dictionary))

            else:

                print("Enter Valid choice between 0-13")

        except Exception as e:

            print(e)
