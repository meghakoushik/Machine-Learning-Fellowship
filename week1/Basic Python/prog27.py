#program to get the system time


import time

#time object contains current time
t = time.time()


#print the current time
#string represantation time format

current_time= time.strftime("%H:%M:%D:%Y")
print('current_time=', current_time)

