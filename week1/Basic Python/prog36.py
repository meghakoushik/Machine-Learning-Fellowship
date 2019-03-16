#programm to determine if variables is defined or not

try:
    variable = 1

except NameError:

    print('variable is not defined')

else:
    print('variable is defined')

try:
    variable
except NameError:
    print('variable is not defined')

else:
    print('variable is  defined')

