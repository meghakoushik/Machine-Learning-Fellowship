# programs for checking elements is present or not in given list
# only one list ,where we search element
test_list = [4, 2, 3, 1, 5, 6]
if 9 in test_list:
    print("true")
else :
    print("false")


# programs for checking element is present or not in given list with function method
def in_list(list_number, n):
    for value in list_number:
        if n == value:
            return True
        else :
            return False
    print(in_list([2, 1, 4, 5], 2))
    print(in_list([2, 1, 4, 5], -1))
