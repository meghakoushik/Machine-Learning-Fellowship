#program to clear the screen or terminal.

from os import system, name
from time import sleep
# define our clear function
def clear():
   if name == 'nt':
      _ = system('clear')

sleep(5)
# now call function we defined above
clear()