#program to get the current value of the recursion limit.

import sys
print(sys.getrecursionlimit())

def recursion(counter):
    print(counter)

    counter +=1

print(recursion())