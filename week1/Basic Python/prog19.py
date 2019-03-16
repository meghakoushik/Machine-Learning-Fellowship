#program to get file creation and modification date and times.

import os, time, datetime

file = "Addition.py"


modified = os.path.getmtime(file)
print("Date modified: "+time.ctime(modified))
print("Date modified:", datetime.datetime.fromtimestamp(modified))

created = os.path.getctime(file)
print("Date created: "+time.ctime(created))
print("Date created:", datetime.datetime.fromtimestamp(created))
