#program to retrieve file properties

import os.path
import time

#print all the properties of file

print('file_name:', __file__)
print('access_time:', time.ctime(os.path.getatime(__file__)))
print('modified_time:', time.ctime(os.path.getmtime(__file__)))
print('changed_time:', time.ctime(os.path.getctime(__file__)))
print('size:', (os.path.getsize(__file__)))