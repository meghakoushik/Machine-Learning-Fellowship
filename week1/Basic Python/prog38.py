#program to add leading zero's to a string

string_a = 111
print('original string_a:{:<08d}'.format(111))


#with using string method

str = '123'
print("original string:", str)
str1 = str.ljust(5,'0')

print(str1)