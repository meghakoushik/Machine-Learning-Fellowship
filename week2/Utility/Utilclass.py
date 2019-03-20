"""-----------------------------array programs---------------------------------"""
import textwrap


class Util:

    """ 1. Display the integer array"""

    # display array
    def display_array(self, arr):

        for _ in arr:
            # return all element in array
            return arr

    """ 2. Write a Python program to reverse the order of the items in the array. """

    # Reverse Array
    def reverse_array(self, arr):
        arr.reverse()
        for temp in range(len(arr)):
            return arr

    """ 3. Write a Python program to get the number of occurrences of a specified element in an array.  """

    # Count
    def count_element(self, arr):
        temp = arr.count(10)
        return temp

    """ 4. Write a Python program to remove the first occurrence of a specified element from an array. """

    # Remove Element
    def remove_element(self, arr):
        arr.remove(30)
        return arr

    """--------------------------dictionary program ---------------------------------------"""

    """1. Write a Python script to sort (ascending and descending) a dictionary by value. """

    def asc_order(self, dict_numbers):
        asc_dict = sorted(dict_numbers.values())
        return asc_dict

    def desc_order(self, dict_numbers):
        dec_sort = sorted(dict_numbers.values(), reverse=True)
        return dec_sort

    """2. add the key into the dictionary"""

    def add_dict(self, dict_numbers):
        first_dict = dict_numbers["Fifth"] = 5
        return first_dict

    """3. Write a Python script to concatenate following dictionaries to create a new one"""

    def concatenate_dict(self, dict_first, dict_second, dict_third):
        for _ in (dict_first, dict_second, dict_third):
            dict_fourth = dict(dict_first)
            dict_fourth.update(dict_second)
            dict_fourth.update(dict_third)
        return dict_fourth

    """4. write a Python program to iterate over dictionaries using for loops."""

    def iterate_dict(self, dict_value):
        for key, value in dict_value.items():
            print("\n key:%s" % key)
            print(" value:%s" % value)

    """5. write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the 
          form (x, x*x) """

    def create_dict(self):
        try:
            num = input("Enter a num")
            num1 = int(num)
            if num.isdigit():
                dict1 = {x: x * x for x in range(1, num1 + 1)}
                return dict1
            else:
                raise ValueError

        except ValueError:
            print("Enter number only")

    """6. Write a Python program to remove a key from a dictionary."""

    def remove_key(self, dict_value) :
        try :
            del dict_value['first ']
            return dict_value
        except KeyError :
            print("Invalid Key or key not present in dictionary")

    """7. Write a Python program to print all unique values in a dictionary."""

    def unique_dict(self, dictionary_values) :
        unique = set(val for dic in dictionary_values for val in dic.values())
        # for element in unique:
        return unique

    """8. Track the count of the letters from the string."""

    def count_dict(self, string) :
        res = {}
        for keys in string :
            res[keys] = res.get(keys, 0) + 1
        print(" Count of all characters in  is : \n" + str(res))

    """9. Write a Python program to print a dictionary in table format."""

    def table_dict(self, my_dict) :
        for row in zip(*([key] + value for key, value in sorted(my_dict.items()))) :
            print(*row)

    """11. Write a Python program to convert a list into a nested dictionary of keys."""

    def nested_dictionary(self, num_list) :
        main_list = ttt = {}
        for i in num_list :
            ttt[i] = {}
            ttt = ttt[i]
            print(main_list)

    """12.Write a Python program to check multiple keys exists in a dictionary. """

    def key_matching(self, dict_value) :
        if 'second ' in dict_value :

            return print(" Yes 'second' key exists in dictionary")

        else :

            raise KeyError
        print('\n key does not exists in dictionary')

    """13. Write a Python program to count number of items in a dictionary value"""

    def count_number(self, dict) :
        count = sum(map(len, dict.values()))
        return count

    "--------------------sets---------------------------"
    "1. Write a Python program to create a sets. "
    def create_set1(self) :
        # Creating two sets
        setA = {1, 2, 3, 4, 5}
        setB = {0, 2, 4, 6, 8}
        return setA, setB

    "1. Write a Python program to create an intersection of sets. "

    """2. Write a Python program to iteration over sets. """

    # display set
    def display_set(self, set_number) :
        for temp in set_number :
            print(temp)

    """3. Write a Python program to add member(s) in a set."""

    # add set
    def add_set(self, temp) :
        temp.update([1, 6, 8, 9, 2])
        return temp

    """4. Write a Python program to remove item(s) from set"""

    # remove set
    def remove_set(self, set_number) :
        try :
            set_number.remove(45)

        except KeyError:
            return "enter valid index"
        finally :
            return set_number

    """5. Write a Python program to remove an item from a set if it is present in the set. """

    # discard set
    def discard_set(self, set_number) :
        set_number.discard(88)

    """6. Write a Python program to create an intersection of sets."""

    # intersection set
    def intersection_set(self, set_third, set_fourth) :
        set_result = set_third.intersection(set_fourth)
        return set_result

    """7. Write a Python program to create a union of sets"""

    # union set
    def union_set(self, set_third, set_fourth) :
        set_result = (set_third | set_fourth)
        return set_result

    """8. Write a Python program to create set difference. """

    # set difference
    def diff_set(self, set_third, set_fourth) :
        setDifference = set_third.difference(set_fourth)
        return setDifference, set_third, set_fourth

    """9. Write a Python program to create a symmetric difference. """

    # symmetric diff
    def sys_diff(self, set_third, set_fourth) :
        set_fifth = set_third.symmetric_difference(set_fourth)
        set_sixth = set_fourth.symmetric_difference(set_third)
        return set_fifth, set_sixth

    """10. Write a Python program to clear a set. """

    # clear set
    def clr_set(self, set_number) :
        set_number.clear()

    """11. Write a Python program to use of frozen sets. """

    # frozen set
    def frozen_set(self) :
        vowels = ('a', 'e', 'i', 'o', 'u')
        setVowels = frozenset(vowels)
        return setVowels

    """12. Write a Python program to find maximum and the minimum value in a set. """

    # maximum value
    def max_set(self, set_value) :
        setMax = max(set_value)
        return setMax

    # minimum value
    def min_set(self, set_value) :
        setMin = min(set_value)
        return setMin

    """-------------------------tuples---------------------------------"""

    """1. Write a Python program to create a tuple."""

    # create tuple

    def tuple_create(self) :
        tuple_number = ("apple", "banana", "cherry")
        return tuple_number

    """2. Write a Python program to create a tuple with different data types."""

    # create a tuple with different data types

    def tuple_datatype(self) :
        thistuple = ("python", " tutorial", 1, " phy", 99)
        return thistuple

    """3. Write a Python program to unpack a tuple in several variables."""

    # unpack tuple
    def unpack_tuple(self, tuple_variable) :
        (college, student, type_of_college) = tuple_variable
        return college, student, type_of_college

    """4. Write a Python program to create the colon of a tuple."""

    # colon of a tuple

    def Cloning(self, list_number) :
        list_copy = []
        list_copy.extend(list_number)
        return list_copy

    """5. Write a Python program to find the repeated items of a tuple."""

    # repeated items of a tuple

    def repeat_element(self, vowels) :
        list1 = []
        list2 = list(vowels)
        for var in list2 :
            if list2.count(var) > 1 :
                list1.append(var)

        set1 = set(list1)
        return set1, list2

    """6. Write a Python program to check whether an element exists within a tuple."""

    def exist_element(self, number) :
        try :
            pos = number.index(23)
            return " Element Found at position : ", pos

        except ValueError as e :
            return e

    """8. Write a Python program to remove an item from a tuple."""

    def remove_items(self, tuple_number):
        try:
            pos = 2
            tuple_number = tuple_number[: pos] + tuple_number[pos + 1:]
            list1 = list(tuple_number)
            list1.remove(pos)
            tuple_number = tuple(list1)
            return tuple_number
        except IndexError :
            print("enter index not found")

    """10. Write a Python program to reverse a tuple."""

    # reverse a tuple

    def Reverse_tuple(self, number):
        new_tuple = number[::-1]
        return new_tuple

    """---------------------list-----------------------"""

    "2. Write a Python program to multiplies all the items in a list."

    # multiplies all the items in a list

    def multi_list(self, main_list):
        my_new_list = [i * 5 for i in main_list]
        return my_new_list

    "3. Write a Python program to get the smallest number from a list."

    # smallest number from a list

    def min_list(self, main_list):
        list2 = min(main_list)
        return list2

    "4. To count string length there first and last character are same from a given list of strings"

    # first and last character are same from a given list of strings

    def match_words(self, words_list):
        count = 0

        for word in words_list:
            if len(word) > 1 and word[0] == word[-1]:
                count += 1
        return count

    "5. To sorted in increasing order by the last element in each tuple from a given list of non-empty tuples"

    def last(self, n):
        return n[-1]

    def sort(self, Sample_List):
        return sorted(Sample_List, key=self.last)

    "6. Write a Python program to remove duplicates from a list."

    # element remove
    def remove_Duplicates(self, main_list):
        list1 = []

        for var in main_list:
            if main_list.count(var) > 1:
                list1.append(var)

        set1 = set(main_list)
        return set1

    "7. Write a Python program to clone or copy a list."

    # cloning

    def cloning_list(self, main_list):
        list_copy = main_list[:]
        return list_copy

    "8.program to find the list of words that are longer than n from a given list of words."

    def longer_words(self, n, str):
        word_len = []
        txt = str.split(" ")
        for x in txt:
            if len(x) > n:
                word_len.append(x)
        return word_len

    "9. Write a Python function that takes two lists and returns True if they have aleast one common member."

    # commons member

    def common_member(self, first_set, second_set):
        set_first = set(first_set)
        set_second = set(second_set)
        if set_first & set_second:
            return True
        else:
            return False

    "10. program to print a specified list after removing the 0th, 4th and 5th elements."

    # remove specific element

    def remove_specific_element(self, list1):
        my_list = [x for (i, x) in enumerate(list1) if i not in (0, 4, 5)]
        return my_list

    "11. Write a Python program to generate all permutations of a list in Python."

    # permutations

    def permute(self, list_1):
        num = len(list_1)
        result = []
        temp1 = num * [0]

        result.append(list_1)

        i = 0
        while i < num:
            if temp1[i] < i:
                if i % 2 == 0:
                    tmp = list_1[0]
                    list_1[0] = list_1[i]
                    list_1[i] = tmp

                else:

                    tmp = list_1[temp1[i]]
                    list_1[temp1[i]] = list_1[i]
                    list_1[i] = tmp

                result.append(list_1)
                temp1[i] += 1
                i = 0
            else :
                temp1[i] = 0
                i += 1

        return result

    "12. Write a Python program to get the difference between the two lists."

    # difference between the two lists

    def diff_list(self, list_A, list_B) :
        return list(set(list_A) - set(list_B))

    "13. Write a Python program to append a list to the second list."

    # append a list to the second list

    def append_list(self, list1, list2) :
        my_list = list2 + list1
        return my_list

    "14. Write a python program to check whether two lists are circularly identical."

    # two lists are circularly identical

    def circularly_identical(self, list_one, list_two) :
        return ' '.join(map(str, list_two)) in ' '.join(map(str, list_one * 2))

    "15. Write a Python program to find common items from two lists."

    def common_member(self, itemList_first, itemList_second) :
        first_set = set(itemList_first)
        second_set = set(itemList_second)
        # check length

        if len(first_set.intersection(second_set)) > 0 :
            return second_set.intersection(second_set)
        else :
            return "no common elements"

    "16. Write a Python program to split a list based on first character of word."
    "-------------------------string----------------------------"

    """ 1. Write a Python program to calculate the length of a string."""

    def string_validation(self) :
        try :
            string = input("Enter string")

            if string.isalpha() :
                print("length of string", len(string))
                print(string)
            else :
                raise ValueError
        except ValueError :
            print("Letter only Please")

    """ 2. Write a Python program to count the number of characters (character frequency) in a string.  """

    def char_frequency(self, str1) :
        dict = {}
        for n in str1 :
            keys = dict.keys()
            if n in keys :
                dict[n] += 1
            else :
                dict[n] = 1
        return dict

    def count_char(self, string) :
        res = {}
        for keys in string :
            res[keys] = res.get(keys, 0) + 1
        print(" Count of all characters in  is : \n" + str(res))

    """3. Write a Python program to get a string from a given string where all occurrences of
             its first char have been changed to '$', except the first char itself.  """

    def changed_char(self, string) :
        char = string[0]
        string = string.replace(char, '$')
        string = char + string[1 :]
        return string

    """4. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
                 If the given string already ends with 'ing' then add 'ly' instead. 
                 If the string length of the given string is less than 3, leave it unchanged."""

    def isConSpace(self, string) :
        for temp in string :
            if temp == " " :
                return True
        return False

    def string_add(self) :

        string = input("Enter a string : ")

        if len(string) > 0 :
            if self.isConSpace(string) == False :

                if string.isalpha() :

                    if len(string) > 2 :

                        if string[-3 :] == "ing" :
                            string += "ly"
                            print(string)
                        else :
                            string += "ing"
                            print(string)
                    else :
                        print(string)
                else :
                    print("String must be contain only alphabet.")
            else :
                print("Please enter a string without space.")
        else :
            print("String is empty.")

    """5. Write a Python function that takes a list of words and returns the length of the longest one.  """

    def longest_words(self, list_words) :

        max1 = len(list_words[0])
        temp1 = list_words[0]
        for temp2 in list_words :
            if len(temp2) > max1 :
                max1 = len(temp2)
                temp1 = temp2
        return temp1

    """6. Python script that takes input  displays that input back in upper and lower cases."""

    def upper_str(self, string):
        string_one = string.upper()
        return string_one

    def lower_str(self, string):
        string_two = string.lower()
        return string_two
    """7. """
    def comma_seperated(self, words):

        words = [items for items in words.split(",")]
        return ",".join(sorted(list(set(words))))

    """9. Write a Python program to display formatted text (width=50) as output."""

    def wrapped_data(self, value) :
        # Wrap text.
        wrapper = textwrap.TextWrapper(width=50)

        word_list = wrapper.wrap(text=value)

        # Print each line.

        for element in word_list :
            return element

    """11. Write a Python program to reverse a string."""

    def reverse_string(self, string_one) :
        string = ""
        for i in string_one :
            string = i + string
        return string
