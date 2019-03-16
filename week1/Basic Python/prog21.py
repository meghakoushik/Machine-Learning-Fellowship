#program to sort files by date


import glob
import os
import time

searchedfile = glob.glob("*.py")
files = sorted( searchedfile, key = lambda file: os.path.getctime(file))

for file in files:
 print("{} - {}".format(file, time.ctime(os.path.getctime(file))))