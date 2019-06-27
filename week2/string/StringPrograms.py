from week2.Utility.Utilclass import Util


class String:
    obj = Util()
    flag = True

    print("1. Write a Python program to calculate the length of a string.  ")
    print("2. Write a Python program to count the number of characters (character frequency) in a string.   ")
    print("3. Python program str occurrences of its first char have been changed to '$', except the first char itself.")
    print("4. Python program to add 'ing' at the end of a given str. If ends with 'ing' then add 'ly' instead")
    print("5. Write a Python function that takes a list of words and returns the length of the longest one.")
    print("6. Python script that takes input from the user and displays that input back in upper and lower cases. ")
    print("7. program accepts a comma separated sequence of words as input and prints the unique words in sorted form ")
    print("8. Write a Python program to get the last part of a string before a specified character.  ")
    print("9. Write a Python program to display formatted text (width=50) as output. ")
    print("10. Write a Python program to count occurrences of a substring in a string.  ")
    print("11. Write a Python program to reverse a string. ")
    print("12. Write a Python program to lowercase first n characters in a string. ")
    print("0. EXIT")

    while flag:

        try:

            print("______________________________________________________________________")

            choice = int(input("Enter your choice"))

            if choice == 0:
                flag = False

            elif choice == 1:

                """1. Write a Python program to calculate the length of a string. """

                # call by string_validation () in Utility
                print(obj.string_validation())

            elif choice == 2:

                """2. Write a Python program to count the number of characters (character frequency) in a string.  """

                print(obj.char_frequency('stringCharacter'))

            elif choice == 3:

                """3. Write a Python program to get a string from a given string where all occurrences of
                 its first char have been changed to '$', except the first char itself.  """

                try:
                    characters = str(input("enter the characters:"))
                    if characters.isalpha():
                        print(obj.changed_char(characters))
                    else:
                        raise ValueError
                except ValueError:
                    print("enter only character value")
                    print("integer value is not valid")

            elif choice == 4:

                """4. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
                 If the given string already ends with 'ing' then add 'ly' instead. 
                 If the string length of the given string is less than 3, leave it unchanged."""

                print(obj.string_add())

            elif choice == 5:

                """5. Write a Python function that takes a list of words and returns the length of the longest one.  """

                try:
                    list_words = []
                    num = input("Enter the number of elements in list:")
                    num1 = int(num)
                    if num.isdigit():
                        pass
                        try:
                            for temp in range(0, num1):
                                string = input("Enter element" + str(temp + 1) + ":")
                                if string.isalpha():
                                    list_words.append(string)
                                    s1 = obj.longest_words(list_words)
                                else:
                                    raise Exception
                            print("longest words", s1)
                        except Exception as e:
                            print("enter string only", e)
                    else:
                        raise Exception
                except Exception as e:
                    print("enter digit only", e)
                    try:
                        print("The word with the longest length is:", s1)
                    except NameError:
                        print("Enter valid string")

            elif choice == 6:

                """6. Python script that takes input  displays that input back in upper and lower cases."""

                try:
                    string = str(input("enter the string"))
                    if string.isalpha(string):
                        print("Upper case", obj.upper_str(string))
                        print("Upper case", obj.lower_str(string))
                    else:
                        raise ValueError
                except:
                    print("invalid input ")
                    print("enter only character values")
            elif choice == 7:

                """7. Write a Python program that accepts a comma separated sequence of words as input and 
                    prints the unique words in sorted form (alphanumerically)."""

                try:
                    words = str(input("enter a separated sequence of words:"))
                    if words.isalpha():
                        print(obj.comma_seperated(words))
                    else:
                        raise ValueError
                except ValueError:
                    print("enter only character value")
                    print("integer value is not valid")

            elif choice == 8:

                """8. Write a Python program to get the last part of a string before a specified character. """

                given_string = 'https://www.w3resource.com/python-exercises/string'
                print(given_string.rsplit('/', 1)[0])
                print(given_string.rsplit('-', 1)[0])

            elif choice == 9:

                """9. Write a Python program to display formatted text (width=50) as output."""

                value = """This function wraps the input paragraph such that each line in the paragraph is at most width
                        characters long. The wrap method returns a list of output lines.The returned list is empty if 
                        the wrapped output has no content."""

                print("Formatted text:", obj.wrapped_data(value))

            elif choice == 10:

                """10. Write a Python program to count occurrences of a substring in a string. """

                string = "Python Programming"
                substring = "i"
                count = string.count(substring)
                # print count
                print("The count is:", count)

            elif choice == 11:

                """11. Write a Python program to reverse a string."""
                try:
                    main_string = str(input("enter the string"))
                    if main_string.isalpha():
                        print("reversed string is:", obj.reverse_string(main_string))
                    else:
                        raise ValueError
                except ValueError:
                    print("Enter valid character values")

            elif choice == 12:

                """12. Write a Python program to lowercase first n characters in a string. """

                string_character = 'PyThon ProGramminG'
                print(string_character[:4].lower() + string_character[4:])

            else:
                print("Enter Valid choice between 0-12")

        except Exception as e:

            print(e)
