
#program to determine if the python shell is executing in 32bit or 64bit mode on operating system.

import struct

#calculate the no of bits and print it
print(struct.calcsize('P') * 8)