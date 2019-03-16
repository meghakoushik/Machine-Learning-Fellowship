 #program to sort three integer number without using any conditional statement and loops

 #take the three input form user

a = int(input("enter the 1st no"))
b = int(input("enter the 2nd no"))
c = int(input("enter the 3rd no"))

#find minimum number
first = min(a, b, c)


#find maximum number
third = max(a, b, c)


#find middle number
second = (a+b+c) - (first+third)


#output sorted three integer number
print(first, second, third)
