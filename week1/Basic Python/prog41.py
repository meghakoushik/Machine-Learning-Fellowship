#program to convert an integer to binary keep leading zeros.

num_str = int(input("enter the no"))
num_bin_reversed = ''
while num_str > 0:
 if num_str % 2 == 0:

  num_str =int(num_str/2)
  num_remainder =1
  print("remainder is :", 0)
  num_bin_reversed = num_bin_reversed+'0'

  continue

 elif num_str %2 == 1:
  num_str = int(num_str/2)
  num_remainder = 1
  print("Remainder is:", 1)
  num_bin_reversed = num_bin_reversed+'1'


num_bin = num_bin_reversed[::-1]
print(num_bin)
if int(num_str) > 0:

 print('0b' + num_bin == bin(int(num_str)))