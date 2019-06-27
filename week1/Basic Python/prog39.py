#program to find files and skip directories of a given directory.
import os


basepath = "/home/bridgeit/m.txt"
for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    if os.path.isdir(path):
        # skip directories
        continue
