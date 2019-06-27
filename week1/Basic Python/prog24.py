#program to get the size of an object in type\


import sys
#take the input from user
a = int(input('enter the obj1'))
b = float(input('enter the obj2'))
d = str(input('enter the obj4'))

#print the size of an object
print( 'the size of an obj1:', +(sys.getsizeof(a)))
print('the size of an obj1:', +(sys.getsizeof(b)))
print('the size of an obj1:', +(sys.getsizeof(d)))
