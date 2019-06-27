#program to access and print a URL's content to the console.

import urllib.request

#open a connection of url using urllib request
webUrl = urllib.request.urlopen('https://www.google.com')

#read the data of url and print it
data = webUrl.read()
print(data)