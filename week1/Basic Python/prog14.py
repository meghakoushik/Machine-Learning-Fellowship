# program to list all files in a directory
from os import walk

for filename in walk('/home/bridgeit'):
    print(filename)
