#program to get numbers divisible by fifteen from a list using an anonymous function.


list1 = [17, 20, 25, 18]

Result= list(filter(lambda x: [x % 15 == 0], list1))
print('numbers divisible by 15 into the list:', Result)

