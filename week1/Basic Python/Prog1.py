# Python program to Reverse First and last name

first = input("Enter First name")
second = input("Enter Last name")
# Display the Reverse name
print(second + "  " + first)
# second method : if you want reverse name separately
print(first[::-1] + "" + second[::-1])
