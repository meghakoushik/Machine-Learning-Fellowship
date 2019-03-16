#program to get the users environment

import os
print(os.environ)                       #Using python dictionary


HOME = os.environ['HOME']
print('HOME:', HOME)                             #print HOME directory

PATH = os.environ['PATH']
print('PATH:', PATH)                          #print PATH name of directory