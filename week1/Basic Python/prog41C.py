#program to convert an integer to binary keep leading zeros.
integer_number = input("enter the no")

integer_number = int(integer_number)


result = ''
for x in range(8):

 number = (integer_number%2)
 integer_number = integer_number//2
 result= (result + str(number))
 result=result[::-1]

print(result)