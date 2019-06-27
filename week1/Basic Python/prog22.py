#program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.


import sys

print('Name of the script:', sys.argv[0])              #display name of the script

argument_list = len(sys.argv[0])-1                       #count length

print('The no. of arguments:', argument_list)            #display count of arguments

print('Arguments:', str(sys.argv))
