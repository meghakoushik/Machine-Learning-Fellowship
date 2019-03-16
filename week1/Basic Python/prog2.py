# This program prints comma- Seperate no. from user and generate a list and tuple of this numbers.

data = input('enter the data:')
list_data = data.split(',')

tuple_data = tuple(list_data)

# displaying the list
print("list:", list_data)

# displaying the tuple
print("tuple:", tuple_data)
